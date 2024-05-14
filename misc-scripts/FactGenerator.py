read_permissions = set([
    # s3 permissions https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html
    's3:GetObject',

    # dynamodb permissions https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazondynamodb.html
    'dynamodb:BatchGetItem',
    'dynamodb:GetItem',
    'dynamodb:PartiQLSelect',
    'dynamodb:Query',
    'dynamodb:Scan',
    'dynamodb:GetRecords',

    # RDS permissions
    # https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonrds.html 
    # this seems to just be management type of permissions rather than data access

    # sns permissions https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonsns.html
    'sns:Subscribe',

    # sqs permissions
    # https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonsqs.html
    'sqs:ReceiveMessage', 

    # iot permissions
    # https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html
    'iot:Receive',

    # cloudwatch permissions
    # https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoncloudwatch.html
    'cloudwatch:GetMetricData',

    # cloudwatch logs permissions
    # https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoncloudwatchlogs.html
    'logs:GetLogEvents',
    'logs:GetLogRecord',

    # Kinesis permissions
    # https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonkinesis.html
    'kinesis:GetRecords',

    # Sagemaker permissions
    # https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonsagemaker.html
    'sagemaker:GetRecord',

    # Simpledb permissions
    # https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonsimpledb.html
    'sdb:Select',
    'sdb:GetAttributes',

    # Athena permissions
    # https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonathena.html
    'athena:GetQueryResults', # this actually reads an S3 bucket and must have s3:GetObject

    # AWS AppSync permissions
    # https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsappsync.html
    'appsync:GraphQL', # both read and write

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
])

write_permissions = set([
    # s3 permissions https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html
    's3:PutObject',

    # dynamodb permissions https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazondynamodb.html
    'dynamodb:BatchWriteItem',
    'dynamodb:PartiQLInsert',
    'dynamodb:PartiQLUpdate',
    'dynamodb:PutItem',
    'dynamodb:UpdateItem',

    # sns permissions https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonsns.html
    'sns:Publish',

    # sqs permissions
    # https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonsqs.html
    'sqs:SendMessage', 

    # iot permissions
    # https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html
    'iot:Publish',

    # cloudwatch permissions
    # https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoncloudwatch.html
    'cloudwatch:PutMetricData',

    # cloudwatch logs permissions
    # https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoncloudwatchlogs.html
    'logs:PutLogEvents',

    # Kinesis permissions
    # https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonkinesis.html
    'kinesis:PutRecord',
    'kinesis:PutRecords',

    # Sagemaker permissions
    # https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonsagemaker.html
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
    'sdb:BatchPutAttributes',
    'sdb:PutAttributes',

    # AWS AppSync permissions
    # https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsappsync.html
    'appsync:GraphQL', # both read and write

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
])


# Other
# # s3 permissions https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html
# 's3:DeleteObject'
# 's3:CreateBucket',
# 's3:DeleteBucket',

# # lambda permissions
# # https://docs.aws.amazon.com/service-authorization/latest/reference/list_awslambda.html
# 'lambda:InvokeAsync',
# 'lambda:InvokeFunction',
