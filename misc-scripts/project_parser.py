#!/usr/bin/env python

#>= v2.24.0 uses provider.iam.role.statements
#< v2.24.0 uses provider.iamRoleStatements

import csv
import os
import yaml

from pathlib import Path

total_count = 0

def count_lines(file):
    lines = 0
    with open(file) as infile:
        for line in infile:
            lines += 1

    return lines

def allows_invoke(stmts):
    for stmt in stmts:
        for action in stmt['Action']:
            if 'InvokeFunction' in action or 'InvokeAsync' in action:
                return True

            if action == '*':
                return True

            if action[-1] == '*' and action[:-1] in 'lambda:Invoke':
                return True
    return False

def get_policy_version(project, config):
    policies = {'global': None, 'function': None}

    # Check for global policies
    try:
        current = config['provider']['iam']['role']['statements']
        policies['global'] = 'Latest'
    except KeyError:
        try:
            legacy = config['provider']['iamRoleStatements']
            policies['global'] = 'Legacy'
        except KeyError:
            policies['global'] = 'None'

    # Check for Function policies
    try:
        functions = config['functions']
        if isinstance(functions, dict):
            hasRole = False
            hasPlugin = False
            for function_name, function in functions.items():
                try:
                    roles = function['role']
                    hasRole = True
                except KeyError:
                    try:
                        iamStatements = function['iamRoleStatements']
                        hasPlugin = True
                    except KeyError:
                        pass

            if hasRole and hasPlugin:
                policies['function'] = 'Role and iamStatements'
            elif hasRole:
                policies['function'] = 'Default Role-Based'
            elif hasPlugin:
                policies['function'] = 'iamStatements Plugin'
    except KeyError:
        # TODO should I handle this
        pass

    if policies['function'] is None:
        policies['function'] = 'None'

    project['Global Policy Version'] = policies['global']
    project['Function Policy Version'] = policies['function']

def get_function_count(project, config):
    try: 
        functions = config['functions']
        if functions and isinstance(functions, dict):
            project['Functions'] += len(functions)
        else:
            project['Functions Defined Externally'] += 1
    except KeyError:
        # TODO: how should I handle this
        pass

def get_plugin_count(project, config):
    try:
        plugins = config['plugins']
        if plugins and isinstance(plugins, list):
            project['Plugins'] += len(plugins)
        else:
            # TODO how should I handle this
            pass
    except KeyError:
        # TODO hwo should I handle this
        pass

def get_package_count(project, config):
    try:
        packages = config['packages']['include']
        if packages and isinstance(packages, list):
            project['Packages'] += len(packages)
        else: 
            # TODO how should I handle this
            pass
    except KeyError:
        # TODO how should I handle this
        pass

def get_resource_count(project, config):
    try:
        resources = config['Resources']
        project['Resources'] = len(resources)
    except KeyError:
        pass

def get_iam_statement_count(project, config):
    try:
        role = config['provider']['iam']['role']
        project['YMLs with Global Policies'] += 1

        if isinstance(role, str):
            project['Number of Global Roles'] += 1
        elif isinstance(role, dict):
            if 'statements' in role:
                statements = role['statements']
                if isinstance(statements, list):
                    project['Number of Global Statements'] += len(statements)
                    if allows_invoke(statements):
                        project['Allows Invoke'] = True
                        project['Global Invoke'] = True
    except KeyError:
        try:
            statements = config['provider']['iamRoleStatements']
            project['YMLs with Global Policies'] += 1

            if isinstance(statements, list):
                project['Number of Global Statements'] += len(statements)
                if allows_invoke(statements):
                    project['Allows Invoke'] = True
                    project['Global Invoke'] = True
        except KeyError:
            # There are no global policies
            pass

    try:
        functions = config['functions']
        
        if isinstance(functions, dict):
            for function_name, function in functions.items():
                if 'role' in function:
                    project['Functions with Policies'] += 1
                    project['Number of Functions with Roles'] += 1
                    # TODO check if roles enable allow invoke
                elif 'iamRoleStatements' in function:
                    project['Functions with Policies'] += 1
                    statements = function['iamRoleStatements']
                    if isinstance(statements, list):
                        project['Number of Function Statements'] += len(statements)
                        if allows_invoke(statements):
                            project['Allows Invoke'] = True
                    
    except KeyError:
        pass


def get_provider_names(project, config):
    try:
        provider = config['provider']['name']
        project['Providers'].add(provider)
    except KeyError:
        project['Providers'].add('aws')


def process_project(project_path):
    global total_count

    project = {}

    project['YMLs'] = 0
    project['Invalid YMLs'] = 0
    project['Name'] = project_path
    project['Functions'] = 0
    project['Plugins'] = 0
    project['Resources'] = 0
    project['Packages'] = 0
    project['YML LOC'] = 0
    project['Global Policy Version'] = 'Unknown'
    project['Function Policy Version'] = 'Unknown'
    project['Functions Defined Externally'] = 0
    project['Resources'] = 0
    project['YMLs with Global Policies'] = 0
    project['Number of Global Statements'] = 0
    project['Number of Global Roles'] = 0
    project['Functions with Policies'] = 0 
    project['Number of Functions with Roles'] = 0
    project['Number of Function Statements'] = 0
    project['Allows Invoke'] = False
    project['Global Invoke'] = False
    project['Providers'] = set()

    last = 0
    for path in Path(project_path).rglob('*serverless*.y*ml'):
        total_count += 1
        project['YMLs'] += 1


        with open(path, 'r') as file:
            try:
                config = yaml.safe_load(file)

                get_function_count(project, config)
                get_plugin_count(project, config)
                get_package_count(project, config)
                get_policy_version(project, config)
                get_resource_count(project, config)
                get_iam_statement_count(project, config)
                get_provider_names(project, config)
                project['YML LOC'] += count_lines(path)

                current = project['Number of Global Statements'] + \
                    project['Number of Global Roles'] + \
                    project['Number of Function Statements'] + \
                    project['Number of Functions with Roles']
                if  current > last:
                    print(path)
                    last = current
            except:
                project['Invalid YMLs'] += 1

    return project

if __name__ == '__main__':
    users = [f.path for f in os.scandir('/data/serverless-dataset') if f.is_dir()]
    projects = []
    for user in users:
        projects += [f.path for f in os.scandir(user) if f.is_dir()]

    print('{} Projects found.'.format(len(projects)))

    parsed_results = []
    providers = {}
    for project in projects:
        parsed_results.append(process_project(project))
        for provider in parsed_results[-1]['Providers']:
            if provider not in providers:
                providers[provider] = 0
            providers[provider] += 1



    print('{} candidate ymls found.'.format(total_count))
    print(providers)


    with open('data.csv', 'w', newline='') as outFile:
        writer = csv.writer(outFile)
        writer.writerow([
            'Name',
            'YMLs',
            'Invalid YMLs',
            'Functions',
            'Plugins',
            'Packages',
            'Global Policy Version',
            'Function Policy Version',
            'YML LOC',
            'Functions Defined Externally',
            'Resources',
            'YMLs with Global Policies',
            'Number of Global Statements',
            'Number of Global Roles',
            'Functions with Policies',
            'Number of Functions with Roles',
            'Number of Function Statements',
            'Allows Invoke',
            'Global Invoke', 
            'AWS Lambda Project'
        ])
        for result in parsed_results:
            writer.writerow([
                result['Name'],
                result['YMLs'],
                result['Invalid YMLs'],
                result['Functions'],
                result['Plugins'],
                result['Packages'],
                result['Global Policy Version'],
                result['Function Policy Version'],
                result['YML LOC'],
                result['Functions Defined Externally'],
                result['Resources'],
                result['YMLs with Global Policies'],
                result['Number of Global Statements'],
                result['Number of Global Roles'],
                result['Functions with Policies'],
                result['Number of Functions with Roles'],
                result['Number of Function Statements'],
                result['Allows Invoke'],
                result['Global Invoke'],
                'aws' in result['Providers']
            ])
