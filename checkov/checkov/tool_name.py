#!/usr/bin/env python
import atexit
import json
import logging
import os
import shutil
import signal
import sys
from pathlib import Path
from typing import Any, List, Optional

import argcomplete
import configargparse
from urllib3.exceptions import MaxRetryError

from checkov.common.util.data_structures_utils import SEVERITY_RANKING

signal.signal(signal.SIGINT, lambda x, y: sys.exit(''))

from checkov.arm.runner import Runner as arm_runner
from checkov.cloudformation.runner import Runner as cfn_runner
from checkov.common.bridgecrew.bc_source import SourceTypes, BCSourceType, get_source_type
from checkov.common.bridgecrew.vulnerability_scanning.image_scanner import image_scanner
from checkov.common.bridgecrew.integration_features.integration_feature_registry import integration_feature_registry
from checkov.common.bridgecrew.platform_integration import bc_integration
from checkov.common.goget.github.get_git import GitGetter
from checkov.common.output.baseline import Baseline
from checkov.common.output.report import CheckType
from checkov.common.runners.runner_registry import RunnerRegistry, OUTPUT_CHOICES
from checkov.common.checks.base_check_registry import BaseCheckRegistry
from checkov.common.util.banner import banner as checkov_banner
from checkov.common.util.config_utils import get_default_config_paths
from checkov.common.util.consts import DEFAULT_EXTERNAL_MODULES_DIR
from checkov.common.util.docs_generator import print_checks
from checkov.common.util.ext_argument_parser import ExtArgumentParser
from configargparse import ArgumentParser
from checkov.common.util import prompt
from checkov.common.util.runner_dependency_handler import RunnerDependencyHandler
from checkov.common.util.type_forcers import convert_str_to_bool
from checkov.dockerfile.runner import Runner as dockerfile_runner
from checkov.helm.runner import Runner as helm_runner
from checkov.kubernetes.runner import Runner as k8_runner
from checkov.logging_init import init as logging_init
from checkov.runner_filter import RunnerFilter
from checkov.secrets.runner import Runner as secrets_runner
from checkov.serverless.runner import Runner as sls_runner
from checkov.terraform.plan_runner import Runner as tf_plan_runner
from checkov.terraform.runner import Runner as tf_graph_runner
from checkov.json_doc.runner import Runner as json_runner
from checkov.github.runner import Runner as github_configuration_runner
from checkov.kustomize.runner import Runner as kustomize_runner
from checkov.gitlab.runner import Runner as gitlab_configuration_runner
from checkov.sca_package.runner import Runner as sca_package_runner

from typing import List, Dict, Tuple
from checkov.common.runners.base_runner import BaseRunner, filter_ignored_paths
from checkov.common.parallelizer.parallel_runner import parallel_runner
from checkov.serverless.parsers.parser import parse
from checkov.common.parsers.node import DictNode
from checkov.cloudformation.checks.resource.registry import cfn_registry
from checkov.serverless.checks.complete.registry import complete_registry
from checkov.serverless.checks.custom.registry import custom_registry
from checkov.serverless.checks.function.registry import function_registry
from checkov.serverless.checks.layer.registry import layer_registry
from checkov.serverless.checks.package.registry import package_registry
from checkov.serverless.checks.plugin.registry import plugin_registry
from checkov.serverless.checks.provider.registry import provider_registry
from checkov.serverless.checks.service.registry import service_registry

from serverless.parsers.sls_attack_graph import SlsAttackGraph

from checkov.version import version

outer_registry = None

logging_init()
logger = logging.getLogger(__name__)

SLS_FILE_MASK = os.getenv(
    "CKV_SLS_FILE_MASK", "serverless.yml,serverless.yaml").split(",")

MULTI_ITEM_SECTIONS = [
    ("functions", function_registry),
    ("layers", layer_registry)
]
SINGLE_ITEM_SECTIONS = [
    ("custom", custom_registry),
    ("package", package_registry),
    ("plugins", plugin_registry),
    ("provider", provider_registry),
    ("service", service_registry)
]


def run(banner: str = checkov_banner, argv: List[str] = sys.argv[1:]) -> Optional[int]:
    default_config_paths = get_default_config_paths(sys.argv[1:])
    parser = ExtArgumentParser(description='Infrastructure as code static analysis',
                               default_config_files=default_config_paths,
                               config_file_parser_class=configargparse.YAMLConfigFileParser,
                               add_env_var_help=True)
    add_parser_args(parser)
    argcomplete.autocomplete(parser)
    config = parser.parse_args(argv)

    # Check if --output value is None. If so, replace with ['cli'] for default cli output.
    if config.output is None:
        config.output = ['cli']

    logger.debug(f'Checkov version: {version}')
    logger.debug(f'Python executable: {sys.executable}')
    logger.debug(f'Python version: {sys.version}')
    logger.debug(f'Checkov executable (argv[0]): {sys.argv[0]}')
    logger.debug(parser.format_values(sanitize=True))

    excluded_paths = config.skip_path or []

    if config.var_file:
        config.var_file = [os.path.abspath(f) for f in config.var_file]

    if config.directory:
        logging.error('directory only implemented for debugging purposes. Please use -l')
        input('Press any key to continue')
        exit_codes = []
        for root_folder in config.directory:
            file = config.file
            files = file

            files_list = []
            filepath_fn = None

            if files:
                files_list = [file for file in files if os.path.basename(file) in SLS_FILE_MASK]

            if root_folder:
                filepath_fn = lambda f: f'/{os.path.relpath(f, os.path.commonprefix((root_folder, f)))}'
                for root, d_names, f_names in os.walk(root_folder):
                    # Don't walk in to "node_modules" directories under the root folder. If –for some reason–
                    # scanning one of these is desired, it can be directly specified.
                    if "node_modules" in d_names:
                        d_names.remove("node_modules")

                    filter_ignored_paths(root, d_names, excluded_paths)
                    filter_ignored_paths(root, f_names, excluded_paths)
                    for file in f_names:
                        if file in SLS_FILE_MASK:
                            full_path = os.path.join(root, file)
                            if "/." not in full_path:
                                # skip temp directories
                                files_list.append(full_path)

            sls_ag = SlsAttackGraph(files_list, filepath_fn)
            definitions, definitions_raw = sls_ag.definitions, sls_ag.definitions_raw

            # Filter out empty files that have not been parsed successfully
            definitions = {k: v for k, v in definitions.items() if v}
            definitions_raw = {k: v for k, v in definitions_raw.items() if k in definitions.keys()}

            for sls_file, sls_file_data in definitions.items():
                logger.error(f"Template Dump for {sls_file}: {sls_file_data}")

        exit_code = 1 if 1 in exit_codes else 0
        return exit_code
    elif config.file:
        logging.error('File only implemented for debugging purposes. Please use -l')
        input('Press any key to continue...')
        files = config.file

        sls_ag = SlsAttackGraph(files, None)
        definitions, definitions_raw = sls_ag.definitions, sls_ag.definitions_raw

        # Filter out empty files that have not been parsed successfully
        definitions = {k: v for k, v in definitions.items() if v}
        definitions_raw = {k: v for k, v in definitions_raw.items() if k in definitions.keys()}

        for sls_file, sls_file_data in definitions.items():
            print(f"Template Dump for {sls_file}: {sls_file_data}")

        for ag in sls_ag.attack_graphs:
            for fact in sorted(list(ag.facts)):
                print(fact)
    elif config.list:
        with open('../../misc-scripts/model.pl', 'r') as template_file:
            template = template_file.read()
        
        with open('../../misc-scripts/data/sec-policy-only.csv', 'r') as csvfile, open('../../misc-scripts//data/parsed-permissions.csv', 'w') as permission_file:
            permission_file.write('file,global_iam_stmts,min_fn_iam_stmts,max_fn_iam_stmts,avg_fn_iam_stmts,fn_roles_used,stmts_defined,actual_rules,actual_stmts,raw_stmt_dict\n')
            parsing_errors = {}
            conversion_errors = {}

            read_header = False
            all_repos = {}
            working_repos = {}
            projects = 0
            success = 0
            for line in csvfile:
                print(line.strip())
                if not read_header:
                    read_header = True
                    continue

                dirs = line.split('/')
                repo = f'{dirs[3]}/{dirs[4]}'
                if repo not in all_repos:
                    all_repos[repo] = 0
                all_repos[repo] += 1

                projects += 1
                files = [line.strip()]
                try:
                    sls_ag = SlsAttackGraph(files, None)
                except Exception as e:
                    if str(e) not in parsing_errors:
                        parsing_errors[str(e)] = 0
                    parsing_errors[str(e)] += 1
                    continue

                #definitions, definitions_raw = sls_ag.definitions, sls_ag.definitions_raw
                # Filter out empty files that have not been parsed successfully
                #definitions = {k: v for k, v in definitions.items() if v}
                #definitions_raw = {k: v for k, v in definitions_raw.items() if k in definitions.keys()}

                if len(sls_ag.attack_graphs) == 0:
                    continue

                ag = sls_ag.attack_graphs[0]
                ag.ParseConfig()
                if ag.yml_stats['error']:
                    e_msg = ag.yml_stats['error_msg']
                    if e_msg not in conversion_errors:
                        conversion_errors[e_msg] = 0
                    conversion_errors[e_msg] += 1
                    if 'sqs events notz' in e_msg:
                        logging.error(e_msg)
                        logging.error(ag.config)
                        logging.error(str(ag.yml_stats['trace']))
                        input('>')
                    continue
                else:
                    success += 1
                    if repo not in working_repos:
                        working_repos[repo] = 0
                    working_repos[repo] += 1


                out_path = '../../misc-scripts/data/new-results/{}-{}-{}.pl'.format(dirs[3], dirs[4], projects)
                with open(out_path, 'w') as outfile:
                    outfile.write('% Project repo: {}\n'.format(line))
                    outfile.write(template)

                    for fact in sorted(list(ag.facts)):
                        outfile.write('{}\n'.format(fact))
                

                ag.calc_stats()
                permission_file.write(
                    f"{out_path},{ag.yml_stats['global_iam_stmts']},"
                )
                mma = min_max_avg(ag.yml_stats['fn_iam_stmts'])
                permission_file.write(
                    f"{mma[0]},{mma[1]},{mma[2]},{ag.yml_stats['fn_roles_used']},"
                )
                permission_file.write(    
                    f"{count_stmts_defined(ag.yml_stats['stmt_stats'])},"
                )
                permission_file.write(
                    f"{ag.yml_stats['actual_rules_written']},{ag.yml_stats['actual_stmts_written']},"
                )
                permission_file.write(
                    f"'{json.dumps(ag.yml_stats['stmt_stats'])}'\n"
                )

            print('{}/{} parsed successfully across {}/{} repos'.format(success, projects, len(working_repos), len(all_repos)))
            print('Parsing Errors')
            for key, value in sorted(parsing_errors.items(), key=lambda item: item[1]):
                print('\t{} : {}'.format(key, value))
            print('Conversion Errors')
            for key, value in sorted(conversion_errors.items(), key=lambda item: item[1]):
                print('\t{} : {}'.format(key, value))

    return None

def count_stmts_defined(stmts_dict):
    total = 0
    processed = set()

    for key, value in stmts_dict.items():
        if value['name'] == 'global' and value['type'] == 'global' and 'global' not in processed:
            total += value['stmt_count']
            processed.add('global')
        elif value['type'] == 'function_stmts':
            total += value['stmt_count']
        elif value['type'] == 'function_role' and value['name'] not in processed:
            total += value['stmt_count']
            processed.add(value['name'])
    
    return total


def min_max_avg(obj):
    vals = obj.values()

    if len(vals) == 0:
        return 0, 0, 0

    return min(vals), max(vals), sum(vals)/len(vals)


def add_parser_args(parser: ArgumentParser) -> None:
    parser.add('-v', '--version',
               help='version', action='version', version=version)
    parser.add('-d', '--directory', action='append',
               help='IaC root directory (can not be used together with --file).')
    parser.add('-f', '--file', action='append',
               help='IaC file(can not be used together with --directory)')
    parser.add('--skip-path', action='append',
               help='Path (file or directory) to skip, using regular expression logic, relative to current '
                    'working directory. Word boundaries are not implicit; i.e., specifying "dir1" will skip any '
                    'directory or subdirectory named "dir1". Ignored with -f. Can be specified multiple times.')
    parser.add('-o', '--output', action='append', choices=OUTPUT_CHOICES,
               default=None,
               help='Report output format. Add multiple outputs by using the flag multiple times (-o sarif -o cli)')
    parser.add('--quiet', action='store_true',
               default=False,
               help='in case of CLI output, display only failed checks')
    parser.add('--var-file', action='append',
               help='Variable files to load in addition to the default files (see '
                    'https://www.terraform.io/docs/language/values/variables.html#variable-definitions-tfvars-files).'
                    'Currently only supported for source Terraform (.tf file), and Helm chart scans.'
                    'Requires using --directory, not --file.')
    parser.add('--evaluate-variables',
               help="evaluate the values of variables and locals",
               default=True)
    parser.add('-l', '--list', action='append',
                help='List of YML files to process')


if __name__ == '__main__':
    sys.exit(run())
