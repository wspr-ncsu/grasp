from ServerlessProjectv2 import ServerlessProject
from ServerlessManagedPolicies import managed_policy
import ServerlessWildcards
from pathlib import Path
import os
import re
import csv
import json
import traceback

unimplemented = set()

def process_event(fn_name, event_type, event_properties):
    global unimplemented
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
        if isinstance(event_properties, str):
            input('did this really happen>')
            name = event_properties
            event_triggers.extend(ServerlessWildcards.get_vals('s3:ObjectCreated:*', 'events'))
            event_triggers.extend(ServerlessWildcards.get_vals('s3:ObjectRemoved:*', 'events'))
        elif isinstance(event_properties, dict):
            name = event_properties['bucket']
            event_value = event_properties['event']
            if event_value[-1] == '*':
                event_triggers.extend(ServerlessWildcards.get_vals(event_value, 'events'))
            else:
                event_triggers.append(event_value)
        else:
            raise ValueError('s3 event must be string or dict')

        retval = []
        for trigger in event_triggers:
            retval.append("event_s3('{}', '{}', '{}').".format(trigger, name, fn_name))

        return retval

    unimplemented.add((event_type, 'event'))
    return []

# Parses custom IAM:ROLE resources and return list of statements
def parse_role_resource(res_name, res):
    retval = []

    if res['Type'] != 'AWS::IAM::Role':
        raise TypeError('Resource must be AWS::IAM::Role')

    try:
        for policy in res['Properties']['ManagedPolicyArns']:
            # Translate a managed_policy into a list of statements
            retval.extend(managed_policy(policy))
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


def get_provider_iam(root_config):
    retval = []

    provider_config = root_config['provider']
    resources = None
    try:
        resources = root_config['resources']['Resources']
    except KeyError:
        pass

    if 'iam' in provider_config:
        # Newer provider.iam.role format
        role = provider_config['iam']['role']
        if isinstance(role, str):
            if not role.startswith('arn:'):
                # Cannot handle roles defined outside of the config
                if resources and role in resources:
                    retval.extend(parse_role_resource(role, resources[role]))
                    return retval
        elif isinstance(role, dict):
            if 'managedPolicies' in role:
                for policy in role['managedPolicies']:
                    print(policy)
                    input('managedPolicies>')
            
            if 'permissionsBoundary' in role:
                raise NotImplementedError('PermissionBoundaries not implemented')

            if 'statements' in role:
                retval.extend(role['statements'])
            return retval
        else:
            return retval
    elif 'role' in provider_config:
        if not provider_config['role'].startswith('arn:'):
            # Cannot handle roles defined outside of the config
            if resources and provider_config['role'] in resources:
                role = provider_config['role']
                retval.extend(parse_role_resource(role, resources[role]))
                return retval
    elif 'iamRoleStatements' in provider_config:
        # Legacy permissions, no other interesting fields
        retval.extend(provider_config['iamRoleStatements'])
        return retval

    return retval

# Extracts explicitly defined resources (no wildcards)
def extract_resources_from_rules(rule_list):
    retval = set()
    for rule in rule_list:
        if isinstance(rule['Resource'], str):
            res_name = rule['Resource']
            if 'FAKE-' in res_name:
                # print('Unusable resource {}'.format(res_name))
                pass

            if 'arn:' in res_name:
                serv, resource = arn_to_service_and_resource(res_name)

                if '*' not in serv and '*' not in resource:
                    retval.add((serv, resource))
            elif '*' in res_name:
                continue # skip any wildcards that aren't an arn
            else:
                # print('Unusable resource {}'.format(res_name))
                pass
        elif isinstance(rule['Resource'], list):
            for res in rule['Resource']:
                if 'FAKE-' in res:
                    # print('Unusable resource {}'.format(res))
                    pass

                if 'arn:' in res:
                    serv, resource = arn_to_service_and_resource(res)
                        
                    if '*' not in serv and '*' not in resource:
                        retval.add((serv, resource))
                elif '*' in res:
                    continue # skip any wildcards that aren't an arn
                else:
                    # print('Unusable resource {}'.format(res))
                    pass
    
    return retval

# Update accessibility values for an s3 bucket
def update_bucket_resource(resource_definitions, bucket, public_principal, actions):
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

def parse_bucket_policies(bucket_policies, resource_definitions):
    for bp in bucket_policies:
        if bp['Effect'] != 'Allow':
            continue

        actions = []
        if isinstance(bp['Action'], list):
            for action in bp['Action']:
                if action[-1] == '*':
                    actions.extend(ServerlessWildcards.get_vals(action, 'permissions'))
                else:
                    actions.append(action)
        elif isinstance(bp['Action'], str):
            action = bp['Action']
            if action[-1] == '*':
                actions = ServerlessWildcards.get_vals(action, 'permissions')
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
                bucket = ServerlessProject.ParseArn(bucket)['resource_type']
            update_bucket_resource(resource_definitions, bucket, public_principal, actions)
        elif isinstance(bp['Resource'], list):
            for bucket_name in bp['Resource']:
                bucket = bucket_name
                if 'arn:' in bucket:
                    bucket = ServerlessProject.ParseArn(bucket)['resource_type']
                update_bucket_resource(resource_definitions, bucket, public_principal, actions)

def arn_to_service_and_resource(arn):
    parsed_service = ServerlessProject.ParseArn(arn)
    serv = parsed_service['service']
    resource = parsed_service['resource']
    #if parsed_service['resource_type']:
    #    resource = parsed_service['resource_type']
    #else:
    #    resource = parsed_service['resource']

    return serv, resource

# Build permission facts for a function given its permissions and set of all resources
def function_permissions(fn_names, fn_permissions, resource_definitions):
    permissions = set()

    for fn_name, stmt_list in fn_permissions.items():
        for stmt in stmt_list:
            if stmt['Effect'] != 'Allow':
                continue

            actions = []
            action = stmt['Action']
            if isinstance(action, str):
                if action[-1] == '*':
                    actions.extend(ServerlessWildcards.get_vals(action, 'permissions'))
                else:
                    actions.append(action)
            elif isinstance(action, list):
                for item in action:
                    if item[-1] == '*':
                        actions.extend(ServerlessWildcards.get_vals(item, 'permissions'))
                    else:
                        actions.append(item)

            # if action is lambda: handle it differently

            target_resources = []
            resource = stmt['Resource']
            if isinstance(resource, str):
                target_resources.extend(extract_statement_resources(resource, fn_names, resource_definitions))
            elif isinstance(resource, list):
                for res in resource:
                    target_resources.extend(extract_statement_resources(res, fn_names, resource_definitions))

            for action in actions:
                service = action.split(':')[0]

                for target in target_resources:
                    if target[0] == service and fn_name != target[1]:
                        permissions.add("permission('{}', '{}', '{}').".format(fn_name, action, target[1]))

    return permissions

# Return a list of resources affected by a statement by expanding wildcards
def extract_statement_resources(resource_string, fn_names, resource_definitions):
    target_resources = []
    resource = resource_string
    if resource == '*':
        for _, value in resource_definitions.items():
            target_resources.append((value['type'], value['name']))

        for fn_name in fn_names:
            target_resources.append(('lambda', fn_name))
    elif 'arn:' in resource:
        service, res = arn_to_service_and_resource(resource)
        if service == '*' and res != '*':
            for _, value in resource_definitions.items():
                if value['name'] == res:
                    target_resources.append((value['type'], value['name']))
            
            if res in fn_names:
                target_resources.append(('lambda', res))
        elif service != '*' and res == '*':
            if service == 'lambda':
                for fn_name in fn_names:
                    target_resources.append(fn_name)
            else:
                for _, value in resource_definitions.items():
                    if value['type'] == service.lower():
                        target_resources.append((value['type'], value['name']))
        elif service == '*' and res == '*':
            for _, value in resource_definitions.items():
                target_resources.append((value['type'], value['name']))
            for fn_name in fn_names:
                target_resources.append(fn_name)
        else:
            target_resources.append((service, res))
    
    return target_resources

# Given a list of statements count types of wildcards used
def count_wildcards(stmts):
    res = {}
    res['full_wc_res'] = 0
    res['full_wc_perm'] = 0
    res['partial_wc_res'] = 0
    res['partial_wc_perm'] = 0

    for stmt in stmts:
        action = stmt['Action']
        if isinstance(action, str):
            if action == '*':
                res['full_wc_perm'] += 1
            elif action[-1] == '*':
                res['partial_wc_perm'] += 1
        elif isinstance(action, list):
            for item in action:
                if item == '*':
                    res['full_wc_perm'] += 1
                elif item[-1] == '*':
                    res['partial_wc_perm'] += 1
        
        resource = stmt['Resource']
        if isinstance(resource, str):
            if resource == '*':
                res['full_wc_res'] += 1
            elif 'arn:' in resource:
                service, res_name = arn_to_service_and_resource(resource)
                if service == '*' and res_name != '*':
                    res['partial_wc_res'] += 1
                elif service != '*' and res_name == '*':
                    res['partial_wc_res'] += 1
                elif service == '*' and res_name == '*':
                    res['full_wc_res'] += 1
        elif isinstance(resource, list):
            for item in resource:
                if item == '*':
                    res['full_wc_res'] += 1
                elif 'arn:' in item:
                    service, res_name = arn_to_service_and_resource(item)
                    if service == '*' and res_name != '*':
                        res['partial_wc_res'] += 1
                    elif service != '*' and res_name == '*':
                        res['partial_wc_res'] += 1
                    elif service == '*' and res_name == '*':
                        res['full_wc_res'] += 1

    return res

def YmlToProlog(path, template):
    yml_stats = {}
    yml_stats['error'] = False
    facts = set()

    try:
        svs_yml = ServerlessProject(path)
        num_fn = len(svs_yml.config['functions'])

        config = json.dumps(svs_yml.config)

        fn_names = svs_yml.config['functions'].keys()
        bucket_policies = []
        project_resources = set()

        # IamRoleLambdaExectuion is the role created by serverless framework for functions
        # unless a role was explicitly assigned to a function. role_permissions tracks all
        # permissions granted to a custom role
        role_permissions = {}
        role_permissions['IamRoleLambdaExecution'] = []
        if 'resources' in svs_yml.config:
            if 'Resources' in svs_yml.config['resources']:
                resources = svs_yml.config['resources']['Resources']
                for res_name, res_value in resources.items():
                    if 'Type' not in res_value:
                        continue
                    res_type = res_value['Type']
                    if  res_type == 'AWS::IAM::Role':
                        if res_name not in role_permissions:
                            role_permissions[res_name] = []
                        role_permissions[res_name].extend(parse_role_resource(res_name, res_value))
                        
                    # Resources
                    elif res_type == 'AWS::DynamoDB::Table':
                        try:
                            project_resources.add(('dynamodb', res_value['Properties']['TableName']))
                        except KeyError:
                            # Not actually sure the proper way to handle this. Pretty sure
                            # the files that do not have a tablename defined the table
                            # outside of the yml.
                            project_resources.add(('dynamodb', res_name))
                    elif res_type == 'AWS::S3::Bucket':
                        try:
                            project_resources.add(('s3', res_value['Properties']['BucketName']))

                            if 'AccessControl' in res_value['Properties']:
                                # https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-overview.html#canned-acl
                                # functions must be given access via statements
                                # policies define which users (usually public) can access
                                
                                ac_policy = res_value['Properties']['AccessControl']
                                if 'PublicRead' in ac_policy:
                                    bucket_policies.append(
                                        {
                                            'Effect': 'Allow',
                                            'Principal': '*',
                                            'Action': ['s3:GetObject'],
                                            'Resource': res_value['Properties']['BucketName']
                                        }
                                    )
                                if ac_policy == 'PublicReadWrite':
                                    bucket_policies.append(
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
                            project_resources.add(('sns', res_value['Properties']['TopicName']))
                        except KeyError:
                            # Can't really do much about this
                            pass
                    elif res_type == 'AWS::SQS::Queue':
                        try:
                            project_resources.add(('sqs', res_value['Properties']['QueueName']))
                        except KeyError:
                            # Can't really do much about this
                            pass
                    elif res_type == 'AWS::Kinesis::Stream':
                        try:
                            project_resources.add(('kinesis', res_value['Properties']['Name']))
                        except KeyError:
                            # Can't really do much about this
                            pass
                    elif res_type == 'AWS::Events::EventBus':
                        try:
                            project_resources.add(('event', res_value['Properties']['Name']))
                        except KeyError:
                            # Can't really do much about this
                            pass

                    # Policies 
                    elif res_type == 'AWS::S3::BucketPolicy':
                        try:
                            # Ignore Properties.Bucket since pretty sure the ARN must be
                            # given in each policy statement as Resource
                            bucket_policies.extend(res_value['Properties']['PolicyDocument']['Statement'])
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

                                    if role_name not in role_permissions:
                                        role_permissions[role_name] = []
                                    role_permissions[role_name].extend(stmts)
                            elif isinstance(policy_roles, str):
                                if policy_roles not in role_permissions:
                                    role_permissions[policy_roles] = []

                                role_permissions[policy_roles].extend(stmts)
                            elif isinstance(policy_roles, dict):
                                role_name = policy_roles['Ref']
                                if role_name not in role_permissions:
                                    role_permissions[role_name] = []

                                role_permissions[role_name].extend(stmts)
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

        # List of rules applied to all functions
        global_iam = get_provider_iam(svs_yml.config)
        role_permissions['IamRoleLambdaExecution'].extend(global_iam)

        # Add implicitly defined resources to the resource set
        # (resources referenced in rules but not defined in the yaml)
        project_resources.update(extract_resources_from_rules(global_iam))
        for _, role_rules in role_permissions.items():
            project_resources.update(extract_resources_from_rules(role_rules))

        # Parse function definitions, built event facts and collect permissions per functions
        fn_permissions = {}
        for fn_name, fn_value in svs_yml.config['functions'].items():
            if 'events' in fn_value:
                fn_events = fn_value['events']
                if isinstance(fn_events, list):
                    for event in fn_events:
                        if isinstance(event, dict):
                            for event_type in event:
                                facts.update(process_event(fn_name, event_type, event[event_type]))
                        elif isinstance(event, str):
                            # This is an error in the yml itself.
                            continue
                        else:
                            raise NotImplementedError('Unhandled event type in list')
                else:
                    raise NotImplementedError('Events was not a list')

            if 'role' in fn_value:
                role_name = fn_value['role']
                if role_name in role_permissions:
                    fn_permissions[fn_name] = role_permissions[role_name]
                else:
                    # The role is defined outside of the YML
                    fn_permissions[fn_name] = []
            elif 'iamRoleStatements' in fn_value:
                fn_permissions[fn_name] = fn_value['iamRoleStatements']
            else:
                fn_permissions[fn_name] = role_permissions['IamRoleLambdaExecution']

        # Generate facts from function_rules and all resources.
        # fn_permissions, project_resources, and bucket policies

        # function(fn_name, public_facing).
        # if function(name, true). is not already in the fact set from event parsing above then
        # the function is not publicly accessible so add function(name, false).
        for fn_name in fn_names:
            if "function('{}', true).".format(fn_name) not in facts:
                facts.add("function('{}', false).".format(fn_name))

        resource_definitions = {}
        for res_type, res_name in project_resources:
            if res_type == 'lambda':
                continue
            res_key = '{}:{}'.format(res_type.lower(), res_name)
            resource_definitions[res_key] = {}
            resource_definitions[res_key]['type'] = res_type.lower()
            resource_definitions[res_key]['name'] = res_name
            resource_definitions[res_key]['public_read'] = 'false'
            resource_definitions[res_key]['public_write'] = 'false'

        # Update Public Read/Write for s3 buckets
        parse_bucket_policies(bucket_policies, resource_definitions)
                
        for _, res in resource_definitions.items():      
            facts.add("resource('{}', '{}', '{}', '{}').".format(
                res['type'], res['name'], res['public_read'], res['public_write'])
            )

        # Generate function permission facts
        facts.update(function_permissions(fn_names, fn_permissions, resource_definitions))
        
        dirs = path.split('/')
        out_path = '/data/results/{}-{}-{}.pl'.format(dirs[3], dirs[4], attempts)
        with open(out_path, 'w') as outfile:
            outfile.write('% Project repo: {}\n'.format(path))
            outfile.write(template)

            for fact in sorted(list(facts)):
                outfile.write('{}\n'.format(fact))

        # Calc stats based on original YML
        yml_stats['global_iam_stmts'] = len(role_permissions['IamRoleLambdaExecution'])
        yml_stats['fn_iam_stmts'] = {}
        yml_stats['fn_roles_used'] = 0

        # Get count of iamStatements Placed on individual functions and times roles were used
        for fn_name, fn_value in svs_yml.config['functions'].items():
            if 'iamRoleStatements' in fn_value:
                yml_stats['fn_iam_stmts'][fn_name] = len(fn_value['iamRoleStatements'])
            
            if 'role' in fn_value:
                yml_stats['fn_roles_used'] += 1

        # Get a count of how often wild cards were used
        yml_stats['num_full_wc_res'] = 0
        yml_stats['num_full_wc_perm'] = 0   # e.g., *
        yml_stats['num_partial_wc_res'] = 0 
        yml_stats['num_partial_wc_perm'] = 0 # e.g., s3* or s*

        # count wildcards in global statements and other roles
        for role in role_permissions:
            wc_counts = count_wildcards(role_permissions[role])
            yml_stats['num_full_wc_perm'] += wc_counts['full_wc_perm']
            yml_stats['num_full_wc_res'] += wc_counts['full_wc_res']
            yml_stats['num_partial_wc_perm'] += wc_counts['partial_wc_perm']
            yml_stats['num_partial_wc_res'] += wc_counts['partial_wc_res']

        # Count wildcards for functions that define statements
        for fn_name, fn_value in svs_yml.config['functions'].items():
            if 'iamRoleStatements' in fn_value:
                wc_counts = count_wildcards(fn_value['iamRoleStatements'])
                yml_stats['num_full_wc_perm'] += wc_counts['full_wc_perm']
                yml_stats['num_full_wc_res'] += wc_counts['full_wc_res']
                yml_stats['num_partial_wc_perm'] += wc_counts['partial_wc_perm']
                yml_stats['num_partial_wc_res'] += wc_counts['partial_wc_res']

        # Calc Stats based on facts that are created
        yml_stats['num_fn'] = 0
        yml_stats['priv_fn'] = 0
        yml_stats['pub_fn'] = 0
        yml_stats['num_res'] = 0
        yml_stats['res_types'] = {}
        yml_stats['res_pub_rw'] = 0
        yml_stats['res_pub_r'] = 0
        yml_stats['res_pub_w'] = 0
        yml_stats['res_priv'] = 0
        yml_stats['num_perm_facts'] = 0
        yml_stats['fn_perm_facts'] = {}
        yml_stats['events'] = 0
        yml_stats['s3_events'] = 0
        yml_stats['iot_events'] = 0
        yml_stats['stream_msg_events'] = 0
        yml_stats['sns_msg_events'] = 0
        for fact in facts:
            # Get a count of functions, how many are public and private
            if fact.startswith('function('):
                yml_stats['num_fn'] += 1
                match = re.search('function\((.+), (.+)\).', fact)
                is_pub = match.group(2).lower().replace("'", '').strip()
                if 'false' in is_pub:
                    yml_stats['priv_fn'] += 1
                else:
                    yml_stats['pub_fn'] += 1
            # Get a count of resources, types of resources, how many public and private
            elif fact.startswith('resource('):
                yml_stats['num_res'] += 1
                match = re.search('resource\((.+), (.+), (.+), (.+)\).', fact)
                service = match.group(1).lower().replace("'", '').strip()
                pub_read = match.group(3).lower().replace("'", '').strip()
                pub_write = match.group(4).lower().replace("'", '').strip()

                if service not in yml_stats['res_types']:
                    yml_stats['res_types'][service] = 0
                yml_stats['res_types'][service] += 1

                if 'true' in pub_read and 'true' in pub_write:
                    yml_stats['res_pub_rw'] += 1
                elif 'true' in pub_read and 'false' in pub_write:
                    yml_stats['res_pub_r'] += 1
                elif 'false' in pub_read and 'true' in pub_write:
                    yml_stats['res_pub_w'] += 1
                elif 'false' in pub_read and 'false' in pub_write:
                    yml_stats['res_priv'] += 1
                else:
                    print('Error counting resources')
                    print(fact)
                    print(service, pub_write, pub_write)
                    input('Continue>')
            # Get a count of how many permission facts are in out, globally and per function
            elif fact.startswith('permission('):
                yml_stats['num_perm_facts'] += 1
                match = re.search('permission\((.+), (.+), (.+)\).', fact)
                fn_name = match.group(1)
                if fn_name not in yml_stats['fn_perm_facts']:
                    yml_stats['fn_perm_facts'][fn_name] = 0
                yml_stats['fn_perm_facts'][fn_name] += 1
            # Get a count of how many events and types
            elif fact.startswith('event_'):
                yml_stats['events'] += 1
                match = re.search('event_(.+)\(', fact)
                if match.group(1) == 's3':
                    yml_stats['s3_events'] += 1
                elif match.group(1) == 'iot':
                    yml_stats['iot_events'] += 1
                elif match.group(1) == 'stream_msg':
                    yml_stats['stream_msg_events'] += 1
                elif match.group(1) == 'sns_msg':
                    yml_stats['sns_msg_events'] += 1


        yml_stats['fact_file'] = out_path
        yml_stats['yml_file'] = path
        return yml_stats
    except Exception as e:
        #print(traceback.print_exc(e))
        #print(path)
        #print(config)
        yml_stats['yml_file'] = path
        yml_stats['fact_file'] = ''
        yml_stats['error'] = True
        yml_stats['error_msg'] = str(e)
        return yml_stats

def min_max_avg(obj):
    vals = obj.values()

    if len(vals) == 0:
        return 0, 0, 0

    return min(vals), max(vals), sum(vals)/len(vals)

if __name__ == '__main__':
    errors = 0
    attempts = 0

    with open('model.pl', 'r') as template_file:
        template = template_file.read()

    yml_file = 'sec-policy-only.csv'

    with open(yml_file, 'r') as infile, open('YmlStats.csv', 'w', newline='') as outFile:
        reader = csv.reader(infile)
        writer = csv.writer(outFile)
        writer.writerow([
            # General file info
            'YML File',
            'Prolog File',
            # Functions
            'FNs Using Roles',
            'FN Count',
            'Private FN Count',
            'Public FN Count',
            # Resources
            'Resource Count',
            'Public RW Resources',
            'Public RO Resources',
            'Public WO Resources',
            'Private Resources',
            # Individual Resources
            'dynamodb Resources',
            'rds Resources',
            'secretsmanager Resources',
            'route53 Resources',
            'kinesis Resources',
            's3 Resources',
            'apigateway Resources',
            'sqs Resources',
            'ssm Resources',
            'sdb Resources',
            'event Resources',
            'kms Resources',
            'sns Resources',
            # Permissions - Original Statements
            'Global IAM Stmts',
            'Min Stmts Defined Per FN',
            'Max Stmts Defined Per FN',
            'Avg Stmts Defined Per FN',
            'Full Wildcard Resources',
            'Full Wildcard Permissions',
            'Partial Wildcard Resources',
            'Partial Wildcard Permissions',
            # Permissions - Facts Generated
            'Permission Facts Generated',
            'Min Facts Generated Per FN',
            'Max Facts Generated Per FN',
            'Avg Facts Generated Per FN',
            # Events
            'Event Triggers',
            'S3 Triggers',
            'IoT Triggers',
            'Stream Msg Triggers',
            'SNS Msg Triggers',
        ])
        read_header = False
        error_msgs = {}
        all_repos = set()
        repos_w_err = set()
        for row in reader:
            path = row[0]
            facts = set()
            if not read_header:
                read_header = True
                continue

            attempts += 1
            print(path)
            parts = path.split('/')
            all_repos.add(parts[3] + '/' + parts[4])
            res = YmlToProlog(path, template)
            if res['error']:
                repos_w_err.add(parts[3] + '/' + parts[4])
                errors += 1
                msg = res['error_msg']
                if '[Errno 2] No such file or directory' in msg:
                    msg = '[Errno 2] No such file or directory'
                if 'Invalid yml:' in msg:
                    msg = 'Invalid yml'
                if 'Could not generate fake value for' in msg:
                    msg = 'Could not generate fake value'
                if msg not in error_msgs:
                    error_msgs[msg] = 0
                error_msgs[msg] += 1

                continue

            writer.writerow([
                # General file info
                res['yml_file'],
                res['fact_file'],
                # Functions
                res['fn_roles_used'],
                res['num_fn'],
                res['priv_fn'],
                res['pub_fn'],
                # Resources
                res['num_res'],
                res['res_pub_rw'],
                res['res_pub_r'],
                res['res_pub_w'],
                res['res_priv'],
                # Individual Resources
                res['res_types'].get('dynamodb' , 0),
                res['res_types'].get('rds' , 0),
                res['res_types'].get('secretsmanager' , 0),
                res['res_types'].get('route53' , 0),
                res['res_types'].get('kinesis' , 0),
                res['res_types'].get('s3' , 0),
                res['res_types'].get('apigateway' , 0),
                res['res_types'].get('sqs' , 0),
                res['res_types'].get('ssm' , 0),
                res['res_types'].get('sdb' , 0),
                res['res_types'].get('event' , 0),
                res['res_types'].get('kms' , 0),
                res['res_types'].get('sns' , 0),
                # Permissions - Original Statements
                res['global_iam_stmts'],
                min_max_avg(res['fn_iam_stmts'])[0],
                min_max_avg(res['fn_iam_stmts'])[1],
                min_max_avg(res['fn_iam_stmts'])[2],
                res['num_full_wc_res'],
                res['num_full_wc_perm'],
                res['num_partial_wc_res'], 
                res['num_partial_wc_perm'],
                # Permissions - Facts Generated
                res['num_perm_facts'],
                min_max_avg(res['fn_perm_facts'])[0],
                min_max_avg(res['fn_perm_facts'])[1],
                min_max_avg(res['fn_perm_facts'])[2],
                # Events
                res['events'],
                res['s3_events'],
                res['iot_events'],
                res['stream_msg_events'],
                res['sns_msg_events']
                # = {}
            ])

    print('Errors/Attempts: {}/{}'.format(errors, attempts))
    print(error_msgs)
    print('Number of repos: {}'.format(len(all_repos)))
    print('Repos without err: {}'.format(len(all_repos.symmetric_difference(repos_w_err))))
    #for key in sorted(fn_cnt.keys()):
    #    print('{}:{} '.format(key, fn_cnt[key]))
    #print(fn_cnt)
    #print(unimplemented)
