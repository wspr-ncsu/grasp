#!/usr/bin/env python

import os
import traceback
import yaml
from pathlib import Path

total_count = 0

def parse_provider(config, permissions):
    if 'provider' not in config:
        return

    provider = config['provider']

    if not isinstance(provider, dict):
        return

    if 'iam' in provider:
        if 'role' in provider['iam']:
            role = provider['iam']['role']

            if isinstance(role, str):
                return

            if isinstance(role, dict) and 'statements' in role:
                for stmt in role['statements']:
                    if isinstance(stmt, dict):
                        actions = stmt['Action']
                        if isinstance(actions, list):
                            for action in actions:
                                permissions.add(action)

            if 'managedPolicies' in role:
                managedPolicies = role['managedPolicies']
                if isinstance(managedPolicies, list):
                    for policy in managedPolicies:
                        permissions.add(policy)

    elif 'iamRoleStatements' in provider:
        stmts = provider['iamRoleStatements']
        if isinstance(stmts, list):
            for stmt in stmts:
                if isinstance(stmt, dict):
                    actions = stmt['Action']
                    if isinstance(actions, list):
                        for action in actions:
                            permissions.add(action)

def parse_functions(config, permissions):
    if 'functions' not in config:
        return

    functions = config['functions']

    if isinstance(functions, dict):
        for function_name, function in functions.items():
            if isinstance(function, dict):
                if 'iamRoleStatements' in function:
                    stmts = function['iamRoleStatements']
                    if isinstance(stmts, list):
                        for stmt in stmts:
                            if isinstance(stmt, dict):
                                actions = stmt['Action']
                                if isinstance(actions, list):
                                    for action in actions:
                                        permissions.add(action)
    elif isinstance(functions, list):
        # TODO resolve additional YML
        pass

def parse_roles(config, permissions):
    if 'resources' not in config:
        return

    resources = config['resources']
    if not isinstance(resources, dict):
        return

    if 'Resources' not in resources:
        return

    resources = resources['Resources']
    if not isinstance(resources, dict):
        return

    for resource_name, resource in resources.items():
        if not isinstance(resource, dict):
            continue

        if 'Type' not in resource:
            continue

        if resource['Type'] == 'AWS::IAM::Role':
            if 'Policies' in resource:
                for policy in resource['Policies']:
                    try:
                        stmts = policy['PolicyDocument']['Statement']
                        if isinstance(stmts, list):
                            for stmt in stmts:
                                actions = stmt['Action']
                                if isinstance(actions, list):
                                    for action in actions:
                                        permissions.add(action)
                    except KeyError:
                        pass


def process_project(project_path):
    global total_count
    permissions = set()

    for path in Path(project_path).rglob('*serverless*.y*ml'):
        total_count += 1

        with open(path, 'r') as file:
            try:
                config = yaml.safe_load(file)
                if not isinstance(config, dict):
                    continue

                parse_provider(config, permissions)
                parse_functions(config, permissions)
                parse_roles(config, permissions)
            except yaml.constructor.ConstructorError:
                continue
            except yaml.scanner.ScannerError:
                continue
            except yaml.composer.ComposerError:
                continue
            except yaml.parser.ParserError:
                continue
            except Exception as e:
                print(traceback.format_exc())
                continue

    return permissions

if __name__ == '__main__':
    users = [f.path for f in os.scandir('/data/serverless-dataset') if f.is_dir()]
    projects = []
    for user in users:
        projects += [f.path for f in os.scandir(user) if f.is_dir()]

    print('{} Projects found.'.format(len(projects)))

    permissions = {}

    for project in projects:
        project_permissions = process_project(project)

        for permission in project_permissions:
            if permission not in permissions:
                permissions[permission] = 0

            permissions[permission] += 1

    print('{} candidate ymls found.'.format(total_count))

    for key, value in sorted(permissions.items(), key=lambda item: item[1]):
        print('{}: {}'.format(key, value))
