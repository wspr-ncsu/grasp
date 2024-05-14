import logging
import resource
from serverless.parsers.parser import parse, process_intrinsic
from serverless.parsers.ServerlessManagedPolicies import managed_policy
import traceback
import json
DEFAULT_ROLE = 'IamRoleLambdaExecution'

class SlsAttackGraph(object):

    def __init__(self, files, filepath_fn):
        self.files = files
        self.filepath_fn = filepath_fn
        self.definitions, self.definitions_raw = SlsAttackGraph.get_file_definitions(files, filepath_fn)

        self.attack_graphs = []

        for path, definition in self.definitions.items():
            self.attack_graphs.append(SlsApplication(path, definition))

    def get_file_definitions(files, filepath_fn=None):
        definitions = {}
        definitions_raw = {}

        for file in files:
            result = parse(file)
            if result:
                path = filepath_fn(file) if filepath_fn else file
                definitions[path], definitions_raw[path] = result

        return definitions, definitions_raw


class SlsApplication(object):

    def __init__(self, path, config):
        self.path = path
        self.config = config
        self.roles = {}
        self.roles[DEFAULT_ROLE] = []
        self.project_resources = set()
        self.bucket_policies = []
        self.fn_names = set()
        self.fn_permissions = {}
        self.events = {}
        self.facts = set()
        self.yml_stats = {'error': False}
        self.yml_stats['yml_file'] = path
        self.yml_stats['stmt_stats'] = {}
        self.iam_stmt_count = 0  # for counting explicit statements on functions (not roles or default)
        self.iam_rule_count = 0  # for counting explicit rules on functions (not roles or default)
        self.repair_config()

    # Try to recover situations where the yml defines functions and resources as lists of files
    # this should ideally be done in the parser but using a quick hack here instead.
    def repair_config(self):
        try:
            resources = self.config['resources']
            if isinstance(resources, list):
                tmp = {}
                for item in resources:
                    if isinstance(item, dict):
                        if 'Resources' in item:
                            tmp.update(item['Resources'])
                    else:
                        pass
                self.config['resources'] = {'Resources': tmp }
        except Exception as e:
            pass

        try:
            Functions = self.config['functions']
            if isinstance(Functions, list):
                functions = {}
                for item in Functions:
                    functions.update(item)
                self.config['functions'] = functions
        except:
            pass

    def ParseConfig(self):
        try:
            self.roles[DEFAULT_ROLE].extend(self.process_default_role())
            self.process_default_role()
            self.process_resources()
            self.process_functions()
            self.project_resources.update(self.extract_resources_from_rules())
            self.GenerateFacts()
        except Exception as e:
            self.yml_stats['error'] = True
            self.yml_stats['error_msg'] = str(e)
            self.yml_stats['trace'] = str(traceback.format_exc())
    
    def extract_resources_from_rules(self):
        retval = set()
        for _, role_rules in self.roles.items():
            retval.update(self.extract_resources_from_rule_list(role_rules))
        
        for _, fn_rules in self.fn_permissions.items():
            retval.update(self.extract_resources_from_rule_list(fn_rules))

        
        return retval

    def extract_resources_from_rule_list(self, rule_list):
        retval = set()
        for rule in rule_list:
            if 'Resource' not in rule:
                raise ValueError('Invalid Yml. Statement missing resource')
            
            if isinstance(rule['Resource'], str):
                resource_tuple = self._resource_extractor_helper(rule['Resource'])
                if resource_tuple:
                    retval.add(resource_tuple)
            elif isinstance(rule['Resource'], list):
                for res_name in rule['Resource']:
                    resource_tuple = self._resource_extractor_helper(res_name)
                    if resource_tuple:
                        retval.add(resource_tuple)
        return retval
    
    def _resource_extractor_helper(self, res_name):
        if 'arn:' in res_name:
            parsed_arn = SlsApplication._parse_arn(res_name)
            if parsed_arn['service'].lower() == 's3' and '*' not in parsed_arn['resource_type']:
                return (parsed_arn['service'], parsed_arn['resource_type'])
            elif '*' not in parsed_arn['resource']:
                return (parsed_arn['service'], parsed_arn['resource'])
        elif '*' in res_name:
            pass  # skip wildcard resources
        else:
            # The preprocessor will replace Ref with just the name (no arn:)
            # we can skip this because the resource has to be listed in Resources
            # and is added later
            pass

        return None



    # Extracts a list of role statements for the global iam policy that is used as default.
    def process_default_role(self):
        provider = None
        resources = None
        try:
            provider = self.config['provider']
        except KeyError:
            return []

        try:
            resources = self.config['resources']['Resources']
        except KeyError:
            pass

        if 'iam' in provider and 'role' in provider['iam']:
            # Newer provider.iam.role format
            role = provider['iam']['role']
            if isinstance(role, str):
                if role.startswith('arn:'):
                    parsed_res = SlsApplication._parse_arn(role)
                    if parsed_res['resource_type'] == 'policy':
                        arn_name = parsed_res['resource']
                        if arn_name == 'service-role': # service-role/ACTUALNAME
                            arn_name = parsed_res['extra']
                        return managed_policy(arn_name)
                    elif parsed_res['resource_type'] == 'role':
                        raise TypeError('Role {} defined outside of serverless file.'.format(role))
                elif resources and role in resources:
                    return SlsApplication._parse_role_resource(role, resources[role])
            elif isinstance(role, dict):
                retval = []
                if 'managedPolicies' in role:
                    for policy in role['managedPolicies']:
                        parsed_res = SlsApplication._parse_arn(policy)
                        mp_name = parsed_res['resource']
                        if mp_name == 'service-role':
                            mp_name = parsed_res['extra']
                        retval.extend(managed_policy(mp_name))
                
                if 'permissionsBoundary' in role:
                    raise NotImplementedError('PermissionBoundaries not implemented')

                if 'statements' in role:
                    retval.extend(role['statements'])
                return retval
        elif 'role' in provider:
            role = provider['role']
            if role.startswith('arn:'):
                parsed_res = SlsApplication._parse_arn(role)
                if parsed_res['resource_type'] == 'policy':
                    arn_name = parsed_res['resource']
                    if arn_name == 'service-role':
                        arn_name = parsed_res['extra']
                    return managed_policy(arn_name)
                elif parsed_res['resource_type'] == 'role':
                    raise TypeError('Role {} defined outside of serverless file.'.format(role))
            elif resources and role in resources:
                return SlsApplication._parse_role_resource(role, resources[role])
        elif 'iamRoleStatements' in provider:
            # Legacy permission format
            return provider['iamRoleStatements']
        
        return []


    # Parses the important values from the config['resources']['Resources'] section of a serverless config
    def process_resources(self):
        for res_name, res_value in self.Resources():
            if 'Type' not in res_value:
                continue
            
            res_type = res_value['Type']
            if  res_type == 'AWS::IAM::Role':
                if res_name not in self.roles:
                    self.roles[res_name] = []
                self.roles[res_name].extend(SlsApplication._parse_role_resource(res_name, res_value))
                    
            # Resources
            elif res_type == 'AWS::DynamoDB::Table':
                try:
                    self.project_resources.add(('dynamodb', res_value['Properties']['TableName']))
                except KeyError:
                    # Not actually sure the proper way to handle this. Pretty sure
                    # the files that do not have a tablename defined the table
                    # outside of the yml.
                    self.project_resources.add(('dynamodb', res_name))
            elif res_type == 'AWS::S3::Bucket':
                try:
                    self.project_resources.add(('s3', res_value['Properties']['BucketName']))

                    if 'AccessControl' in res_value['Properties']:
                        # https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-overview.html#canned-acl
                        # functions must be given access via statements
                        # policies define which users (usually public) can access
                        
                        ac_policy = res_value['Properties']['AccessControl']
                        if 'PublicRead' in ac_policy:
                            self.bucket_policies.append(
                                {
                                    'Effect': 'Allow',
                                    'Principal': '*',
                                    'Action': ['s3:GetObject'],
                                    'Resource': res_value['Properties']['BucketName']
                                }
                            )
                        if ac_policy == 'PublicReadWrite':
                            self.bucket_policies.append(
                                {
                                    'Effect': 'Allow',
                                    'Principal': '*',
                                    'Action': ['s3:PutObject'],
                                    'Resource': res_value['Properties']['BucketName']
                                }
                            )
                except KeyError:
                    pass
            elif res_type == 'AWS::SNS::Topic':
                try:
                    self.project_resources.add(('sns', res_value['Properties']['TopicName']))
                except KeyError:
                    # Can't really do much about this
                    pass
            elif res_type == 'AWS::SQS::Queue':
                try:
                    self.project_resources.add(('sqs', res_value['Properties']['QueueName']))
                except KeyError:
                    # Can't really do much about this
                    pass
            elif res_type == 'AWS::Kinesis::Stream':
                try:
                    self.project_resources.add(('kinesis', res_value['Properties']['Name']))
                except KeyError:
                    # Can't really do much about this
                    pass
            elif res_type == 'AWS::Events::EventBus':
                try:
                    self.project_resources.add(('event', res_value['Properties']['Name']))
                except KeyError:
                    # Can't really do much about this
                    pass

            # Policies 
            elif res_type == 'AWS::S3::BucketPolicy':
                try:
                    # Ignore Properties.Bucket since pretty sure the ARN must be
                    # given in each policy statement as Resource
                    self.bucket_policies.extend(res_value['Properties']['PolicyDocument']['Statement'])
                except KeyError:
                    pass
            elif res_type == 'AWS::IAM::Policy':
                try:
                    stmts = res_value['Properties']['PolicyDocument']['Statement']

                    policy_roles = res_value['Properties']['Roles']
                    if isinstance(policy_roles, list):
                        for role in policy_roles:
                            if isinstance(role, dict):
                                role_name = role['Ref']
                            elif isinstance(role, str):
                                role_name = role

                            if role_name not in self.roles:
                                self.roles[role_name] = []
                            self.roles[role_name].extend(stmts)
                    elif isinstance(policy_roles, str):
                        if policy_roles not in self.roles:
                            self.roles[policy_roles] = []

                        self.roles[policy_roles].extend(stmts)
                    elif isinstance(policy_roles, dict):
                        role_name = policy_roles['Ref']
                        if role_name not in self.roles:
                            self.roles[role_name] = []

                        self.roles[role_name].extend(stmts)
                except KeyError:
                    pass

            # SKIP the following
            elif res_type.startswith('AWS::ApiGateway::'):
                pass
            elif res_type == 'AWS::Logs::LogGroup':
                pass
            elif res_type.startswith('AWS::ECS::'):
                pass
            elif res_type.startswith('AWS::Glue::'):
                pass
            elif res_type == 'AWS::Lambda::Function':
                pass
            elif res_type == 'AWS::SES::Template':
                pass
            elif res_type == 'AWS::EC2::SecurityGroup':
                pass # don't hand since it's EC2 not lambda
            elif res_type == 'AWS::CloudWatch::Alarm':
                pass
            elif res_type == 'AWS::SSM::Parameter':
                pass
            else:
                raise NotImplementedError('{} not handled'.format(res_type))

    # Parses the important values from the config['functions'] section of a serverless config
    def process_functions(self):
        for fn_name, fn_value in self.Functions():
            self.fn_names.add(fn_name)
            # Process events
            if 'events' in fn_value:
                fn_events = fn_value['events']
                if isinstance(fn_events, list):
                    self.events[fn_name] = Events(fn_name, fn_events)


            # Determine the IAM policy for the function
            if 'role' in fn_value:
                role_name = fn_value['role']
                if role_name in self.roles:
                    self.fn_permissions[fn_name] = self.roles[role_name]
                    self.yml_stats['stmt_stats'][fn_name] = {
                        'type': 'function_role',
                        'name': role_name,
                        'rule_count': len(self.roles[role_name]),
                        'stmt_count': SlsApplication._num_stmts_generated(self.roles[role_name])
                    }
                else:
                    # The role is defined outside of the YML
                    self.fn_permissions[fn_name] = []
            elif 'iamRoleStatements' in fn_value:
                self.fn_permissions[fn_name] = fn_value['iamRoleStatements']
                self.yml_stats['stmt_stats'][fn_name] = {
                    'type': 'function_stmts',
                    'name': fn_name,
                    'rule_count': len(fn_value['iamRoleStatements']),
                    'stmt_count': SlsApplication._num_stmts_generated(fn_value['iamRoleStatements'])
                }
                self.iam_rule_count += self.yml_stats['stmt_stats'][fn_name]['rule_count']
                self.iam_stmt_count += self.yml_stats['stmt_stats'][fn_name]['stmt_count']
            else:
                self.fn_permissions[fn_name] = self.roles[DEFAULT_ROLE]
                self.yml_stats['stmt_stats'][fn_name] = {
                    'type': 'global',
                    'name': 'global',
                    'rule_count': len(self.roles[DEFAULT_ROLE]),
                    'stmt_count': SlsApplication._num_stmts_generated(self.roles[DEFAULT_ROLE]) 
                }

    # Generator for all functions in config['functions']
    def Functions(self):
        try:
            functions = self.config['functions']
            for fn_name, fn_value in functions.items():
                if fn_name in ('__startline__', '__endline__'):
                    continue
                yield fn_name, fn_value
        except:
            return

    # Generator for all resources in config['resources']['Resources']
    def Resources(self):
        try:
            resources = self.config['resources']['Resources']
            for res_name, res_value in resources.items():
                if res_name in ('__startline__', '__endline__'):
                    continue
                yield res_name, res_value
        except:
            return
    
    # Rules can define multiple actions applied on multiple resources, get a count of the number
    # of actual statements that are generated for a rule. e.g., Allow "s3:A, s3:B" on "bucket1,
    # bucket2" would generate 4 statements for the single rule. s3:A on bucket1, s3:A on bucket2,
    # s3:B on bucket1, s3:B on bucket2
    @staticmethod
    def _num_stmts_generated(rules):
        total_stmts = 0

        for rule in rules:
            try:
                if isinstance(rule['Action'], str):
                    actions = 1
                elif isinstance(rule['Action'], list):
                    actions = len(rule['Action'])

                if isinstance(rule['Resource'], str):
                    resources = 1
                elif isinstance(rule['Resource'], list):
                    resources = len(rule['Resource'])

                total_stmts += actions * resources
            except KeyError:
                continue

        return total_stmts

    # Convert a role resource into a list of statements
    @staticmethod
    def _parse_role_resource(res_name, res):
        retval = []

        if res['Type'] != 'AWS::IAM::Role':
            raise TypeError('Resource must be AWS::IAM::Role')

        try:
            for policy in res['Properties']['ManagedPolicyArns']:
                # Translate a managed_policy into a list of statements
                parsed_res = SlsApplication._parse_arn(policy)
                arn_name = parsed_res['resource']
                if arn_name == 'service-role':
                    arn_name = parsed_res['extra']
                retval.extend(managed_policy(arn_name))
        except KeyError:
            pass

        try:
            for policy in res['Properties']['Policies']:
                statements = policy['PolicyDocument']['Statement']
                retval.extend(statements)
        except KeyError:
            pass

        try:
            assumeRoleDocument = res['Properties']['AssumedRolePolicyDocument']
            # TODO: do I need to handle this in a special way?
            # this defines which services can assume this role, but we can just
            # assume that the services this role is applied to in the yaml is
            # valid.
        except KeyError:
            pass

        return retval

    # Creates all the resource, function, permission, event, etc. prolog facts for a given config
    def GenerateFacts(self):
        # Add all the event triggers, including publicly accessible functions
        for _, event in self.events.items():
            self.facts.update(event.facts)

        # function(fn_name, public_facing).
        # if function(name, true). is not already in the fact set from event parsing above then
        # the function is not publicly accessible so add function(name, false).
        for fn_name in self.fn_names:
            if "function('{}', true).".format(fn_name) not in self.facts:
                self.facts.add("function('{}', false).".format(fn_name))

        # Generate facts for resources to update their visibility
        resource_definitions = {}
        for res_type, res_name in self.project_resources:
            if res_type == 'lambda':
                continue
            res_key = '{}:{}'.format(res_type.lower(), res_name)
            resource_definitions[res_key] = {}
            resource_definitions[res_key]['type'] = res_type.lower()
            resource_definitions[res_key]['name'] = res_name
            resource_definitions[res_key]['public_read'] = 'false'
            resource_definitions[res_key]['public_write'] = 'false'

        # Update public read/write for s3 buckets
        SlsApplication._parse_bucket_policies(self.bucket_policies, resource_definitions)

        # Parse bucket policies into facts
        for _, res in resource_definitions.items():
            self.facts.add("resource('{}', '{}', '{}', '{}').".format(
                res['type'], res['name'], res['public_read'], res['public_write'])
            )

        # Get function permission facts
        self.facts.update(self.function_permissions())

    def calc_stats(self):
        # Calculate permission stats
        self.yml_stats['global_iam_stmts'] = len(self.roles[DEFAULT_ROLE])
        self.yml_stats['fn_iam_stmts'] = {}
        self.yml_stats['fn_roles_used'] = 0

        for fn_name, fn_value in self.Functions():
            if 'role' in fn_value:
                self.yml_stats['fn_roles_used'] += 1

            if 'iamRoleStatements' in fn_value:
                self.yml_stats['fn_iam_stmts'][fn_name] = len(fn_value['iamRoleStatements'])

        # latest calculation I don't remember what the above does right now.
        # calculate the number of rules actually written in roles + default + explicit function
        # statements. already counted statements and rules in process_functions()
        for role in self.roles:
            self.iam_rule_count += len(self.roles[role])
            self.iam_stmt_count += SlsApplication._num_stmts_generated(self.roles[role])
        self.yml_stats['actual_rules_written'] = self.iam_rule_count
        self.yml_stats['actual_stmts_written'] = self.iam_stmt_count


    def function_permissions(self):
        permissions = set()

        for fn_name, stmt_list in self.fn_permissions.items():
            for stmt in stmt_list:
                if stmt['Effect'] != 'Allow':
                    continue

                actions = []
                action = stmt['Action']
                if isinstance(action, str):
                    actions.append(action)
                elif isinstance(action, list):
                    actions.extend(action)

                # if action is lambda: hand it differently

                targets = []
                resource = stmt['Resource']
                if isinstance(resource, str):
                    if 'arn:' in resource:
                        parsed_arn = SlsApplication._parse_arn(resource)
                        res_name = parsed_arn['resource']
                        targets.append(res_name)
                    else:
                        targets.append(resource)
                elif isinstance(resource, list):
                    for res in resource:
                        if 'arn:' in res:
                            parsed_arn = SlsApplication._parse_arn(res)
                            res_name = parsed_arn['resource']
                            targets.append(res_name)
                        else:
                            targets.append(res)

                for action in actions:
                    for target in targets:
                        permissions.add("permission('{}', '{}', '{}').".format(fn_name, action, target))
            
        return permissions


    # Loop through bucket policies to determine if buckets are publicly accessible
    # if so update the resource definition
    @staticmethod
    def _parse_bucket_policies(bucket_policies, resource_definitions):
        for bp in bucket_policies:
            if bp['Effect'] != 'Allow':
                continue

            actions = []
            if isinstance(bp['Action'], list):
                for action in bp['Action']:
                    if action[-1] == '*':
                        if 's3:GetObject'.startswith(action[:-1]):
                            actions.append('s3:GetObject')
                        if 's3:PutObject'.startswith(action[:-1]):
                            actions.append('s3:PutObject')
                    else:
                        actions.append(action)
            elif isinstance(bp['Action'], str):
                action = bp['Action']
                if action[-1] == '*':
                    if 's3:GetObject'.startswith(action[:-1]):
                        actions.append('s3:GetObject')
                    if 's3:PutObject'.startswith(action[:-1]):
                        actions.append('s3:PutObject')
                else:
                    actions.append(action)

            public_principal = False
            principal = bp['Principal']
            if isinstance(principal, str) and principal == '*':
                public_principal = True
            elif isinstance(principal, list) and '*' in principal:
                public_principal = True

            if isinstance(bp['Resource'], str):
                bucket = bp['Resource']
                if 'arn:' in bucket:
                    bucket = SlsApplication._parse_arn(bucket)['resource_type']
                SlsApplication._update_bucket_resource(resource_definitions, bucket, public_principal, actions)
            elif isinstance(bp['Resource'], list):
                for bucket_name in bp['Resource']:
                    bucket = bucket_name
                    if 'arn:' in bucket:
                        bucket = SlsApplication._parse_arn(bucket)['resource_type']
                    SlsApplication._update_bucket_resource(resource_definitions, bucket, public_principal, actions)

    @staticmethod
    def _update_bucket_resource(resource_definitions, bucket, public_principal, actions):
        if not public_principal:
            return

        res_key = 's3:{}'.format(bucket)
        if res_key not in resource_definitions:
            resource_definitions[res_key] = {}
            resource_definitions[res_key]['type'] = 's3'
            resource_definitions[res_key]['name'] = bucket
            resource_definitions[res_key]['public_read'] = 'false' 
            resource_definitions[res_key]['public_write'] = 'false' 

        if 's3:GetObject' in actions:
            resource_definitions[res_key]['public_read'] = 'true'
        if 's3:PutObject' in actions:
            resource_definitions[res_key]['public_write'] = 'true'


    # Converts an arn string into the individual components. Accounts for arn strings that
    # contain unresolved variables
    @staticmethod
    def _parse_arn(arn_string):
        parts = []
        open_brackets = 0
        part_start = 0

        for idx, char in enumerate(arn_string):
            if char in [':', '/'] and open_brackets == 0 and len(parts) < 6:
                parts.append(arn_string[part_start:idx])
                part_start = idx + 1
            elif char == '{':
                open_brackets += 1
            elif char == '}':
                open_brackets -= 1
        parts.append(arn_string[part_start:])

        if parts[-1] == '*' and len(parts) < 6:
            while len(parts) < 6:
                parts.append('*')
        result = {}
        result['arn'] = parts[0]
        result['partition'] = parts[1]
        result['service'] = parts[2]
        result['region'] = parts[3]
        result['account'] = parts[4]
        if len(parts) == 6:
            result['resource'] = parts[5]
            result['resource_type'] = None
        else:
            splitted = parts[6].split('/', 1)
            result['resource'] = splitted[0]
            result['resource_type'] = parts[5]
            if len(splitted) > 1:
                result['extra'] = splitted[1]

        return result


# Helper class that represents a function's event triggers
class Events(object):
    def __init__(self, fn_name, event_list):
        self.fn_name = fn_name
        self.events = event_list
        self.facts = set()

        self.generate_facts()

    # Generator that loops through all event triggers
    def Events(self):
        for event in self.events:
            if isinstance(event, dict):
                # There should only be a single key here, which is the event type/name
                for event_type in event:
                    if event_type in ['__startline__', '__endline__']:
                        continue
                    yield self.fn_name, event_type, event[event_type]

    # Generate SWI prolog facts for all event triggers
    def generate_facts(self):
        for fn_name, event_type, event_properties in self.Events():
            self.facts.update(Events.event_fact(fn_name, event_type, event_properties))

    # Takes a single event config and outputs a fact based on the config
    def event_fact(fn_name, event_type, event_properties):
        event_type = event_type.lower()
    
        # HTTP methods or URL do not matter as it is accessible regardless
        if event_type == 'http' or event_type == 'httpapi' or event_type == 'https':
            return ["function('{}', true).".format(fn_name)]

        # enables an alexaskill to invoke a function
        elif event_type == 'alexaskill':
            if isinstance(event_properties, dict):
                if 'appId' in event_properties:
                    return ["event_alexaSkill('{}', '{}').".format(event_properties['appId'], fn_name)]
                else:
                    return []
            elif isinstance(event_properties, str):
                return ["event_alexaSkill('{}', '{}').".format(event_properties, fn_name)]
            else:
                return []
        
        # a write to an sns topic will invoke the given function
        # event_sns_msg(topic, triggered_function)
        elif event_type == 'sns':
            if isinstance(event_properties, dict):
                return ["event_sns_msg('{}', '{}').".format(event_properties['topicName'], fn_name)]
            elif isinstance(event_properties, str):
                # if a full arn is provided then it is defined outside of the policy. only care about topics
                if event_properties.startswith('arn:'):
                    topic = event_properties.split(':')[-1]
                else:
                    topic = event_properties

                return ["event_sns_msg('{}', '{}').".format(topic, fn_name)]
            else:
                raise ValueError('sns must be a string or dict.')

        # TODO handle sqs types
        elif event_type == 'sqss':
            if isinstance(event_properties, dict):
                return []

        # Websockets are like HTTP endpoints and always public
        # public(function_name)
        elif event_type == 'websocket':
            return ["function('{}', true).".format(fn_name)]

        # Not sure I can do anything with this without knowledge of the IoT setup
        # this basically says an IoT event can invoke lambda to do some kind of read
        # from a topic. But we will never know if this IoT rule can be triggered publicly
        # event_iot(triggered_function)
        elif event_type == 'iot':
            return ["event_iot('{}').".format(fn_name)]

        # event_stream_msg(stream_arn, triggered_function)
        elif event_type == 'stream':
            if isinstance(event_properties, dict):
                # TODO will type ever matter here?
                if 'arn' not in event_properties:
                    raise ValueError('no arn in stream event')
                if not isinstance(event_properties['arn'], str):
                    raise NotImplementedError('stream event arns must be string')

                return ["event_stream_msg('{}', '{}').".format(event_properties['arn'], fn_name)]
            elif isinstance(event_properties, str):
                return ["event_stream_msg('{}', '{}').".format(event_properties, fn_name)]

        # Since users can't influence schedules just return they are on a schedule
        # event_schedule(periodically_triggered_function)
        elif event_type == 'schedule':
            return ["event_schedule('{}').".format(fn_name)]

        # Since we don't know anything outside of lambda and cloudwatch doesn't generate lambda events
        # just notify user there are cloudwatch possibilites for invocation
        # event_cloudwatch(triggered_function)
        elif event_type == 'cloudwatchevent':
            return ["event_cloudwatch('{}').".format(fn_name)]


        # This is setup external to serverless and we don't know if the origin is public
        # event_cloudfront(triggered_function)
        elif event_type == 'cloudfront':
            return ["event_cloudfront('{}').".format(fn_name)]

        # Just show that a source can generate some kind of event to trigger a lambda
        # event_eventbridge(some_aws_source, triggered_function)
        elif event_type == 'eventbridge':
            if isinstance(event_properties, dict):
                if 'pattern' in event_properties:
                    pattern = event_properties['pattern']
                    sources = pattern['source']
                    retval = []
                    for source in sources:
                        retval.append("event_eventbridge('{}', '{}').".format(source, fn_name))

                    return retval
                else:
                    raise NotImplementedError('eventbridge without a pattern not implemented.')
            else:
                raise NotImplementedError('eventbridge only implemented as a dict')

        # event_s3(event, on_bucket, triggerd_function)
        elif event_type == 's3':
            event_triggers = []
            # I'm pretty sure this can't be a string and is a yml error
            # but just in case just granting all event permissions
            if isinstance(event_properties, str):
                name = event_properties
                event_triggers = [
                    's3:ObjectCreated:Put', 
                    's3:ObjectCreated:Post',
                    's3:ObjectCreated:Copy', 
                    's3:ObjectCreated:CompleteMultipartCopy',
                    's3:ObjectRemoved:Delete', 
                    's3:ObjectRemoved:DeleteMarkerCreated'
                ]
            elif isinstance(event_properties, dict):
                name = event_properties['bucket']
                event_value = event_properties['event']
                event_triggers.append(event_value)
            else:
                raise ValueError('s3 event not a string or dict')

            retval = []
            for trigger in event_triggers:
                retval.append("event_s3('{}', '{}', '{}').".format(trigger, name, fn_name))

            return retval

        raise NotImplementedError('{} events not handled'.format(event_type))