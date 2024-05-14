# These are the event triggers I currently care about
event_wildcards = [
    's3:ObjectCreated:Put', 
    's3:ObjectCreated:Post',
    's3:ObjectCreated:Copy', 
    's3:ObjectCreated:CompleteMultipartCopy',
    's3:ObjectRemoved:Delete', 
    's3:ObjectRemoved:DeleteMarkerCreated'
]


# These are permissions I care about for now that enable reads or writes to shared resources.
# Future expansion can include permissions to change IAM policies or create resources such as ec2
# machines that can trigger ec2 events etc.
permission_wildcards = [
    # s3 permissions https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html
    's3:GetObject',
    's3:PutObject',
    's3:DeleteObject'
    's3:CreateBucket',
    's3:DeleteBucket',

    # dynamodb permissions https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazondynamodb.html
    'dynamodb:BatchGetItem',
    'dynamodb:GetItem',
    'dynamodb:PartiQLSelect',
    'dynamodb:Query',
    'dynamodb:Scan',
    'dynamodb:GetRecords',
    'dynamodb:BatchWriteItem',
    'dynamodb:PartiQLInsert',
    'dynamodb:PartiQLUpdate',
    'dynamodb:PutItem',
    'dynamodb:UpdateItem',

    # RDS permissions
    # https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonrds.html 
    # this seems to just be management type of permissions rather than data access

    # sns permissions https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonsns.html
    'sns:Subscribe',
    'sns:Publish',

    # lambda permissions
    # https://docs.aws.amazon.com/service-authorization/latest/reference/list_awslambda.html
    'lambda:InvokeAsync',
    'lambda:InvokeFunction',

    # sqs permissions
    # https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonsqs.html
    'sqs:ReceiveMessage', 
    'sqs:SendMessage', 

    # iot permissions
    # https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html
    'iot:Receive',
    'iot:Publish',


    # cloudwatch permissions
    # https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoncloudwatch.html
    'cloudwatch:GetMetricData',
    'cloudwatch:PutMetricData',

    # cloudwatch logs permissions
    # https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoncloudwatchlogs.html
    'logs:GetLogEvents',
    'logs:GetLogRecord',
    'logs:PutLogEvents',

    # Kinesis permissions
    # https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonkinesis.html
    'kinesis:GetRecords',
    'kinesis:PutRecord',
    'kinesis:PutRecords',

    # States (Step functions)
    # https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsstepfunctions.html
    # TODO: is there anything important to handle here

    # Sagemaker permissions
    # https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonsagemaker.html
    'sagemaker:GetRecord',
    'sagemaker:PutRecord',

    # Eventbridge permissions
    # https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoneventbridge.html
    'events:PutEvents',

    # Firehose permissions
    # https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonkinesisfirehose.html
    'firehose:PutRecord',
    'firehose:PutRecordBatch',

    # Simpledb permissions
    # https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonsimpledb.html
    'sdb:Select',
    'sdb:GetAttributes',
    'sdb:BatchPutAttributes',
    'sdb:PutAttributes',

    # Athena permissions
    # https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonathena.html
    'athena:GetQueryResults', # this actually reads an S3 bucket and must have s3:GetObject

    # AWS AppSync permissions
    # https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsappsync.html
    'appsync:GraphQL',

    # rds-db permissions
    # https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonrdsiamauthentication.html
    'rds-db:connect', # both read and write

    # rds-data permissions
    # https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonrdsdataapi.html
    'rds-data:BatchExecuteStatement', # both read and write
    'rds-data:ExecuteSql', # both read and write
    'rds-data:ExecuteStatement', # both read and write

    # Neptune-db permissions
    # https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonneptune.html
    'neptune-db:connect', # both read and write
]

def get_vals(wildcard_string, wildcard_type):
    global event_wildcards
    global permission_wildcards
    retval = []
    if wildcard_string[-1] != '*':
        return retval

    if wildcard_type == 'events':
        wildcard_set = event_wildcards
    elif wildcard_type == 'permissions':
        wildcard_set = permission_wildcards
    else:
        raise ValueError('wildcard type must be events or permissions')


    for val in wildcard_set:
        if val.startswith(wildcard_string[:-1]):
            retval.append(val)

    return retval
