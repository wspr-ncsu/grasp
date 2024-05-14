# From https://gist.github.com/bernadinm/6f68bfdd015b3f3e0a17b2f00c9ea3f8
policies = {
    "AWSAccountActivityAccess": {
        "Arn": "arn:aws:iam::aws:policy/AWSAccountActivityAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:41:18+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "aws-portal:ViewBilling"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJQRYCWMFX5J3E333K",
        "PolicyName": "AWSAccountActivityAccess",
        "UpdateDate": "2015-02-06T18:41:18+00:00",
        "VersionId": "v1"
    },
    "AWSAccountUsageReportAccess": {
        "Arn": "arn:aws:iam::aws:policy/AWSAccountUsageReportAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:41:19+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "aws-portal:ViewUsage"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJLIB4VSBVO47ZSBB6",
        "PolicyName": "AWSAccountUsageReportAccess",
        "UpdateDate": "2015-02-06T18:41:19+00:00",
        "VersionId": "v1"
    },
    "AWSCloudFormationReadOnlyAccess": {
        "Arn": "arn:aws:iam::aws:policy/AWSCloudFormationReadOnlyAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:39:49+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "cloudformation:DescribeStacks",
                        "cloudformation:DescribeStackEvents",
                        "cloudformation:DescribeStackResource",
                        "cloudformation:DescribeStackResources",
                        "cloudformation:GetTemplate",
                        "cloudformation:List*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJWVBEE4I2POWLODLW",
        "PolicyName": "AWSCloudFormationReadOnlyAccess",
        "UpdateDate": "2015-02-06T18:39:49+00:00",
        "VersionId": "v1"
    },
    "AWSCloudHSMFullAccess": {
        "Arn": "arn:aws:iam::aws:policy/AWSCloudHSMFullAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:39:51+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": "cloudhsm:*",
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAIMBQYQZM7F63DA2UU",
        "PolicyName": "AWSCloudHSMFullAccess",
        "UpdateDate": "2015-02-06T18:39:51+00:00",
        "VersionId": "v1"
    },
    "AWSCloudHSMReadOnlyAccess": {
        "Arn": "arn:aws:iam::aws:policy/AWSCloudHSMReadOnlyAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:39:52+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "cloudhsm:Get*",
                        "cloudhsm:List*",
                        "cloudhsm:Describe*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAISVCBSY7YDBOT67KE",
        "PolicyName": "AWSCloudHSMReadOnlyAccess",
        "UpdateDate": "2015-02-06T18:39:52+00:00",
        "VersionId": "v1"
    },
    "AWSCloudHSMRole": {
        "Arn": "arn:aws:iam::aws:policy/service-role/AWSCloudHSMRole",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:41:23+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "ec2:CreateNetworkInterface",
                        "ec2:CreateTags",
                        "ec2:DeleteNetworkInterface",
                        "ec2:DescribeNetworkInterfaceAttribute",
                        "ec2:DescribeNetworkInterfaces",
                        "ec2:DescribeSubnets",
                        "ec2:DescribeVpcs",
                        "ec2:DetachNetworkInterface"
                    ],
                    "Effect": "Allow",
                    "Resource": [
                        "*"
                    ]
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/service-role/",
        "PolicyId": "ANPAI7QIUU4GC66SF26WE",
        "PolicyName": "AWSCloudHSMRole",
        "UpdateDate": "2015-02-06T18:41:23+00:00",
        "VersionId": "v1"
    },
    "AWSCloudTrailFullAccess": {
        "Arn": "arn:aws:iam::aws:policy/AWSCloudTrailFullAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-10-01T16:19:40+00:00",
        "DefaultVersionId": "v3",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "sns:AddPermission",
                        "sns:CreateTopic",
                        "sns:DeleteTopic",
                        "sns:ListTopics",
                        "sns:SetTopicAttributes",
                        "sns:GetTopicAttributes"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                },
                {
                    "Action": [
                        "s3:CreateBucket",
                        "s3:DeleteBucket",
                        "s3:ListAllMyBuckets",
                        "s3:PutBucketPolicy",
                        "s3:ListBucket",
                        "s3:GetObject",
                        "s3:GetBucketLocation",
                        "s3:GetBucketPolicy"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                },
                {
                    "Action": "cloudtrail:*",
                    "Effect": "Allow",
                    "Resource": "*"
                },
                {
                    "Action": [
                        "logs:CreateLogGroup"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                },
                {
                    "Action": [
                        "iam:PassRole",
                        "iam:ListRoles",
                        "iam:GetRolePolicy",
                        "iam:GetUser"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                },
                {
                    "Action": [
                        "kms:GetKeys",
                        "kms:GetAliases"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAIQNUJTQYDRJPC3BNK",
        "PolicyName": "AWSCloudTrailFullAccess",
        "UpdateDate": "2015-10-01T16:19:40+00:00",
        "VersionId": "v3"
    },
    "AWSCloudTrailReadOnlyAccess": {
        "Arn": "arn:aws:iam::aws:policy/AWSCloudTrailReadOnlyAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-10-01T16:17:59+00:00",
        "DefaultVersionId": "v4",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "s3:GetObject",
                        "s3:GetBucketLocation"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                },
                {
                    "Action": [
                        "cloudtrail:GetTrailStatus",
                        "cloudtrail:DescribeTrails",
                        "cloudtrail:LookupEvents",
                        "cloudtrail:ListTags",
                        "s3:ListAllMyBuckets",
                        "kms:ListAlias"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJDU7KJADWBSEQ3E7S",
        "PolicyName": "AWSCloudTrailReadOnlyAccess",
        "UpdateDate": "2015-10-01T16:17:59+00:00",
        "VersionId": "v4"
    },
    "AWSCodeCommitFullAccess": {
        "Arn": "arn:aws:iam::aws:policy/AWSCodeCommitFullAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-07-09T17:02:19+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "codecommit:*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAI4VCZ3XPIZLQ5NZV2",
        "PolicyName": "AWSCodeCommitFullAccess",
        "UpdateDate": "2015-07-09T17:02:19+00:00",
        "VersionId": "v1"
    },
    "AWSCodeCommitPowerUser": {
        "Arn": "arn:aws:iam::aws:policy/AWSCodeCommitPowerUser",
        "AttachmentCount": 0,
        "CreateDate": "2015-10-22T17:21:25+00:00",
        "DefaultVersionId": "v2",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "codecommit:BatchGetRepositories",
                        "codecommit:CreateBranch",
                        "codecommit:CreateRepository",
                        "codecommit:Get*",
                        "codecommit:GitPull",
                        "codecommit:GitPush",
                        "codecommit:List*",
                        "codecommit:Put*",
                        "codecommit:Test*",
                        "codecommit:Update*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAI4UIINUVGB5SEC57G",
        "PolicyName": "AWSCodeCommitPowerUser",
        "UpdateDate": "2015-10-22T17:21:25+00:00",
        "VersionId": "v2"
    },
    "AWSCodeCommitReadOnly": {
        "Arn": "arn:aws:iam::aws:policy/AWSCodeCommitReadOnly",
        "AttachmentCount": 0,
        "CreateDate": "2015-07-09T17:05:06+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "codecommit:BatchGetRepositories",
                        "codecommit:Get*",
                        "codecommit:GitPull",
                        "codecommit:List*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJACNSXR7Z2VLJW3D6",
        "PolicyName": "AWSCodeCommitReadOnly",
        "UpdateDate": "2015-07-09T17:05:06+00:00",
        "VersionId": "v1"
    },
    "AWSCodeDeployDeployerAccess": {
        "Arn": "arn:aws:iam::aws:policy/AWSCodeDeployDeployerAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-05-19T18:18:43+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "codedeploy:Batch*",
                        "codedeploy:CreateDeployment",
                        "codedeploy:Get*",
                        "codedeploy:List*",
                        "codedeploy:RegisterApplicationRevision"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJUWEPOMGLMVXJAPUI",
        "PolicyName": "AWSCodeDeployDeployerAccess",
        "UpdateDate": "2015-05-19T18:18:43+00:00",
        "VersionId": "v1"
    },
    "AWSCodeDeployFullAccess": {
        "Arn": "arn:aws:iam::aws:policy/AWSCodeDeployFullAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-05-19T18:13:23+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": "codedeploy:*",
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAIONKN3TJZUKXCHXWC",
        "PolicyName": "AWSCodeDeployFullAccess",
        "UpdateDate": "2015-05-19T18:13:23+00:00",
        "VersionId": "v1"
    },
    "AWSCodeDeployReadOnlyAccess": {
        "Arn": "arn:aws:iam::aws:policy/AWSCodeDeployReadOnlyAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-05-19T18:21:32+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "codedeploy:Batch*",
                        "codedeploy:Get*",
                        "codedeploy:List*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAILZHHKCKB4NE7XOIQ",
        "PolicyName": "AWSCodeDeployReadOnlyAccess",
        "UpdateDate": "2015-05-19T18:21:32+00:00",
        "VersionId": "v1"
    },
    "AWSCodeDeployRole": {
        "Arn": "arn:aws:iam::aws:policy/service-role/AWSCodeDeployRole",
        "AttachmentCount": 0,
        "CreateDate": "2015-05-04T18:05:37+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "autoscaling:CompleteLifecycleAction",
                        "autoscaling:DeleteLifecycleHook",
                        "autoscaling:DescribeAutoScalingGroups",
                        "autoscaling:DescribeLifecycleHooks",
                        "autoscaling:PutLifecycleHook",
                        "autoscaling:RecordLifecycleActionHeartbeat",
                        "ec2:DescribeInstances",
                        "ec2:DescribeInstanceStatus",
                        "tag:GetTags",
                        "tag:GetResources"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/service-role/",
        "PolicyId": "ANPAJ2NKMKD73QS5NBFLA",
        "PolicyName": "AWSCodeDeployRole",
        "UpdateDate": "2015-05-04T18:05:37+00:00",
        "VersionId": "v1"
    },
    "AWSCodePipelineCustomActionAccess": {
        "Arn": "arn:aws:iam::aws:policy/AWSCodePipelineCustomActionAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-07-09T17:02:54+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "codepipeline:AcknowledgeJob",
                        "codepipeline:GetJobDetails",
                        "codepipeline:PollForJobs",
                        "codepipeline:PutJobFailureResult",
                        "codepipeline:PutJobSuccessResult"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJFW5Z32BTVF76VCYC",
        "PolicyName": "AWSCodePipelineCustomActionAccess",
        "UpdateDate": "2015-07-09T17:02:54+00:00",
        "VersionId": "v1"
    },
    "AWSCodePipelineFullAccess": {
        "Arn": "arn:aws:iam::aws:policy/AWSCodePipelineFullAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-07-09T22:12:17+00:00",
        "DefaultVersionId": "v2",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "codepipeline:*",
                        "iam:ListRoles",
                        "iam:PassRole",
                        "s3:CreateBucket",
                        "s3:GetBucketPolicy",
                        "s3:GetObject",
                        "s3:ListAllMyBuckets",
                        "s3:ListBucket",
                        "s3:PutBucketPolicy",
                        "codedeploy:GetApplication",
                        "codedeploy:GetDeploymentGroup",
                        "codedeploy:ListApplications",
                        "codedeploy:ListDeploymentGroups",
                        "elasticbeanstalk:DescribeApplications",
                        "elasticbeanstalk:DescribeEnvironments",
                        "lambda:GetFunctionConfiguration",
                        "lambda:ListFunctions"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJP5LH77KSAT2KHQGG",
        "PolicyName": "AWSCodePipelineFullAccess",
        "UpdateDate": "2015-07-09T22:12:17+00:00",
        "VersionId": "v2"
    },
    "AWSCodePipelineReadOnlyAccess": {
        "Arn": "arn:aws:iam::aws:policy/AWSCodePipelineReadOnlyAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-07-09T22:02:56+00:00",
        "DefaultVersionId": "v2",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "codepipeline:GetPipeline",
                        "codepipeline:GetPipelineState",
                        "codepipeline:ListActionTypes",
                        "codepipeline:ListPipelines",
                        "iam:ListRoles",
                        "s3:GetBucketPolicy",
                        "s3:GetObject",
                        "s3:ListAllMyBuckets",
                        "s3:ListBucket",
                        "codedeploy:GetApplication",
                        "codedeploy:GetDeploymentGroup",
                        "codedeploy:ListApplications",
                        "codedeploy:ListDeploymentGroups",
                        "elasticbeanstalk:DescribeApplications",
                        "elasticbeanstalk:DescribeEnvironments",
                        "lambda:GetFunctionConfiguration",
                        "lambda:ListFunctions"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAILFKZXIBOTNC5TO2Q",
        "PolicyName": "AWSCodePipelineReadOnlyAccess",
        "UpdateDate": "2015-07-09T22:02:56+00:00",
        "VersionId": "v2"
    },
    "AWSConfigRole": {
        "Arn": "arn:aws:iam::aws:policy/service-role/AWSConfigRole",
        "AttachmentCount": 0,
        "CreateDate": "2015-11-04T19:18:44+00:00",
        "DefaultVersionId": "v3",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "cloudtrail:DescribeTrails",
                        "ec2:Describe*",
                        "config:PutEvaluations",
                        "cloudtrail:GetTrailStatus",
                        "s3:GetObject",
                        "iam:GetAccountAuthorizationDetails",
                        "iam:GetGroup",
                        "iam:GetGroupPolicy",
                        "iam:GetPolicy",
                        "iam:GetPolicyVersion",
                        "iam:GetRole",
                        "iam:GetRolePolicy",
                        "iam:GetUser",
                        "iam:GetUserPolicy",
                        "iam:ListAttachedGroupPolicies",
                        "iam:ListAttachedRolePolicies",
                        "iam:ListAttachedUserPolicies",
                        "iam:ListEntitiesForPolicy",
                        "iam:ListGroupPolicies",
                        "iam:ListGroupsForUser",
                        "iam:ListInstanceProfilesForRole",
                        "iam:ListPolicyVersions",
                        "iam:ListRolePolicies",
                        "iam:ListUserPolicies"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/service-role/",
        "PolicyId": "ANPAIQRXRDRGJUA33ELIO",
        "PolicyName": "AWSConfigRole",
        "UpdateDate": "2015-11-04T19:18:44+00:00",
        "VersionId": "v3"
    },
    "AWSConfigUserAccess": {
        "Arn": "arn:aws:iam::aws:policy/AWSConfigUserAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-09-02T17:44:33+00:00",
        "DefaultVersionId": "v2",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "config:Get*",
                        "config:Describe*",
                        "config:Deliver*",
                        "config:List*",
                        "tag:GetResources",
                        "tag:GetTagKeys"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAIWTTSFJ7KKJE3MWGA",
        "PolicyName": "AWSConfigUserAccess",
        "UpdateDate": "2015-09-02T17:44:33+00:00",
        "VersionId": "v2"
    },
    "AWSConnector": {
        "Arn": "arn:aws:iam::aws:policy/AWSConnector",
        "AttachmentCount": 0,
        "CreateDate": "2015-09-28T19:50:38+00:00",
        "DefaultVersionId": "v3",
        "Document": {
            "Statement": [
                {
                    "Action": "iam:GetUser",
                    "Effect": "Allow",
                    "Resource": "*"
                },
                {
                    "Action": [
                        "s3:ListAllMyBuckets"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                },
                {
                    "Action": [
                        "s3:CreateBucket",
                        "s3:DeleteBucket",
                        "s3:DeleteObject",
                        "s3:GetBucketLocation",
                        "s3:GetObject",
                        "s3:ListBucket",
                        "s3:PutObject",
                        "s3:PutObjectAcl",
                        "s3:AbortMultipartUpload",
                        "s3:ListBucketMultipartUploads",
                        "s3:ListMultipartUploadParts"
                    ],
                    "Effect": "Allow",
                    "Resource": "arn:aws:s3:::import-to-ec2-*"
                },
                {
                    "Action": [
                        "ec2:CancelConversionTask",
                        "ec2:CancelExportTask",
                        "ec2:CreateImage",
                        "ec2:CreateInstanceExportTask",
                        "ec2:CreateTags",
                        "ec2:CreateVolume",
                        "ec2:DeleteTags",
                        "ec2:DeleteVolume",
                        "ec2:DescribeConversionTasks",
                        "ec2:DescribeExportTasks",
                        "ec2:DescribeImages",
                        "ec2:DescribeInstanceAttribute",
                        "ec2:DescribeInstanceStatus",
                        "ec2:DescribeInstances",
                        "ec2:DescribeRegions",
                        "ec2:DescribeTags",
                        "ec2:DetachVolume",
                        "ec2:ImportInstance",
                        "ec2:ImportVolume",
                        "ec2:ModifyInstanceAttribute",
                        "ec2:RunInstances",
                        "ec2:StartInstances",
                        "ec2:StopInstances",
                        "ec2:TerminateInstances",
                        "ec2:ImportImage",
                        "ec2:DescribeImportImageTasks",
                        "ec2:DeregisterImage",
                        "ec2:DescribeSnapshots",
                        "ec2:DeleteSnapshot",
                        "ec2:CancelImportTask",
                        "ec2:ImportSnapshot",
                        "ec2:DescribeImportSnapshotTasks"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                },
                {
                    "Action": [
                        "SNS:Publish"
                    ],
                    "Effect": "Allow",
                    "Resource": "arn:aws:sns:*:*:metrics-sns-topic-for-*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJ6YATONJHICG3DJ3U",
        "PolicyName": "AWSConnector",
        "UpdateDate": "2015-09-28T19:50:38+00:00",
        "VersionId": "v3"
    },
    "AWSDataPipelineFullAccess": {
        "Arn": "arn:aws:iam::aws:policy/AWSDataPipelineFullAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:40:05+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "s3:List*",
                        "dynamodb:DescribeTable",
                        "rds:DescribeDBInstances",
                        "rds:DescribeDBSecurityGroups",
                        "redshift:DescribeClusters",
                        "redshift:DescribeClusterSecurityGroups",
                        "sns:CreateTopic",
                        "sns:ListTopics",
                        "sns:Subscribe",
                        "iam:PassRole",
                        "iam:ListRoles",
                        "iam:CreateRole",
                        "iam:PutRolePolicy",
                        "iam:GetRolePolicy",
                        "iam:GetInstanceProfiles",
                        "iam:ListInstanceProfiles",
                        "iam:CreateInstanceProfile",
                        "iam:AddRoleToInstanceProfile",
                        "datapipeline:*",
                        "cloudwatch:*"
                    ],
                    "Effect": "Allow",
                    "Resource": [
                        "*"
                    ]
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJZVYL5DGR3IHUEA2O",
        "PolicyName": "AWSDataPipelineFullAccess",
        "UpdateDate": "2015-02-06T18:40:05+00:00",
        "VersionId": "v1"
    },
    "AWSDataPipelinePowerUser": {
        "Arn": "arn:aws:iam::aws:policy/AWSDataPipelinePowerUser",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:40:06+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "s3:List*",
                        "dynamodb:DescribeTable",
                        "rds:DescribeDBInstances",
                        "rds:DescribeDBSecurityGroups",
                        "redshift:DescribeClusters",
                        "redshift:DescribeClusterSecurityGroups",
                        "sns:ListTopics",
                        "iam:PassRole",
                        "iam:ListRoles",
                        "iam:PutRolePolicy",
                        "iam:GetRolePolicy",
                        "iam:GetInstanceProfiles",
                        "iam:ListInstanceProfiles",
                        "iam:CreateInstanceProfile",
                        "iam:AddRoleToInstanceProfile",
                        "datapipeline:*",
                        "cloudwatch:*"
                    ],
                    "Effect": "Allow",
                    "Resource": [
                        "*"
                    ]
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJW53AHN6ZWYGU2GNO",
        "PolicyName": "AWSDataPipelinePowerUser",
        "UpdateDate": "2015-02-06T18:40:06+00:00",
        "VersionId": "v1"
    },
    "AWSDataPipelineRole": {
        "Arn": "arn:aws:iam::aws:policy/service-role/AWSDataPipelineRole",
        "AttachmentCount": 0,
        "CreateDate": "2015-07-01T21:38:04+00:00",
        "DefaultVersionId": "v3",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "cloudwatch:*",
                        "datapipeline:DescribeObjects",
                        "datapipeline:EvaluateExpression",
                        "dynamodb:BatchGetItem",
                        "dynamodb:DescribeTable",
                        "dynamodb:GetItem",
                        "dynamodb:Query",
                        "dynamodb:Scan",
                        "dynamodb:UpdateTable",
                        "ec2:AuthorizeSecurityGroupIngress",
                        "ec2:CancelSpotInstanceRequests",
                        "ec2:CreateSecurityGroup",
                        "ec2:CreateTags",
                        "ec2:DeleteTags",
                        "ec2:Describe*",
                        "ec2:ModifyImageAttribute",
                        "ec2:ModifyInstanceAttribute",
                        "ec2:RequestSpotInstances",
                        "ec2:RunInstances",
                        "ec2:StartInstances",
                        "ec2:StopInstances",
                        "ec2:TerminateInstances",
                        "elasticmapreduce:*",
                        "iam:GetInstanceProfile",
                        "iam:GetRole",
                        "iam:GetRolePolicy",
                        "iam:ListAttachedRolePolicies",
                        "iam:ListRolePolicies",
                        "iam:ListInstanceProfiles",
                        "iam:PassRole",
                        "rds:DescribeDBInstances",
                        "rds:DescribeDBSecurityGroups",
                        "redshift:DescribeClusters",
                        "redshift:DescribeClusterSecurityGroups",
                        "s3:CreateBucket",
                        "s3:DeleteObject",
                        "s3:Get*",
                        "s3:List*",
                        "s3:Put*",
                        "sdb:BatchPutAttributes",
                        "sdb:Select*",
                        "sns:GetTopicAttributes",
                        "sns:ListTopics",
                        "sns:Publish",
                        "sns:Subscribe",
                        "sns:Unsubscribe"
                    ],
                    "Effect": "Allow",
                    "Resource": [
                        "*"
                    ]
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/service-role/",
        "PolicyId": "ANPAIKCP6XS3ESGF4GLO2",
        "PolicyName": "AWSDataPipelineRole",
        "UpdateDate": "2015-07-01T21:38:04+00:00",
        "VersionId": "v3"
    },
    "AWSDeviceFarmFullAccess": {
        "Arn": "arn:aws:iam::aws:policy/AWSDeviceFarmFullAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-07-13T16:37:38+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "devicefarm:*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJO7KEDP4VYJPNT5UW",
        "PolicyName": "AWSDeviceFarmFullAccess",
        "UpdateDate": "2015-07-13T16:37:38+00:00",
        "VersionId": "v1"
    },
    "AWSDirectConnectFullAccess": {
        "Arn": "arn:aws:iam::aws:policy/AWSDirectConnectFullAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:40:07+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "directconnect:*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJQF2QKZSK74KTIHOW",
        "PolicyName": "AWSDirectConnectFullAccess",
        "UpdateDate": "2015-02-06T18:40:07+00:00",
        "VersionId": "v1"
    },
    "AWSDirectConnectReadOnlyAccess": {
        "Arn": "arn:aws:iam::aws:policy/AWSDirectConnectReadOnlyAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:40:08+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "directconnect:Describe*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAI23HZ27SI6FQMGNQ2",
        "PolicyName": "AWSDirectConnectReadOnlyAccess",
        "UpdateDate": "2015-02-06T18:40:08+00:00",
        "VersionId": "v1"
    },
    "AWSDirectoryServiceFullAccess": {
        "Arn": "arn:aws:iam::aws:policy/AWSDirectoryServiceFullAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:41:11+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "ds:*",
                        "ec2:AuthorizeSecurityGroupEgress",
                        "ec2:AuthorizeSecurityGroupIngress",
                        "ec2:CreateNetworkInterface",
                        "ec2:CreateSecurityGroup",
                        "ec2:DeleteNetworkInterface",
                        "ec2:DeleteSecurityGroup",
                        "ec2:DescribeNetworkInterfaces",
                        "ec2:DescribeSubnets",
                        "ec2:DescribeVpcs",
                        "ec2:RevokeSecurityGroupEgress",
                        "ec2:RevokeSecurityGroupIngress"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAINAW5ANUWTH3R4ANI",
        "PolicyName": "AWSDirectoryServiceFullAccess",
        "UpdateDate": "2015-02-06T18:41:11+00:00",
        "VersionId": "v1"
    },
    "AWSDirectoryServiceReadOnlyAccess": {
        "Arn": "arn:aws:iam::aws:policy/AWSDirectoryServiceReadOnlyAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:41:12+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "ds:Check*",
                        "ds:Describe*",
                        "ds:Get*",
                        "ds:List*",
                        "ec2:DescribeNetworkInterfaces",
                        "ec2:DescribeSubnets",
                        "ec2:DescribeVpcs"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAIHWYO6WSDNCG64M2W",
        "PolicyName": "AWSDirectoryServiceReadOnlyAccess",
        "UpdateDate": "2015-02-06T18:41:12+00:00",
        "VersionId": "v1"
    },
    "AWSElasticBeanstalkFullAccess": {
        "Arn": "arn:aws:iam::aws:policy/AWSElasticBeanstalkFullAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:40:18+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "elasticbeanstalk:*",
                        "ec2:*",
                        "elasticloadbalancing:*",
                        "autoscaling:*",
                        "cloudwatch:*",
                        "s3:*",
                        "sns:*",
                        "cloudformation:*",
                        "rds:*",
                        "sqs:*",
                        "iam:PassRole"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAIZYX2YLLBW2LJVUFW",
        "PolicyName": "AWSElasticBeanstalkFullAccess",
        "UpdateDate": "2015-02-06T18:40:18+00:00",
        "VersionId": "v1"
    },
    "AWSElasticBeanstalkReadOnlyAccess": {
        "Arn": "arn:aws:iam::aws:policy/AWSElasticBeanstalkReadOnlyAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:40:19+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "elasticbeanstalk:Check*",
                        "elasticbeanstalk:Describe*",
                        "elasticbeanstalk:List*",
                        "elasticbeanstalk:RequestEnvironmentInfo",
                        "elasticbeanstalk:RetrieveEnvironmentInfo",
                        "ec2:Describe*",
                        "elasticloadbalancing:Describe*",
                        "autoscaling:Describe*",
                        "cloudwatch:Describe*",
                        "cloudwatch:List*",
                        "cloudwatch:Get*",
                        "s3:Get*",
                        "s3:List*",
                        "sns:Get*",
                        "sns:List*",
                        "cloudformation:Describe*",
                        "cloudformation:Get*",
                        "cloudformation:List*",
                        "cloudformation:Validate*",
                        "cloudformation:Estimate*",
                        "rds:Describe*",
                        "sqs:Get*",
                        "sqs:List*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAI47KNGXDAXFD4SDHG",
        "PolicyName": "AWSElasticBeanstalkReadOnlyAccess",
        "UpdateDate": "2015-02-06T18:40:19+00:00",
        "VersionId": "v1"
    },
    "AWSImportExportFullAccess": {
        "Arn": "arn:aws:iam::aws:policy/AWSImportExportFullAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:40:43+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "importexport:*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJCQCT4JGTLC6722MQ",
        "PolicyName": "AWSImportExportFullAccess",
        "UpdateDate": "2015-02-06T18:40:43+00:00",
        "VersionId": "v1"
    },
    "AWSImportExportReadOnlyAccess": {
        "Arn": "arn:aws:iam::aws:policy/AWSImportExportReadOnlyAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:40:42+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "importexport:ListJobs",
                        "importexport:GetStatus"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJNTV4OG52ESYZHCNK",
        "PolicyName": "AWSImportExportReadOnlyAccess",
        "UpdateDate": "2015-02-06T18:40:42+00:00",
        "VersionId": "v1"
    },
    "AWSIoTConfigAccess": {
        "Arn": "arn:aws:iam::aws:policy/AWSIoTConfigAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-10-27T21:52:07+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "iot:AcceptCertificateTransfer",
                        "iot:AttachPrincipalPolicy",
                        "iot:AttachThingPrincipal",
                        "iot:CancelCertificateTransfer",
                        "iot:CreateCertificateFromCsr",
                        "iot:CreateKeysAndCertificate",
                        "iot:CreatePolicy",
                        "iot:CreatePolicyVersion",
                        "iot:CreateThing",
                        "iot:CreateTopicRule",
                        "iot:DeleteCertificate",
                        "iot:DeletePolicy",
                        "iot:DeletePolicyVersion",
                        "iot:DeleteThing",
                        "iot:DeleteTopicRule",
                        "iot:DescribeCertificate",
                        "iot:DescribeEndpoint",
                        "iot:DescribeThing",
                        "iot:DetachPrincipalPolicy",
                        "iot:DetachThingPrincipal",
                        "iot:GetLoggingOptions",
                        "iot:GetPolicy",
                        "iot:GetPolicyVersion",
                        "iot:GetTopicRule",
                        "iot:ListCertificates",
                        "iot:ListPolicies",
                        "iot:ListPolicyVersions",
                        "iot:ListPrincipalPolicies",
                        "iot:ListPrincipalThings",
                        "iot:ListThingPrincipals",
                        "iot:ListThings",
                        "iot:ListTopicRules",
                        "iot:RejectCertificateTransfer",
                        "iot:ReplaceTopicRule",
                        "iot:SetDefaultPolicyVersion",
                        "iot:SetLoggingOptions",
                        "iot:TransferCertificate",
                        "iot:UpdateCertificate",
                        "iot:UpdateThing"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAIWWGD4LM4EMXNRL7I",
        "PolicyName": "AWSIoTConfigAccess",
        "UpdateDate": "2015-10-27T21:52:07+00:00",
        "VersionId": "v1"
    },
    "AWSIoTConfigReadOnlyAccess": {
        "Arn": "arn:aws:iam::aws:policy/AWSIoTConfigReadOnlyAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-10-27T21:52:31+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "iot:DescribeCertificate",
                        "iot:DescribeEndpoint",
                        "iot:DescribeThing",
                        "iot:GetLoggingOptions",
                        "iot:GetPolicy",
                        "iot:GetPolicyVersion",
                        "iot:GetTopicRule",
                        "iot:ListCertificates",
                        "iot:ListPolicies",
                        "iot:ListPolicyVersions",
                        "iot:ListPrincipalPolicies",
                        "iot:ListPrincipalThings",
                        "iot:ListThingPrincipals",
                        "iot:ListThings",
                        "iot:ListTopicRules"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJHENEMXGX4XMFOIOI",
        "PolicyName": "AWSIoTConfigReadOnlyAccess",
        "UpdateDate": "2015-10-27T21:52:31+00:00",
        "VersionId": "v1"
    },
    "AWSIoTDataAccess": {
        "Arn": "arn:aws:iam::aws:policy/AWSIoTDataAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-10-27T21:51:18+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "iot:Connect",
                        "iot:Publish",
                        "iot:Subscribe",
                        "iot:Receive",
                        "iot:GetThingShadow",
                        "iot:UpdateThingShadow"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJM2KI2UJDR24XPS2K",
        "PolicyName": "AWSIoTDataAccess",
        "UpdateDate": "2015-10-27T21:51:18+00:00",
        "VersionId": "v1"
    },
    "AWSIoTFullAccess": {
        "Arn": "arn:aws:iam::aws:policy/AWSIoTFullAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-10-08T15:19:49+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "iot:*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJU2FPGG6PQWN72V2G",
        "PolicyName": "AWSIoTFullAccess",
        "UpdateDate": "2015-10-08T15:19:49+00:00",
        "VersionId": "v1"
    },
    "AWSIoTLogging": {
        "Arn": "arn:aws:iam::aws:policy/service-role/AWSIoTLogging",
        "AttachmentCount": 0,
        "CreateDate": "2015-10-08T15:17:25+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "logs:CreateLogGroup",
                        "logs:CreateLogStream",
                        "logs:PutLogEvents",
                        "logs:PutMetricFilter",
                        "logs:PutRetentionPolicy",
                        "logs:GetLogEvents",
                        "logs:DeleteLogStream"
                    ],
                    "Effect": "Allow",
                    "Resource": [
                        "*"
                    ]
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/service-role/",
        "PolicyId": "ANPAI6R6Z2FHHGS454W7W",
        "PolicyName": "AWSIoTLogging",
        "UpdateDate": "2015-10-08T15:17:25+00:00",
        "VersionId": "v1"
    },
    "AWSIoTRuleActions": {
        "Arn": "arn:aws:iam::aws:policy/service-role/AWSIoTRuleActions",
        "AttachmentCount": 0,
        "CreateDate": "2015-10-08T15:14:51+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": {
                "Action": [
                    "dynamodb:PutItem",
                    "kinesis:PutRecord",
                    "iot:Publish",
                    "s3:PutObject",
                    "sns:Publish",
                    "sqs:SendMessage*"
                ],
                "Effect": "Allow",
                "Resource": "*"
            },
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/service-role/",
        "PolicyId": "ANPAJEZ6FS7BUZVUHMOKY",
        "PolicyName": "AWSIoTRuleActions",
        "UpdateDate": "2015-10-08T15:14:51+00:00",
        "VersionId": "v1"
    },
    "AWSKeyManagementServicePowerUser": {
        "Arn": "arn:aws:iam::aws:policy/AWSKeyManagementServicePowerUser",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:40:40+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "kms:CreateAlias",
                        "kms:CreateKey",
                        "kms:DeleteAlias",
                        "kms:Describe*",
                        "kms:GenerateRandom",
                        "kms:Get*",
                        "kms:List*",
                        "iam:ListGroups",
                        "iam:ListRoles",
                        "iam:ListUsers"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJNPP7PPPPMJRV2SA4",
        "PolicyName": "AWSKeyManagementServicePowerUser",
        "UpdateDate": "2015-02-06T18:40:40+00:00",
        "VersionId": "v1"
    },
    "AWSLambdaBasicExecutionRole": {
        "Arn": "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole",
        "AttachmentCount": 0,
        "CreateDate": "2015-04-09T15:03:43+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "logs:CreateLogGroup",
                        "logs:CreateLogStream",
                        "logs:PutLogEvents"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/service-role/",
        "PolicyId": "ANPAJNCQGXC42545SKXIK",
        "PolicyName": "AWSLambdaBasicExecutionRole",
        "UpdateDate": "2015-04-09T15:03:43+00:00",
        "VersionId": "v1"
    },
    "AWSLambdaDynamoDBExecutionRole": {
        "Arn": "arn:aws:iam::aws:policy/service-role/AWSLambdaDynamoDBExecutionRole",
        "AttachmentCount": 0,
        "CreateDate": "2015-04-09T15:09:29+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "dynamodb:DescribeStream",
                        "dynamodb:GetRecords",
                        "dynamodb:GetShardIterator",
                        "dynamodb:ListStreams",
                        "logs:CreateLogGroup",
                        "logs:CreateLogStream",
                        "logs:PutLogEvents"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/service-role/",
        "PolicyId": "ANPAIP7WNAGMIPYNW4WQG",
        "PolicyName": "AWSLambdaDynamoDBExecutionRole",
        "UpdateDate": "2015-04-09T15:09:29+00:00",
        "VersionId": "v1"
    },
    "AWSLambdaExecute": {
        "Arn": "arn:aws:iam::aws:policy/AWSLambdaExecute",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:40:46+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "logs:*"
                    ],
                    "Effect": "Allow",
                    "Resource": "arn:aws:logs:*:*:*"
                },
                {
                    "Action": [
                        "s3:GetObject",
                        "s3:PutObject"
                    ],
                    "Effect": "Allow",
                    "Resource": "arn:aws:s3:::*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJE5FX7FQZSU5XAKGO",
        "PolicyName": "AWSLambdaExecute",
        "UpdateDate": "2015-02-06T18:40:46+00:00",
        "VersionId": "v1"
    },
    "AWSLambdaFullAccess": {
        "Arn": "arn:aws:iam::aws:policy/AWSLambdaFullAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-10-08T16:15:10+00:00",
        "DefaultVersionId": "v3",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "cloudwatch:*",
                        "cognito-identity:ListIdentityPools",
                        "cognito-sync:GetCognitoEvents",
                        "cognito-sync:SetCognitoEvents",
                        "dynamodb:*",
                        "events:*",
                        "iam:ListAttachedRolePolicies",
                        "iam:ListRolePolicies",
                        "iam:ListRoles",
                        "iam:PassRole",
                        "kinesis:DescribeStream",
                        "kinesis:ListStreams",
                        "kinesis:PutRecord",
                        "lambda:*",
                        "logs:*",
                        "s3:*",
                        "sns:ListSubscriptions",
                        "sns:ListSubscriptionsByTopic",
                        "sns:ListTopics",
                        "sns:Subscribe",
                        "sns:Unsubscribe"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAI6E2CYYMI4XI7AA5K",
        "PolicyName": "AWSLambdaFullAccess",
        "UpdateDate": "2015-10-08T16:15:10+00:00",
        "VersionId": "v3"
    },
    "AWSLambdaInvocation-DynamoDB": {
        "Arn": "arn:aws:iam::aws:policy/AWSLambdaInvocation-DynamoDB",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:40:47+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "lambda:InvokeFunction"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                },
                {
                    "Action": [
                        "dynamodb:DescribeStream",
                        "dynamodb:GetRecords",
                        "dynamodb:GetShardIterator",
                        "dynamodb:ListStreams"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJTHQ3EKCQALQDYG5G",
        "PolicyName": "AWSLambdaInvocation-DynamoDB",
        "UpdateDate": "2015-02-06T18:40:47+00:00",
        "VersionId": "v1"
    },
    "AWSLambdaKinesisExecutionRole": {
        "Arn": "arn:aws:iam::aws:policy/service-role/AWSLambdaKinesisExecutionRole",
        "AttachmentCount": 0,
        "CreateDate": "2015-04-09T15:14:16+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "kinesis:DescribeStream",
                        "kinesis:GetRecords",
                        "kinesis:GetShardIterator",
                        "kinesis:ListStreams",
                        "logs:CreateLogGroup",
                        "logs:CreateLogStream",
                        "logs:PutLogEvents"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/service-role/",
        "PolicyId": "ANPAJHOLKJPXV4GBRMJUQ",
        "PolicyName": "AWSLambdaKinesisExecutionRole",
        "UpdateDate": "2015-04-09T15:14:16+00:00",
        "VersionId": "v1"
    },
    "AWSLambdaReadOnlyAccess": {
        "Arn": "arn:aws:iam::aws:policy/AWSLambdaReadOnlyAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-10-08T16:15:48+00:00",
        "DefaultVersionId": "v3",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "cloudwatch:Describe*",
                        "cloudwatch:Get*",
                        "cloudwatch:List*",
                        "cognito-identity:ListIdentityPools",
                        "cognito-sync:GetCognitoEvents",
                        "dynamodb:BatchGetItem",
                        "dynamodb:DescribeStream",
                        "dynamodb:DescribeTable",
                        "dynamodb:GetItem",
                        "dynamodb:ListStreams",
                        "dynamodb:ListTables",
                        "dynamodb:Query",
                        "dynamodb:Scan",
                        "events:List*",
                        "events:Describe*",
                        "iam:ListRoles",
                        "kinesis:DescribeStream",
                        "kinesis:ListStreams",
                        "lambda:List*",
                        "lambda:Get*",
                        "logs:DescribeMetricFilters",
                        "logs:GetLogEvents",
                        "logs:DescribeLogGroups",
                        "logs:DescribeLogStreams",
                        "s3:Get*",
                        "s3:List*",
                        "sns:ListTopics",
                        "sns:ListSubscriptions",
                        "sns:ListSubscriptionsByTopic"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJLDG7J3CGUHFN4YN6",
        "PolicyName": "AWSLambdaReadOnlyAccess",
        "UpdateDate": "2015-10-08T16:15:48+00:00",
        "VersionId": "v3"
    },
    "AWSLambdaRole": {
        "Arn": "arn:aws:iam::aws:policy/service-role/AWSLambdaRole",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:41:28+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "lambda:InvokeFunction"
                    ],
                    "Effect": "Allow",
                    "Resource": [
                        "*"
                    ]
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/service-role/",
        "PolicyId": "ANPAJX4DPCRGTC4NFDUXI",
        "PolicyName": "AWSLambdaRole",
        "UpdateDate": "2015-02-06T18:41:28+00:00",
        "VersionId": "v1"
    },
    "AWSMarketplaceFullAccess": {
        "Arn": "arn:aws:iam::aws:policy/AWSMarketplaceFullAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-11T17:21:45+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "aws-marketplace:*",
                        "cloudformation:CreateStack",
                        "cloudformation:DescribeStackResource",
                        "cloudformation:DescribeStackResources",
                        "cloudformation:DescribeStacks",
                        "cloudformation:List*",
                        "ec2:AuthorizeSecurityGroupEgress",
                        "ec2:AuthorizeSecurityGroupIngress",
                        "ec2:CreateSecurityGroup",
                        "ec2:CreateTags",
                        "ec2:DescribeAccountAttributes",
                        "ec2:DescribeAddresses",
                        "ec2:DeleteSecurityGroup",
                        "ec2:DescribeAccountAttributes",
                        "ec2:DescribeImages",
                        "ec2:DescribeInstances",
                        "ec2:DescribeKeyPairs",
                        "ec2:DescribeSecurityGroups",
                        "ec2:DescribeSubnets",
                        "ec2:DescribeTags",
                        "ec2:DescribeVpcs",
                        "ec2:RunInstances",
                        "ec2:StartInstances",
                        "ec2:StopInstances",
                        "ec2:TerminateInstances"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAI2DV5ULJSO2FYVPYG",
        "PolicyName": "AWSMarketplaceFullAccess",
        "UpdateDate": "2015-02-11T17:21:45+00:00",
        "VersionId": "v1"
    },
    "AWSMarketplaceManageSubscriptions": {
        "Arn": "arn:aws:iam::aws:policy/AWSMarketplaceManageSubscriptions",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:40:32+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "aws-marketplace:ViewSubscriptions",
                        "aws-marketplace:Subscribe",
                        "aws-marketplace:Unsubscribe"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJRDW2WIFN7QLUAKBQ",
        "PolicyName": "AWSMarketplaceManageSubscriptions",
        "UpdateDate": "2015-02-06T18:40:32+00:00",
        "VersionId": "v1"
    },
    "AWSMarketplaceRead-only": {
        "Arn": "arn:aws:iam::aws:policy/AWSMarketplaceRead-only",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:40:31+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "aws-marketplace:ViewSubscriptions",
                        "ec2:DescribeAccountAttributes",
                        "ec2:DescribeAddresses",
                        "ec2:DescribeImages",
                        "ec2:DescribeInstances",
                        "ec2:DescribeKeyPairs",
                        "ec2:DescribeSecurityGroups",
                        "ec2:DescribeSubnets",
                        "ec2:DescribeVpcs"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJOOM6LETKURTJ3XZ2",
        "PolicyName": "AWSMarketplaceRead-only",
        "UpdateDate": "2015-02-06T18:40:31+00:00",
        "VersionId": "v1"
    },
    "AWSOpsWorksFullAccess": {
        "Arn": "arn:aws:iam::aws:policy/AWSOpsWorksFullAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:40:48+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "opsworks:*",
                        "ec2:DescribeAvailabilityZones",
                        "ec2:DescribeKeyPairs",
                        "ec2:DescribeSecurityGroups",
                        "ec2:DescribeAccountAttributes",
                        "ec2:DescribeAvailabilityZones",
                        "ec2:DescribeSecurityGroups",
                        "ec2:DescribeSubnets",
                        "ec2:DescribeVpcs",
                        "elasticloadbalancing:DescribeInstanceHealth",
                        "elasticloadbalancing:DescribeLoadBalancers",
                        "iam:GetRolePolicy",
                        "iam:ListInstanceProfiles",
                        "iam:ListRoles",
                        "iam:ListUsers",
                        "iam:PassRole"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAICN26VXMXASXKOQCG",
        "PolicyName": "AWSOpsWorksFullAccess",
        "UpdateDate": "2015-02-06T18:40:48+00:00",
        "VersionId": "v1"
    },
    "AWSOpsWorksRegisterCLI": {
        "Arn": "arn:aws:iam::aws:policy/AWSOpsWorksRegisterCLI",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:40:49+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "opsworks:AssignInstance",
                        "opsworks:CreateStack",
                        "opsworks:CreateLayer",
                        "opsworks:DeregisterInstance",
                        "opsworks:DescribeInstances",
                        "opsworks:DescribeStackProvisioningParameters",
                        "opsworks:DescribeStacks",
                        "opsworks:UnassignInstance"
                    ],
                    "Effect": "Allow",
                    "Resource": [
                        "*"
                    ]
                },
                {
                    "Action": [
                        "ec2:DescribeInstances"
                    ],
                    "Effect": "Allow",
                    "Resource": [
                        "*"
                    ]
                },
                {
                    "Action": [
                        "iam:AddUserToGroup",
                        "iam:CreateAccessKey",
                        "iam:CreateGroup",
                        "iam:CreateUser",
                        "iam:ListInstanceProfiles",
                        "iam:PassRole",
                        "iam:PutUserPolicy"
                    ],
                    "Effect": "Allow",
                    "Resource": [
                        "*"
                    ]
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJ3AB5ZBFPCQGTVDU4",
        "PolicyName": "AWSOpsWorksRegisterCLI",
        "UpdateDate": "2015-02-06T18:40:49+00:00",
        "VersionId": "v1"
    },
    "AWSOpsWorksRole": {
        "Arn": "arn:aws:iam::aws:policy/service-role/AWSOpsWorksRole",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:41:27+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "cloudwatch:GetMetricStatistics",
                        "ec2:DescribeAccountAttributes",
                        "ec2:DescribeAvailabilityZones",
                        "ec2:DescribeInstances",
                        "ec2:DescribeKeyPairs",
                        "ec2:DescribeSecurityGroups",
                        "ec2:DescribeSubnets",
                        "ec2:DescribeVpcs",
                        "elasticloadbalancing:DescribeInstanceHealth",
                        "elasticloadbalancing:DescribeLoadBalancers",
                        "iam:GetRolePolicy",
                        "iam:ListInstanceProfiles",
                        "iam:ListRoles",
                        "iam:ListUsers",
                        "iam:PassRole",
                        "opsworks:*",
                        "rds:*"
                    ],
                    "Effect": "Allow",
                    "Resource": [
                        "*"
                    ]
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/service-role/",
        "PolicyId": "ANPAIDUTMOKHJFAPJV45W",
        "PolicyName": "AWSOpsWorksRole",
        "UpdateDate": "2015-02-06T18:41:27+00:00",
        "VersionId": "v1"
    },
    "AWSQuickSightDescribeRDS": {
        "Arn": "arn:aws:iam::aws:policy/service-role/AWSQuickSightDescribeRDS",
        "AttachmentCount": 0,
        "CreateDate": "2015-11-10T23:24:50+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "rds:Describe*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/service-role/",
        "PolicyId": "ANPAJU5J6OAMCJD3OO76O",
        "PolicyName": "AWSQuickSightDescribeRDS",
        "UpdateDate": "2015-11-10T23:24:50+00:00",
        "VersionId": "v1"
    },
    "AWSQuickSightDescribeRedshift": {
        "Arn": "arn:aws:iam::aws:policy/service-role/AWSQuickSightDescribeRedshift",
        "AttachmentCount": 0,
        "CreateDate": "2015-11-10T23:25:01+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "redshift:Describe*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/service-role/",
        "PolicyId": "ANPAJFEM6MLSLTW4ZNBW2",
        "PolicyName": "AWSQuickSightDescribeRedshift",
        "UpdateDate": "2015-11-10T23:25:01+00:00",
        "VersionId": "v1"
    },
    "AWSQuickSightListIAM": {
        "Arn": "arn:aws:iam::aws:policy/service-role/AWSQuickSightListIAM",
        "AttachmentCount": 0,
        "CreateDate": "2015-11-10T23:25:07+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "iam:List*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/service-role/",
        "PolicyId": "ANPAI3CH5UUWZN4EKGILO",
        "PolicyName": "AWSQuickSightListIAM",
        "UpdateDate": "2015-11-10T23:25:07+00:00",
        "VersionId": "v1"
    },
    "AWSStorageGatewayFullAccess": {
        "Arn": "arn:aws:iam::aws:policy/AWSStorageGatewayFullAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:41:09+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "storagegateway:*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                },
                {
                    "Action": [
                        "ec2:DescribeSnapshots",
                        "ec2:DeleteSnapshot"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJG5SSPAVOGK3SIDGU",
        "PolicyName": "AWSStorageGatewayFullAccess",
        "UpdateDate": "2015-02-06T18:41:09+00:00",
        "VersionId": "v1"
    },
    "AWSStorageGatewayReadOnlyAccess": {
        "Arn": "arn:aws:iam::aws:policy/AWSStorageGatewayReadOnlyAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:41:10+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "storagegateway:List*",
                        "storagegateway:Describe*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                },
                {
                    "Action": [
                        "ec2:DescribeSnapshots"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAIFKCTUVOPD5NICXJK",
        "PolicyName": "AWSStorageGatewayReadOnlyAccess",
        "UpdateDate": "2015-02-06T18:41:10+00:00",
        "VersionId": "v1"
    },
    "AWSSupportAccess": {
        "Arn": "arn:aws:iam::aws:policy/AWSSupportAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:41:11+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "support:*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJSNKQX2OW67GF4S7E",
        "PolicyName": "AWSSupportAccess",
        "UpdateDate": "2015-02-06T18:41:11+00:00",
        "VersionId": "v1"
    },
    "AWSWAFFullAccess": {
        "Arn": "arn:aws:iam::aws:policy/AWSWAFFullAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-10-06T20:44:00+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "waf:*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJMIKIAFXZEGOLRH7C",
        "PolicyName": "AWSWAFFullAccess",
        "UpdateDate": "2015-10-06T20:44:00+00:00",
        "VersionId": "v1"
    },
    "AWSWAFReadOnlyAccess": {
        "Arn": "arn:aws:iam::aws:policy/AWSWAFReadOnlyAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-10-06T20:43:45+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "waf:Get*",
                        "waf:List*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAINZVDMX2SBF7EU2OC",
        "PolicyName": "AWSWAFReadOnlyAccess",
        "UpdateDate": "2015-10-06T20:43:45+00:00",
        "VersionId": "v1"
    },
    "AdministratorAccess": {
        "Arn": "arn:aws:iam::aws:policy/AdministratorAccess",
        "AttachmentCount": 2,
        "CreateDate": "2015-02-06T18:39:46+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": "*",
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAIWMBCKSKIEE64ZLYK",
        "PolicyName": "AdministratorAccess",
        "UpdateDate": "2015-02-06T18:39:46+00:00",
        "VersionId": "v1"
    },
    "AmazonAPIGatewayAdministrator": {
        "Arn": "arn:aws:iam::aws:policy/AmazonAPIGatewayAdministrator",
        "AttachmentCount": 0,
        "CreateDate": "2015-07-09T17:34:45+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "apigateway:*"
                    ],
                    "Effect": "Allow",
                    "Resource": "arn:aws:apigateway:*::/*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJ4PT6VY5NLKTNUYSI",
        "PolicyName": "AmazonAPIGatewayAdministrator",
        "UpdateDate": "2015-07-09T17:34:45+00:00",
        "VersionId": "v1"
    },
    "AmazonAPIGatewayInvokeFullAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonAPIGatewayInvokeFullAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-07-09T17:36:12+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "execute-api:Invoke"
                    ],
                    "Effect": "Allow",
                    "Resource": "arn:aws:execute-api:*:*:*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAIIWAX2NOOQJ4AIEQ6",
        "PolicyName": "AmazonAPIGatewayInvokeFullAccess",
        "UpdateDate": "2015-07-09T17:36:12+00:00",
        "VersionId": "v1"
    },
    "AmazonAPIGatewayPushToCloudWatchLogs": {
        "Arn": "arn:aws:iam::aws:policy/service-role/AmazonAPIGatewayPushToCloudWatchLogs",
        "AttachmentCount": 0,
        "CreateDate": "2015-11-11T23:41:46+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "logs:CreateLogGroup",
                        "logs:CreateLogStream",
                        "logs:DescribeLogGroups",
                        "logs:DescribeLogStreams",
                        "logs:PutLogEvents",
                        "logs:GetLogEvents",
                        "logs:FilterLogEvents"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/service-role/",
        "PolicyId": "ANPAIK4GFO7HLKYN64ASK",
        "PolicyName": "AmazonAPIGatewayPushToCloudWatchLogs",
        "UpdateDate": "2015-11-11T23:41:46+00:00",
        "VersionId": "v1"
    },
    "AmazonAppStreamFullAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonAppStreamFullAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:40:09+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "appstream:*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJLZZXU2YQVGL4QDNC",
        "PolicyName": "AmazonAppStreamFullAccess",
        "UpdateDate": "2015-02-06T18:40:09+00:00",
        "VersionId": "v1"
    },
    "AmazonAppStreamReadOnlyAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonAppStreamReadOnlyAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:40:10+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "appstream:Get*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJXIFDGB4VBX23DX7K",
        "PolicyName": "AmazonAppStreamReadOnlyAccess",
        "UpdateDate": "2015-02-06T18:40:10+00:00",
        "VersionId": "v1"
    },
    "AmazonCognitoDeveloperAuthenticatedIdentities": {
        "Arn": "arn:aws:iam::aws:policy/AmazonCognitoDeveloperAuthenticatedIdentities",
        "AttachmentCount": 0,
        "CreateDate": "2015-03-24T17:22:23+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "cognito-identity:GetOpenIdTokenForDeveloperIdentity",
                        "cognito-identity:LookupDeveloperIdentity",
                        "cognito-identity:MergeDeveloperIdentities",
                        "cognito-identity:UnlinkDeveloperIdentity"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAIQOKZ5BGKLCMTXH4W",
        "PolicyName": "AmazonCognitoDeveloperAuthenticatedIdentities",
        "UpdateDate": "2015-03-24T17:22:23+00:00",
        "VersionId": "v1"
    },
    "AmazonCognitoPowerUser": {
        "Arn": "arn:aws:iam::aws:policy/AmazonCognitoPowerUser",
        "AttachmentCount": 0,
        "CreateDate": "2015-03-24T17:14:56+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "cognito-identity:*",
                        "cognito-sync:*",
                        "iam:ListRoles",
                        "iam:ListOpenIdConnectProviders",
                        "sns:ListPlatformApplications"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJKW5H2HNCPGCYGR6Y",
        "PolicyName": "AmazonCognitoPowerUser",
        "UpdateDate": "2015-03-24T17:14:56+00:00",
        "VersionId": "v1"
    },
    "AmazonCognitoReadOnly": {
        "Arn": "arn:aws:iam::aws:policy/AmazonCognitoReadOnly",
        "AttachmentCount": 0,
        "CreateDate": "2015-03-24T17:06:46+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "cognito-identity:Describe*",
                        "cognito-identity:Get*",
                        "cognito-identity:List*",
                        "cognito-sync:Describe*",
                        "cognito-sync:Get*",
                        "cognito-sync:List*",
                        "iam:ListOpenIdConnectProviders",
                        "iam:ListRoles",
                        "sns:ListPlatformApplications"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJBFTRZD2GQGJHSVQK",
        "PolicyName": "AmazonCognitoReadOnly",
        "UpdateDate": "2015-03-24T17:06:46+00:00",
        "VersionId": "v1"
    },
    "AmazonDRSVPCManagement": {
        "Arn": "arn:aws:iam::aws:policy/AmazonDRSVPCManagement",
        "AttachmentCount": 0,
        "CreateDate": "2015-09-02T00:09:20+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "ec2:AuthorizeSecurityGroupIngress",
                        "ec2:CreateNetworkInterface",
                        "ec2:CreateSecurityGroup",
                        "ec2:DescribeAvailabilityZones",
                        "ec2:DescribeInternetGateways",
                        "ec2:DescribeSecurityGroups",
                        "ec2:DescribeSubnets",
                        "ec2:DescribeVpcAttribute",
                        "ec2:DescribeVpcs",
                        "ec2:DeleteNetworkInterface",
                        "ec2:DeleteSecurityGroup",
                        "ec2:ModifyNetworkInterfaceAttribute",
                        "ec2:RevokeSecurityGroupIngress"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJPXIBTTZMBEFEX6UA",
        "PolicyName": "AmazonDRSVPCManagement",
        "UpdateDate": "2015-09-02T00:09:20+00:00",
        "VersionId": "v1"
    },
    "AmazonDynamoDBFullAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:40:11+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "dynamodb:*",
                        "cloudwatch:DeleteAlarms",
                        "cloudwatch:DescribeAlarmHistory",
                        "cloudwatch:DescribeAlarms",
                        "cloudwatch:DescribeAlarmsForMetric",
                        "cloudwatch:GetMetricStatistics",
                        "cloudwatch:ListMetrics",
                        "cloudwatch:PutMetricAlarm",
                        "datapipeline:ActivatePipeline",
                        "datapipeline:CreatePipeline",
                        "datapipeline:DeletePipeline",
                        "datapipeline:DescribeObjects",
                        "datapipeline:DescribePipelines",
                        "datapipeline:GetPipelineDefinition",
                        "datapipeline:ListPipelines",
                        "datapipeline:PutPipelineDefinition",
                        "datapipeline:QueryObjects",
                        "iam:ListRoles",
                        "sns:CreateTopic",
                        "sns:DeleteTopic",
                        "sns:ListSubscriptions",
                        "sns:ListSubscriptionsByTopic",
                        "sns:ListTopics",
                        "sns:Subscribe",
                        "sns:Unsubscribe"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAINUGF2JSOSUY76KYA",
        "PolicyName": "AmazonDynamoDBFullAccess",
        "UpdateDate": "2015-02-06T18:40:11+00:00",
        "VersionId": "v1"
    },
    "AmazonDynamoDBFullAccesswithDataPipeline": {
        "Arn": "arn:aws:iam::aws:policy/AmazonDynamoDBFullAccesswithDataPipeline",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:40:14+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "cloudwatch:DeleteAlarms",
                        "cloudwatch:DescribeAlarmHistory",
                        "cloudwatch:DescribeAlarms",
                        "cloudwatch:DescribeAlarmsForMetric",
                        "cloudwatch:GetMetricStatistics",
                        "cloudwatch:ListMetrics",
                        "cloudwatch:PutMetricAlarm",
                        "dynamodb:*",
                        "sns:CreateTopic",
                        "sns:DeleteTopic",
                        "sns:ListSubscriptions",
                        "sns:ListSubscriptionsByTopic",
                        "sns:ListTopics",
                        "sns:Subscribe",
                        "sns:Unsubscribe"
                    ],
                    "Effect": "Allow",
                    "Resource": "*",
                    "Sid": "DDBConsole"
                },
                {
                    "Action": [
                        "datapipeline:*",
                        "iam:ListRoles"
                    ],
                    "Effect": "Allow",
                    "Resource": "*",
                    "Sid": "DDBConsoleImportExport"
                },
                {
                    "Action": [
                        "iam:GetRolePolicy",
                        "iam:PassRole"
                    ],
                    "Effect": "Allow",
                    "Resource": [
                        "*"
                    ],
                    "Sid": "IAMEDPRoles"
                },
                {
                    "Action": [
                        "ec2:CreateTags",
                        "ec2:DescribeInstances",
                        "ec2:RunInstances",
                        "ec2:StartInstances",
                        "ec2:StopInstances",
                        "ec2:TerminateInstances",
                        "elasticmapreduce:*",
                        "datapipeline:*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*",
                    "Sid": "EMR"
                },
                {
                    "Action": [
                        "s3:DeleteObject",
                        "s3:Get*",
                        "s3:List*",
                        "s3:Put*"
                    ],
                    "Effect": "Allow",
                    "Resource": [
                        "*"
                    ],
                    "Sid": "S3"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJ3ORT7KDISSXGHJXA",
        "PolicyName": "AmazonDynamoDBFullAccesswithDataPipeline",
        "UpdateDate": "2015-02-06T18:40:14+00:00",
        "VersionId": "v1"
    },
    "AmazonDynamoDBReadOnlyAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonDynamoDBReadOnlyAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-11-11T23:39:05+00:00",
        "DefaultVersionId": "v2",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "cloudwatch:DescribeAlarmHistory",
                        "cloudwatch:DescribeAlarms",
                        "cloudwatch:DescribeAlarmsForMetric",
                        "cloudwatch:GetMetricStatistics",
                        "cloudwatch:ListMetrics",
                        "datapipeline:DescribeObjects",
                        "datapipeline:DescribePipelines",
                        "datapipeline:GetPipelineDefinition",
                        "datapipeline:ListPipelines",
                        "datapipeline:QueryObjects",
                        "dynamodb:BatchGetItem",
                        "dynamodb:DescribeTable",
                        "dynamodb:GetItem",
                        "dynamodb:ListTables",
                        "dynamodb:Query",
                        "dynamodb:Scan",
                        "dynamodb:DescribeReservedCapacity",
                        "dynamodb:DescribeReservedCapacityOfferings",
                        "sns:ListSubscriptionsByTopic",
                        "sns:ListTopics",
                        "lambda:ListFunctions",
                        "lambda:ListEventSourceMappings",
                        "lambda:GetFunctionConfiguration"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAIY2XFNA232XJ6J7X2",
        "PolicyName": "AmazonDynamoDBReadOnlyAccess",
        "UpdateDate": "2015-11-11T23:39:05+00:00",
        "VersionId": "v2"
    },
    "AmazonEC2ContainerServiceFullAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonEC2ContainerServiceFullAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-04-24T16:54:35+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "ec2:Describe*",
                        "elasticloadbalancing:*",
                        "ecs:*",
                        "iam:ListInstanceProfiles",
                        "iam:ListRoles",
                        "iam:PassRole"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJALOYVTPDZEMIACSM",
        "PolicyName": "AmazonEC2ContainerServiceFullAccess",
        "UpdateDate": "2015-04-24T16:54:35+00:00",
        "VersionId": "v1"
    },
    "AmazonEC2ContainerServiceRole": {
        "Arn": "arn:aws:iam::aws:policy/service-role/AmazonEC2ContainerServiceRole",
        "AttachmentCount": 0,
        "CreateDate": "2015-04-09T16:14:19+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "ec2:AuthorizeSecurityGroupIngress",
                        "ec2:Describe*",
                        "elasticloadbalancing:DeregisterInstancesFromLoadBalancer",
                        "elasticloadbalancing:Describe*",
                        "elasticloadbalancing:RegisterInstancesWithLoadBalancer"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/service-role/",
        "PolicyId": "ANPAJO53W2XHNACG7V77Q",
        "PolicyName": "AmazonEC2ContainerServiceRole",
        "UpdateDate": "2015-04-09T16:14:19+00:00",
        "VersionId": "v1"
    },
    "AmazonEC2ContainerServiceforEC2Role": {
        "Arn": "arn:aws:iam::aws:policy/service-role/AmazonEC2ContainerServiceforEC2Role",
        "AttachmentCount": 0,
        "CreateDate": "2015-08-17T23:33:23+00:00",
        "DefaultVersionId": "v2",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "ecs:CreateCluster",
                        "ecs:DeregisterContainerInstance",
                        "ecs:DiscoverPollEndpoint",
                        "ecs:Poll",
                        "ecs:RegisterContainerInstance",
                        "ecs:StartTelemetrySession",
                        "ecs:Submit*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/service-role/",
        "PolicyId": "ANPAJLYJCVHC7TQHCSQDS",
        "PolicyName": "AmazonEC2ContainerServiceforEC2Role",
        "UpdateDate": "2015-08-17T23:33:23+00:00",
        "VersionId": "v2"
    },
    "AmazonEC2FullAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonEC2FullAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:40:15+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": "ec2:*",
                    "Effect": "Allow",
                    "Resource": "*"
                },
                {
                    "Action": "elasticloadbalancing:*",
                    "Effect": "Allow",
                    "Resource": "*"
                },
                {
                    "Action": "cloudwatch:*",
                    "Effect": "Allow",
                    "Resource": "*"
                },
                {
                    "Action": "autoscaling:*",
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAI3VAJF5ZCRZ7MCQE6",
        "PolicyName": "AmazonEC2FullAccess",
        "UpdateDate": "2015-02-06T18:40:15+00:00",
        "VersionId": "v1"
    },
    "AmazonEC2ReadOnlyAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess",
        "AttachmentCount": 1,
        "CreateDate": "2015-02-06T18:40:17+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": "ec2:Describe*",
                    "Effect": "Allow",
                    "Resource": "*"
                },
                {
                    "Action": "elasticloadbalancing:Describe*",
                    "Effect": "Allow",
                    "Resource": "*"
                },
                {
                    "Action": [
                        "cloudwatch:ListMetrics",
                        "cloudwatch:GetMetricStatistics",
                        "cloudwatch:Describe*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                },
                {
                    "Action": "autoscaling:Describe*",
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAIGDT4SV4GSETWTBZK",
        "PolicyName": "AmazonEC2ReadOnlyAccess",
        "UpdateDate": "2015-02-06T18:40:17+00:00",
        "VersionId": "v1"
    },
    "AmazonEC2ReportsAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonEC2ReportsAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:40:16+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": "ec2-reports:*",
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAIU6NBZVF2PCRW36ZW",
        "PolicyName": "AmazonEC2ReportsAccess",
        "UpdateDate": "2015-02-06T18:40:16+00:00",
        "VersionId": "v1"
    },
    "AmazonEC2RoleforAWSCodeDeploy": {
        "Arn": "arn:aws:iam::aws:policy/service-role/AmazonEC2RoleforAWSCodeDeploy",
        "AttachmentCount": 0,
        "CreateDate": "2015-05-19T18:10:14+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "s3:GetObject",
                        "s3:GetObjectVersion",
                        "s3:ListObjects"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/service-role/",
        "PolicyId": "ANPAIAZKXZ27TAJ4PVWGK",
        "PolicyName": "AmazonEC2RoleforAWSCodeDeploy",
        "UpdateDate": "2015-05-19T18:10:14+00:00",
        "VersionId": "v1"
    },
    "AmazonEC2RoleforDataPipelineRole": {
        "Arn": "arn:aws:iam::aws:policy/service-role/AmazonEC2RoleforDataPipelineRole",
        "AttachmentCount": 0,
        "CreateDate": "2015-03-19T19:18:17+00:00",
        "DefaultVersionId": "v2",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "cloudwatch:*",
                        "datapipeline:*",
                        "dynamodb:*",
                        "ec2:Describe*",
                        "elasticmapreduce:AddJobFlowSteps",
                        "elasticmapreduce:Describe*",
                        "elasticmapreduce:ListInstance*",
                        "rds:Describe*",
                        "redshift:DescribeClusters",
                        "redshift:DescribeClusterSecurityGroups",
                        "s3:*",
                        "sdb:*",
                        "sns:*",
                        "sqs:*"
                    ],
                    "Effect": "Allow",
                    "Resource": [
                        "*"
                    ]
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/service-role/",
        "PolicyId": "ANPAJ3Z5I2WAJE5DN2J36",
        "PolicyName": "AmazonEC2RoleforDataPipelineRole",
        "UpdateDate": "2015-03-19T19:21:14+00:00",
        "VersionId": "v2"
    },
    "AmazonEC2RoleforSSM": {
        "Arn": "arn:aws:iam::aws:policy/service-role/AmazonEC2RoleforSSM",
        "AttachmentCount": 0,
        "CreateDate": "2015-10-23T22:12:37+00:00",
        "DefaultVersionId": "v2",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "ssm:DescribeAssociation",
                        "ssm:GetDocument",
                        "ssm:ListAssociations",
                        "ssm:UpdateAssociationStatus",
                        "ssm:UpdateInstanceInformation"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                },
                {
                    "Action": [
                        "ec2messages:AcknowledgeMessage",
                        "ec2messages:DeleteMessage",
                        "ec2messages:FailMessage",
                        "ec2messages:GetEndpoint",
                        "ec2messages:GetMessages",
                        "ec2messages:SendReply"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                },
                {
                    "Action": [
                        "cloudwatch:PutMetricData"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                },
                {
                    "Action": [
                        "ec2:DescribeInstanceStatus"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                },
                {
                    "Action": [
                        "ds:CreateComputer",
                        "ds:DescribeDirectories"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                },
                {
                    "Action": [
                        "logs:CreateLogGroup",
                        "logs:CreateLogStream",
                        "logs:DescribeLogGroups",
                        "logs:DescribeLogStreams",
                        "logs:PutLogEvents"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                },
                {
                    "Action": [
                        "s3:PutObject",
                        "s3:GetObject",
                        "s3:AbortMultipartUpload",
                        "s3:ListMultipartUploadParts",
                        "s3:ListBucketMultipartUploads"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/service-role/",
        "PolicyId": "ANPAI6TL3SMY22S4KMMX6",
        "PolicyName": "AmazonEC2RoleforSSM",
        "UpdateDate": "2015-10-23T22:12:37+00:00",
        "VersionId": "v2"
    },
    "AmazonEC2SpotFleetRole": {
        "Arn": "arn:aws:iam::aws:policy/service-role/AmazonEC2SpotFleetRole",
        "AttachmentCount": 0,
        "CreateDate": "2015-10-19T20:24:16+00:00",
        "DefaultVersionId": "v2",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "ec2:DescribeImages",
                        "ec2:DescribeSubnets",
                        "ec2:RequestSpotInstances",
                        "ec2:TerminateInstances",
                        "iam:PassRole"
                    ],
                    "Effect": "Allow",
                    "Resource": [
                        "*"
                    ]
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/service-role/",
        "PolicyId": "ANPAIMRTKHWK7ESSNETSW",
        "PolicyName": "AmazonEC2SpotFleetRole",
        "UpdateDate": "2015-10-19T20:24:16+00:00",
        "VersionId": "v2"
    },
    "AmazonESFullAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonESFullAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-10-01T19:14:00+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "es:*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJM6ZTCU24QL5PZCGC",
        "PolicyName": "AmazonESFullAccess",
        "UpdateDate": "2015-10-01T19:14:00+00:00",
        "VersionId": "v1"
    },
    "AmazonESReadOnlyAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonESReadOnlyAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-10-01T19:18:24+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "es:Describe*",
                        "es:List*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJUDMRLOQ7FPAR46FQ",
        "PolicyName": "AmazonESReadOnlyAccess",
        "UpdateDate": "2015-10-01T19:18:24+00:00",
        "VersionId": "v1"
    },
    "AmazonElastiCacheFullAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonElastiCacheFullAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:40:20+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": "elasticache:*",
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAIA2V44CPHAUAAECKG",
        "PolicyName": "AmazonElastiCacheFullAccess",
        "UpdateDate": "2015-02-06T18:40:20+00:00",
        "VersionId": "v1"
    },
    "AmazonElastiCacheReadOnlyAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonElastiCacheReadOnlyAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:40:21+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "elasticache:Describe*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAIPDACSNQHSENWAKM2",
        "PolicyName": "AmazonElastiCacheReadOnlyAccess",
        "UpdateDate": "2015-02-06T18:40:21+00:00",
        "VersionId": "v1"
    },
    "AmazonElasticFileSystemFullAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonElasticFileSystemFullAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-05-27T16:22:28+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "ec2:CreateNetworkInterface",
                        "ec2:DeleteNetworkInterface",
                        "ec2:DescribeAvailabilityZones",
                        "ec2:DescribeNetworkInterfaceAttribute",
                        "ec2:DescribeNetworkInterfaces",
                        "ec2:DescribeSecurityGroups",
                        "ec2:DescribeSubnets",
                        "ec2:DescribeVpcs",
                        "ec2:ModifyNetworkInterfaceAttribute",
                        "elasticfilesystem:*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJKXTMNVQGIDNCKPBC",
        "PolicyName": "AmazonElasticFileSystemFullAccess",
        "UpdateDate": "2015-05-27T16:22:28+00:00",
        "VersionId": "v1"
    },
    "AmazonElasticFileSystemReadOnlyAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonElasticFileSystemReadOnlyAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-05-27T16:25:25+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "ec2:DescribeAvailabilityZones",
                        "ec2:DescribeNetworkInterfaceAttribute",
                        "ec2:DescribeNetworkInterfaces",
                        "ec2:DescribeSecurityGroups",
                        "ec2:DescribeSubnets",
                        "ec2:DescribeVpcs",
                        "elasticfilesystem:Describe*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAIPN5S4NE5JJOKVC4Y",
        "PolicyName": "AmazonElasticFileSystemReadOnlyAccess",
        "UpdateDate": "2015-05-27T16:25:25+00:00",
        "VersionId": "v1"
    },
    "AmazonElasticMapReduceFullAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonElasticMapReduceFullAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-05-21T17:13:51+00:00",
        "DefaultVersionId": "v3",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "cloudwatch:*",
                        "ec2:AuthorizeSecurityGroupIngress",
                        "ec2:CancelSpotInstanceRequests",
                        "ec2:CreateSecurityGroup",
                        "ec2:CreateTags",
                        "ec2:DeleteTags",
                        "ec2:DescribeAvailabilityZones",
                        "ec2:DescribeAccountAttributes",
                        "ec2:DescribeInstances",
                        "ec2:DescribeKeyPairs",
                        "ec2:DescribeRouteTables",
                        "ec2:DescribeSecurityGroups",
                        "ec2:DescribeSpotInstanceRequests",
                        "ec2:DescribeSpotPriceHistory",
                        "ec2:DescribeSubnets",
                        "ec2:DescribeVpcAttribute",
                        "ec2:DescribeVpcs",
                        "ec2:ModifyImageAttribute",
                        "ec2:ModifyInstanceAttribute",
                        "ec2:RequestSpotInstances",
                        "ec2:RunInstances",
                        "ec2:TerminateInstances",
                        "elasticmapreduce:*",
                        "iam:GetPolicy",
                        "iam:GetPolicyVersion",
                        "iam:ListRoles",
                        "iam:PassRole",
                        "kms:List*",
                        "s3:*",
                        "sdb:*",
                        "support:CreateCase",
                        "support:DescribeServices",
                        "support:DescribeSeverityLevels"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAIZP5JFP3AMSGINBB2",
        "PolicyName": "AmazonElasticMapReduceFullAccess",
        "UpdateDate": "2015-05-21T17:16:31+00:00",
        "VersionId": "v3"
    },
    "AmazonElasticMapReduceReadOnlyAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonElasticMapReduceReadOnlyAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:40:23+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "elasticmapreduce:Describe*",
                        "elasticmapreduce:List*",
                        "s3:GetObject",
                        "s3:ListAllMyBuckets",
                        "s3:ListBucket",
                        "sdb:Select",
                        "cloudwatch:GetMetricStatistics"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAIHP6NH2S6GYFCOINC",
        "PolicyName": "AmazonElasticMapReduceReadOnlyAccess",
        "UpdateDate": "2015-02-06T18:40:23+00:00",
        "VersionId": "v1"
    },
    "AmazonElasticMapReduceRole": {
        "Arn": "arn:aws:iam::aws:policy/service-role/AmazonElasticMapReduceRole",
        "AttachmentCount": 0,
        "CreateDate": "2015-10-28T17:24:04+00:00",
        "DefaultVersionId": "v3",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "ec2:AuthorizeSecurityGroupIngress",
                        "ec2:CancelSpotInstanceRequests",
                        "ec2:CreateSecurityGroup",
                        "ec2:CreateTags",
                        "ec2:DeleteTags",
                        "ec2:DescribeAvailabilityZones",
                        "ec2:DescribeAccountAttributes",
                        "ec2:DescribeInstances",
                        "ec2:DescribeInstanceStatus",
                        "ec2:DescribeKeyPairs",
                        "ec2:DescribePrefixLists",
                        "ec2:DescribeRouteTables",
                        "ec2:DescribeSecurityGroups",
                        "ec2:DescribeSpotInstanceRequests",
                        "ec2:DescribeSpotPriceHistory",
                        "ec2:DescribeSubnets",
                        "ec2:DescribeVpcAttribute",
                        "ec2:DescribeVpcEndpoints",
                        "ec2:DescribeVpcEndpointServices",
                        "ec2:DescribeVpcs",
                        "ec2:ModifyImageAttribute",
                        "ec2:ModifyInstanceAttribute",
                        "ec2:RequestSpotInstances",
                        "ec2:RunInstances",
                        "ec2:TerminateInstances",
                        "iam:GetRole",
                        "iam:GetRolePolicy",
                        "iam:ListInstanceProfiles",
                        "iam:ListRolePolicies",
                        "iam:PassRole",
                        "s3:CreateBucket",
                        "s3:Get*",
                        "s3:List*",
                        "sdb:BatchPutAttributes",
                        "sdb:Select",
                        "sqs:CreateQueue",
                        "sqs:Delete*",
                        "sqs:GetQueue*",
                        "sqs:PurgeQueue",
                        "sqs:ReceiveMessage"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/service-role/",
        "PolicyId": "ANPAIDI2BQT2LKXZG36TW",
        "PolicyName": "AmazonElasticMapReduceRole",
        "UpdateDate": "2015-10-28T17:24:04+00:00",
        "VersionId": "v3"
    },
    "AmazonElasticMapReduceforEC2Role": {
        "Arn": "arn:aws:iam::aws:policy/service-role/AmazonElasticMapReduceforEC2Role",
        "AttachmentCount": 0,
        "CreateDate": "2015-05-13T21:23:05+00:00",
        "DefaultVersionId": "v2",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "cloudwatch:*",
                        "dynamodb:*",
                        "ec2:Describe*",
                        "elasticmapreduce:Describe*",
                        "elasticmapreduce:ListBootstrapActions",
                        "elasticmapreduce:ListClusters",
                        "elasticmapreduce:ListInstanceGroups",
                        "elasticmapreduce:ListInstances",
                        "elasticmapreduce:ListSteps",
                        "kinesis:CreateStream",
                        "kinesis:DeleteStream",
                        "kinesis:DescribeStream",
                        "kinesis:GetRecords",
                        "kinesis:GetShardIterator",
                        "kinesis:MergeShards",
                        "kinesis:PutRecord",
                        "kinesis:SplitShard",
                        "rds:Describe*",
                        "s3:*",
                        "sdb:*",
                        "sns:*",
                        "sqs:*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/service-role/",
        "PolicyId": "ANPAIGALS5RCDLZLB3PGS",
        "PolicyName": "AmazonElasticMapReduceforEC2Role",
        "UpdateDate": "2015-05-13T21:27:21+00:00",
        "VersionId": "v2"
    },
    "AmazonElasticTranscoderFullAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonElasticTranscoderFullAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:40:24+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "elastictranscoder:*",
                        "cloudfront:*",
                        "s3:List*",
                        "s3:Put*",
                        "s3:Get*",
                        "s3:*MultipartUpload*",
                        "iam:CreateRole",
                        "iam:GetRolePolicy",
                        "iam:PassRole",
                        "iam:PutRolePolicy",
                        "iam:List*",
                        "sns:CreateTopic",
                        "sns:List*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJ4D5OJU75P5ZJZVNY",
        "PolicyName": "AmazonElasticTranscoderFullAccess",
        "UpdateDate": "2015-02-06T18:40:24+00:00",
        "VersionId": "v1"
    },
    "AmazonElasticTranscoderJobsSubmitter": {
        "Arn": "arn:aws:iam::aws:policy/AmazonElasticTranscoderJobsSubmitter",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:40:25+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "elastictranscoder:Read*",
                        "elastictranscoder:List*",
                        "elastictranscoder:*Job",
                        "elastictranscoder:*Preset",
                        "s3:List*",
                        "iam:List*",
                        "sns:List*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAIN5WGARIKZ3E2UQOU",
        "PolicyName": "AmazonElasticTranscoderJobsSubmitter",
        "UpdateDate": "2015-02-06T18:40:25+00:00",
        "VersionId": "v1"
    },
    "AmazonElasticTranscoderReadOnlyAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonElasticTranscoderReadOnlyAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:40:26+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "elastictranscoder:Read*",
                        "elastictranscoder:List*",
                        "s3:List*",
                        "iam:List*",
                        "sns:List*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJGPP7GPMJRRJMEP3Q",
        "PolicyName": "AmazonElasticTranscoderReadOnlyAccess",
        "UpdateDate": "2015-02-06T18:40:26+00:00",
        "VersionId": "v1"
    },
    "AmazonElasticTranscoderRole": {
        "Arn": "arn:aws:iam::aws:policy/service-role/AmazonElasticTranscoderRole",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:41:26+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "s3:ListBucket",
                        "s3:Put*",
                        "s3:Get*",
                        "s3:*MultipartUpload*"
                    ],
                    "Effect": "Allow",
                    "Resource": [
                        "*"
                    ],
                    "Sid": "1"
                },
                {
                    "Action": [
                        "sns:Publish"
                    ],
                    "Effect": "Allow",
                    "Resource": [
                        "*"
                    ],
                    "Sid": "2"
                },
                {
                    "Action": [
                        "s3:*Policy*",
                        "sns:*Permission*",
                        "sns:*Delete*",
                        "s3:*Delete*",
                        "sns:*Remove*"
                    ],
                    "Effect": "Deny",
                    "Resource": [
                        "*"
                    ],
                    "Sid": "3"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/service-role/",
        "PolicyId": "ANPAJNW3WMKVXFJ2KPIQ2",
        "PolicyName": "AmazonElasticTranscoderRole",
        "UpdateDate": "2015-02-06T18:41:26+00:00",
        "VersionId": "v1"
    },
    "AmazonGlacierFullAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonGlacierFullAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:40:28+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": "glacier:*",
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJQSTZJWB2AXXAKHVQ",
        "PolicyName": "AmazonGlacierFullAccess",
        "UpdateDate": "2015-02-06T18:40:28+00:00",
        "VersionId": "v1"
    },
    "AmazonGlacierReadOnlyAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonGlacierReadOnlyAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:40:27+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "glacier:ListVaults",
                        "glacier:DescribeVault",
                        "glacier:GetVaultNotifications",
                        "glacier:ListJobs",
                        "glacier:DescribeJob",
                        "glacier:GetJobOutput"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAI2D5NJKMU274MET4E",
        "PolicyName": "AmazonGlacierReadOnlyAccess",
        "UpdateDate": "2015-02-06T18:40:27+00:00",
        "VersionId": "v1"
    },
    "AmazonInspectorFullAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonInspectorFullAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-10-07T17:08:04+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "inspector:*",
                        "ec2:DescribeInstances",
                        "ec2:DescribeTags"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAI7Y6NTA27NWNA5U5E",
        "PolicyName": "AmazonInspectorFullAccess",
        "UpdateDate": "2015-10-07T17:08:04+00:00",
        "VersionId": "v1"
    },
    "AmazonInspectorReadOnlyAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonInspectorReadOnlyAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-10-07T17:08:01+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "inspector:Describe*",
                        "inspector:Get*",
                        "inspector:List*",
                        "inspector:LocalizeText",
                        "inspector:Preview*",
                        "ec2:DescribeInstances",
                        "ec2:DescribeTags"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJXQNTHTEJ2JFRN2SE",
        "PolicyName": "AmazonInspectorReadOnlyAccess",
        "UpdateDate": "2015-10-07T17:08:01+00:00",
        "VersionId": "v1"
    },
    "AmazonKinesisFirehoseFullAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonKinesisFirehoseFullAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-10-07T18:45:26+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "firehose:*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJMZQMTZ7FRBFHHAHI",
        "PolicyName": "AmazonKinesisFirehoseFullAccess",
        "UpdateDate": "2015-10-07T18:45:26+00:00",
        "VersionId": "v1"
    },
    "AmazonKinesisFirehoseReadOnlyAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonKinesisFirehoseReadOnlyAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-10-07T18:43:39+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "firehose:Describe*",
                        "firehose:List*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJ36NT645INW4K24W6",
        "PolicyName": "AmazonKinesisFirehoseReadOnlyAccess",
        "UpdateDate": "2015-10-07T18:43:39+00:00",
        "VersionId": "v1"
    },
    "AmazonKinesisFullAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonKinesisFullAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:40:29+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": "kinesis:*",
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAIVF32HAMOXCUYRAYE",
        "PolicyName": "AmazonKinesisFullAccess",
        "UpdateDate": "2015-02-06T18:40:29+00:00",
        "VersionId": "v1"
    },
    "AmazonKinesisReadOnlyAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonKinesisReadOnlyAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:40:30+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "kinesis:Get*",
                        "kinesis:List*",
                        "kinesis:Describe*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAIOCMTDT5RLKZ2CAJO",
        "PolicyName": "AmazonKinesisReadOnlyAccess",
        "UpdateDate": "2015-02-06T18:40:30+00:00",
        "VersionId": "v1"
    },
    "AmazonMachineLearningBatchPredictionsAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonMachineLearningBatchPredictionsAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-04-09T17:12:19+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "machinelearning:CreateBatchPrediction",
                        "machinelearning:DeleteBatchPrediction",
                        "machinelearning:DescribeBatchPredictions",
                        "machinelearning:GetBatchPrediction",
                        "machinelearning:UpdateBatchPrediction"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAILOI4HTQSFTF3GQSC",
        "PolicyName": "AmazonMachineLearningBatchPredictionsAccess",
        "UpdateDate": "2015-04-09T17:12:19+00:00",
        "VersionId": "v1"
    },
    "AmazonMachineLearningCreateOnlyAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonMachineLearningCreateOnlyAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-04-09T17:18:09+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "machinelearning:Create*",
                        "machinelearning:Delete*",
                        "machinelearning:Describe*",
                        "machinelearning:Get*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJDRUNIC2RYAMAT3CK",
        "PolicyName": "AmazonMachineLearningCreateOnlyAccess",
        "UpdateDate": "2015-04-09T17:18:09+00:00",
        "VersionId": "v1"
    },
    "AmazonMachineLearningFullAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonMachineLearningFullAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-04-09T17:25:41+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "machinelearning:*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAIWKW6AGSGYOQ5ERHC",
        "PolicyName": "AmazonMachineLearningFullAccess",
        "UpdateDate": "2015-04-09T17:25:41+00:00",
        "VersionId": "v1"
    },
    "AmazonMachineLearningManageRealTimeEndpointOnlyAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonMachineLearningManageRealTimeEndpointOnlyAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-04-09T17:32:41+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "machinelearning:CreateRealtimeEndpoint",
                        "machinelearning:DeleteRealtimeEndpoint"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJJL3PC3VCSVZP6OCI",
        "PolicyName": "AmazonMachineLearningManageRealTimeEndpointOnlyAccess",
        "UpdateDate": "2015-04-09T17:32:41+00:00",
        "VersionId": "v1"
    },
    "AmazonMachineLearningReadOnlyAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonMachineLearningReadOnlyAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-04-09T17:40:02+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "machinelearning:Describe*",
                        "machinelearning:Get*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAIW5VYBCGEX56JCINC",
        "PolicyName": "AmazonMachineLearningReadOnlyAccess",
        "UpdateDate": "2015-04-09T17:40:02+00:00",
        "VersionId": "v1"
    },
    "AmazonMachineLearningRealTimePredictionOnlyAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonMachineLearningRealTimePredictionOnlyAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-04-09T17:44:06+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "machinelearning:Predict"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAIWMCNQPRWMWT36GVQ",
        "PolicyName": "AmazonMachineLearningRealTimePredictionOnlyAccess",
        "UpdateDate": "2015-04-09T17:44:06+00:00",
        "VersionId": "v1"
    },
    "AmazonMachineLearningRoleforRedshiftDataSource": {
        "Arn": "arn:aws:iam::aws:policy/service-role/AmazonMachineLearningRoleforRedshiftDataSource",
        "AttachmentCount": 0,
        "CreateDate": "2015-04-09T17:05:26+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "ec2:AuthorizeSecurityGroupIngress",
                        "ec2:CreateSecurityGroup",
                        "ec2:DescribeInternetGateways",
                        "ec2:DescribeSecurityGroups",
                        "ec2:RevokeSecurityGroupIngress",
                        "redshift:AuthorizeClusterSecurityGroupIngress",
                        "redshift:CreateClusterSecurityGroup",
                        "redshift:DescribeClusters",
                        "redshift:DescribeClusterSecurityGroups",
                        "redshift:ModifyCluster",
                        "redshift:RevokeClusterSecurityGroupIngress",
                        "s3:GetBucketLocation",
                        "s3:GetBucketPolicy",
                        "s3:GetObject",
                        "s3:PutBucketPolicy",
                        "s3:PutObject"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/service-role/",
        "PolicyId": "ANPAIQ5UDYYMNN42BM4AK",
        "PolicyName": "AmazonMachineLearningRoleforRedshiftDataSource",
        "UpdateDate": "2015-04-09T17:05:26+00:00",
        "VersionId": "v1"
    },
    "AmazonMobileAnalyticsFinancialReportAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonMobileAnalyticsFinancialReportAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:40:35+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "mobileanalytics:GetReports",
                        "mobileanalytics:GetFinancialReports"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJKJHO2R27TXKCWBU4",
        "PolicyName": "AmazonMobileAnalyticsFinancialReportAccess",
        "UpdateDate": "2015-02-06T18:40:35+00:00",
        "VersionId": "v1"
    },
    "AmazonMobileAnalyticsFullAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonMobileAnalyticsFullAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:40:34+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": "mobileanalytics:*",
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAIJIKLU2IJ7WJ6DZFG",
        "PolicyName": "AmazonMobileAnalyticsFullAccess",
        "UpdateDate": "2015-02-06T18:40:34+00:00",
        "VersionId": "v1"
    },
    "AmazonMobileAnalyticsNon-financialReportAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonMobileAnalyticsNon-financialReportAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:40:36+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": "mobileanalytics:GetReports",
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAIQLKQ4RXPUBBVVRDE",
        "PolicyName": "AmazonMobileAnalyticsNon-financialReportAccess",
        "UpdateDate": "2015-02-06T18:40:36+00:00",
        "VersionId": "v1"
    },
    "AmazonMobileAnalyticsWriteOnlyAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonMobileAnalyticsWriteOnlyAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:40:37+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": "mobileanalytics:PutEvents",
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJ5TAWBBQC2FAL3G6G",
        "PolicyName": "AmazonMobileAnalyticsWriteOnlyAccess",
        "UpdateDate": "2015-02-06T18:40:37+00:00",
        "VersionId": "v1"
    },
    "AmazonRDSEnhancedMonitoringRole": {
        "Arn": "arn:aws:iam::aws:policy/service-role/AmazonRDSEnhancedMonitoringRole",
        "AttachmentCount": 0,
        "CreateDate": "2015-11-11T19:58:29+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "logs:CreateLogGroup",
                        "logs:PutRetentionPolicy"
                    ],
                    "Effect": "Allow",
                    "Resource": [
                        "arn:aws:logs:*:*:log-group:RDS*"
                    ],
                    "Sid": "EnableCreationAndManagementOfRDSCloudwatchLogGroups"
                },
                {
                    "Action": [
                        "logs:CreateLogStream",
                        "logs:PutLogEvents",
                        "logs:DescribeLogStreams",
                        "logs:GetLogEvents"
                    ],
                    "Effect": "Allow",
                    "Resource": [
                        "arn:aws:logs:*:*:log-group:RDS*:log-stream:*"
                    ],
                    "Sid": "EnableCreationAndManagementOfRDSCloudwatchLogStreams"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/service-role/",
        "PolicyId": "ANPAJV7BS425S4PTSSVGK",
        "PolicyName": "AmazonRDSEnhancedMonitoringRole",
        "UpdateDate": "2015-11-11T19:58:29+00:00",
        "VersionId": "v1"
    },
    "AmazonRDSFullAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonRDSFullAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:40:52+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "rds:*",
                        "cloudwatch:DescribeAlarms",
                        "cloudwatch:GetMetricStatistics",
                        "ec2:DescribeAccountAttributes",
                        "ec2:DescribeAvailabilityZones",
                        "ec2:DescribeSecurityGroups",
                        "ec2:DescribeSubnets",
                        "ec2:DescribeVpcs",
                        "sns:ListSubscriptions",
                        "sns:ListTopics"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAI3R4QMOG6Q5A4VWVG",
        "PolicyName": "AmazonRDSFullAccess",
        "UpdateDate": "2015-02-06T18:40:52+00:00",
        "VersionId": "v1"
    },
    "AmazonRDSReadOnlyAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonRDSReadOnlyAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:40:53+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "rds:Describe*",
                        "rds:ListTagsForResource",
                        "ec2:DescribeAccountAttributes",
                        "ec2:DescribeAvailabilityZones",
                        "ec2:DescribeSecurityGroups",
                        "ec2:DescribeVpcs"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                },
                {
                    "Action": [
                        "cloudwatch:GetMetricStatistics"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJKTTTYV2IIHKLZ346",
        "PolicyName": "AmazonRDSReadOnlyAccess",
        "UpdateDate": "2015-02-06T18:40:53+00:00",
        "VersionId": "v1"
    },
    "AmazonRedshiftFullAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonRedshiftFullAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:40:50+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "redshift:*",
                        "ec2:DescribeAccountAttributes",
                        "ec2:DescribeAddresses",
                        "ec2:DescribeAvailabilityZones",
                        "ec2:DescribeSecurityGroups",
                        "ec2:DescribeSubnets",
                        "ec2:DescribeVpcs",
                        "ec2:DescribeInternetGateways",
                        "sns:CreateTopic",
                        "sns:Get*",
                        "sns:List*",
                        "cloudwatch:Describe*",
                        "cloudwatch:Get*",
                        "cloudwatch:List*",
                        "cloudwatch:PutMetricAlarm",
                        "cloudwatch:EnableAlarmActions",
                        "cloudwatch:DisableAlarmActions"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAISEKCHH4YDB46B5ZO",
        "PolicyName": "AmazonRedshiftFullAccess",
        "UpdateDate": "2015-02-06T18:40:50+00:00",
        "VersionId": "v1"
    },
    "AmazonRedshiftReadOnlyAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonRedshiftReadOnlyAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:40:51+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "redshift:Describe*",
                        "redshift:ViewQueriesInConsole",
                        "ec2:DescribeAccountAttributes",
                        "ec2:DescribeAddresses",
                        "ec2:DescribeAvailabilityZones",
                        "ec2:DescribeSecurityGroups",
                        "ec2:DescribeSubnets",
                        "ec2:DescribeVpcs",
                        "ec2:DescribeInternetGateways",
                        "sns:Get*",
                        "sns:List*",
                        "cloudwatch:Describe*",
                        "cloudwatch:List*",
                        "cloudwatch:Get*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAIGD46KSON64QBSEZM",
        "PolicyName": "AmazonRedshiftReadOnlyAccess",
        "UpdateDate": "2015-02-06T18:40:51+00:00",
        "VersionId": "v1"
    },
    "AmazonRoute53DomainsFullAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonRoute53DomainsFullAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:40:56+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "route53:CreateHostedZone",
                        "route53domains:*"
                    ],
                    "Effect": "Allow",
                    "Resource": [
                        "*"
                    ]
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAIPAFBMIYUILMOKL6G",
        "PolicyName": "AmazonRoute53DomainsFullAccess",
        "UpdateDate": "2015-02-06T18:40:56+00:00",
        "VersionId": "v1"
    },
    "AmazonRoute53DomainsReadOnlyAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonRoute53DomainsReadOnlyAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:40:57+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "route53domains:Get*",
                        "route53domains:List*"
                    ],
                    "Effect": "Allow",
                    "Resource": [
                        "*"
                    ]
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAIDRINP6PPTRXYVQCI",
        "PolicyName": "AmazonRoute53DomainsReadOnlyAccess",
        "UpdateDate": "2015-02-06T18:40:57+00:00",
        "VersionId": "v1"
    },
    "AmazonRoute53FullAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonRoute53FullAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:40:54+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "route53:*"
                    ],
                    "Effect": "Allow",
                    "Resource": [
                        "*"
                    ]
                },
                {
                    "Action": [
                        "elasticloadbalancing:DescribeLoadBalancers"
                    ],
                    "Effect": "Allow",
                    "Resource": [
                        "*"
                    ]
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJWVDLG5RPST6PHQ3A",
        "PolicyName": "AmazonRoute53FullAccess",
        "UpdateDate": "2015-02-06T18:40:54+00:00",
        "VersionId": "v1"
    },
    "AmazonRoute53ReadOnlyAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonRoute53ReadOnlyAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:40:55+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "route53:Get*",
                        "route53:List*"
                    ],
                    "Effect": "Allow",
                    "Resource": [
                        "*"
                    ]
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAITOYK2ZAOQFXV2JNC",
        "PolicyName": "AmazonRoute53ReadOnlyAccess",
        "UpdateDate": "2015-02-06T18:40:55+00:00",
        "VersionId": "v1"
    },
    "AmazonS3FullAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonS3FullAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:40:58+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": "s3:*",
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAIFIR6V6BVTRAHWINE",
        "PolicyName": "AmazonS3FullAccess",
        "UpdateDate": "2015-02-06T18:40:58+00:00",
        "VersionId": "v1"
    },
    "AmazonS3ReadOnlyAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:40:59+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "s3:Get*",
                        "s3:List*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAIZTJ4DXE7G6AGAE6M",
        "PolicyName": "AmazonS3ReadOnlyAccess",
        "UpdateDate": "2015-02-06T18:40:59+00:00",
        "VersionId": "v1"
    },
    "AmazonSESFullAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonSESFullAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:41:02+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "ses:*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJ2P4NXCHAT7NDPNR4",
        "PolicyName": "AmazonSESFullAccess",
        "UpdateDate": "2015-02-06T18:41:02+00:00",
        "VersionId": "v1"
    },
    "AmazonSESReadOnlyAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonSESReadOnlyAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:41:03+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "ses:Get*",
                        "ses:List*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAINV2XPFRMWJJNSCGI",
        "PolicyName": "AmazonSESReadOnlyAccess",
        "UpdateDate": "2015-02-06T18:41:03+00:00",
        "VersionId": "v1"
    },
    "AmazonSNSFullAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonSNSFullAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:41:05+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "sns:*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJWEKLCXXUNT2SOLSG",
        "PolicyName": "AmazonSNSFullAccess",
        "UpdateDate": "2015-02-06T18:41:05+00:00",
        "VersionId": "v1"
    },
    "AmazonSNSReadOnlyAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonSNSReadOnlyAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:41:06+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "sns:GetTopicAttributes",
                        "sns:List*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAIZGQCQTFOFPMHSB6W",
        "PolicyName": "AmazonSNSReadOnlyAccess",
        "UpdateDate": "2015-02-06T18:41:06+00:00",
        "VersionId": "v1"
    },
    "AmazonSNSRole": {
        "Arn": "arn:aws:iam::aws:policy/service-role/AmazonSNSRole",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:41:30+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "logs:CreateLogGroup",
                        "logs:CreateLogStream",
                        "logs:PutLogEvents",
                        "logs:PutMetricFilter",
                        "logs:PutRetentionPolicy"
                    ],
                    "Effect": "Allow",
                    "Resource": [
                        "*"
                    ]
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/service-role/",
        "PolicyId": "ANPAJK5GQB7CIK7KHY2GA",
        "PolicyName": "AmazonSNSRole",
        "UpdateDate": "2015-02-06T18:41:30+00:00",
        "VersionId": "v1"
    },
    "AmazonSQSFullAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonSQSFullAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:41:07+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "sqs:*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAI65L554VRJ33ECQS6",
        "PolicyName": "AmazonSQSFullAccess",
        "UpdateDate": "2015-02-06T18:41:07+00:00",
        "VersionId": "v1"
    },
    "AmazonSQSReadOnlyAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonSQSReadOnlyAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:41:08+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "sqs:GetQueueAttributes",
                        "sqs:ListQueues"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAIUGSSQY362XGCM6KW",
        "PolicyName": "AmazonSQSReadOnlyAccess",
        "UpdateDate": "2015-02-06T18:41:08+00:00",
        "VersionId": "v1"
    },
    "AmazonSSMFullAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonSSMFullAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-05-29T17:39:47+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "cloudwatch:PutMetricData",
                        "ds:CreateComputer",
                        "ds:DescribeDirectories",
                        "ec2:DescribeInstanceStatus",
                        "logs:*",
                        "ssm:*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJA7V6HI4ISQFMDYAG",
        "PolicyName": "AmazonSSMFullAccess",
        "UpdateDate": "2015-05-29T17:39:47+00:00",
        "VersionId": "v1"
    },
    "AmazonSSMReadOnlyAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonSSMReadOnlyAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-05-29T17:44:19+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "ssm:Describe*",
                        "ssm:Get*",
                        "ssm:List*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJODSKQGGJTHRYZ5FC",
        "PolicyName": "AmazonSSMReadOnlyAccess",
        "UpdateDate": "2015-05-29T17:44:19+00:00",
        "VersionId": "v1"
    },
    "AmazonVPCFullAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonVPCFullAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-05-07T18:04:37+00:00",
        "DefaultVersionId": "v3",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "ec2:AcceptVpcPeeringConnection",
                        "ec2:AllocateAddress",
                        "ec2:AssociateAddress",
                        "ec2:AssociateDhcpOptions",
                        "ec2:AssociateRouteTable",
                        "ec2:AttachClassicLinkVpc",
                        "ec2:AttachInternetGateway",
                        "ec2:AttachVpnGateway",
                        "ec2:AuthorizeSecurityGroupEgress",
                        "ec2:AuthorizeSecurityGroupIngress",
                        "ec2:CreateCustomerGateway",
                        "ec2:CreateDhcpOptions",
                        "ec2:CreateInternetGateway",
                        "ec2:CreateNetworkAcl",
                        "ec2:CreateNetworkAclEntry",
                        "ec2:CreateRoute",
                        "ec2:CreateRouteTable",
                        "ec2:CreateSecurityGroup",
                        "ec2:CreateSubnet",
                        "ec2:CreateTags",
                        "ec2:CreateVpc",
                        "ec2:CreateVpcEndpoint",
                        "ec2:CreateVpcPeeringConnection",
                        "ec2:CreateVpnConnection",
                        "ec2:CreateVpnConnectionRoute",
                        "ec2:CreateVpnGateway",
                        "ec2:DeleteCustomerGateway",
                        "ec2:DeleteDhcpOptions",
                        "ec2:DeleteInternetGateway",
                        "ec2:DeleteNetworkAcl",
                        "ec2:DeleteNetworkAclEntry",
                        "ec2:DeleteRoute",
                        "ec2:DeleteRouteTable",
                        "ec2:DeleteSecurityGroup",
                        "ec2:DeleteSubnet",
                        "ec2:DeleteTags",
                        "ec2:DeleteVpc",
                        "ec2:DeleteVpcEndpoints",
                        "ec2:DeleteVpcPeeringConnection",
                        "ec2:DeleteVpnConnection",
                        "ec2:DeleteVpnGateway",
                        "ec2:DescribeAddresses",
                        "ec2:DescribeAvailabilityZones",
                        "ec2:DescribeCustomerGateways",
                        "ec2:DescribeDhcpOptions",
                        "ec2:DescribeInstances",
                        "ec2:DescribeInternetGateways",
                        "ec2:DescribeKeyPairs",
                        "ec2:DescribeNetworkAcls",
                        "ec2:DescribeNetworkInterfaces",
                        "ec2:DescribePrefixLists",
                        "ec2:DescribeRouteTables",
                        "ec2:DescribeSecurityGroups",
                        "ec2:DescribeSubnets",
                        "ec2:DescribeTags",
                        "ec2:DescribeVpcAttribute",
                        "ec2:DescribeVpcClassicLink",
                        "ec2:DescribeVpcEndpoints",
                        "ec2:DescribeVpcEndpointServices",
                        "ec2:DescribeVpcPeeringConnections",
                        "ec2:DescribeVpcs",
                        "ec2:DescribeVpnConnections",
                        "ec2:DescribeVpnGateways",
                        "ec2:DetachClassicLinkVpc",
                        "ec2:DetachInternetGateway",
                        "ec2:DetachVpnGateway",
                        "ec2:DisableVpcClassicLink",
                        "ec2:DisableVgwRoutePropagation",
                        "ec2:DisassociateAddress",
                        "ec2:DisassociateRouteTable",
                        "ec2:EnableVpcClassicLink",
                        "ec2:EnableVgwRoutePropagation",
                        "ec2:ModifySubnetAttribute",
                        "ec2:ModifyVpcAttribute",
                        "ec2:ModifyVpcEndpoint",
                        "ec2:RejectVpcPeeringConnection",
                        "ec2:ReleaseAddress",
                        "ec2:ReplaceNetworkAclAssociation",
                        "ec2:ReplaceNetworkAclEntry",
                        "ec2:ReplaceRouteTableAssociation",
                        "ec2:RevokeSecurityGroupEgress",
                        "ec2:RevokeSecurityGroupIngress"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJBWPGNOVKZD3JI2P2",
        "PolicyName": "AmazonVPCFullAccess",
        "UpdateDate": "2015-05-07T18:07:43+00:00",
        "VersionId": "v3"
    },
    "AmazonVPCReadOnlyAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonVPCReadOnlyAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-05-07T17:59:08+00:00",
        "DefaultVersionId": "v2",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "ec2:DescribeAddresses",
                        "ec2:DescribeCustomerGateways",
                        "ec2:DescribeDhcpOptions",
                        "ec2:DescribeInternetGateways",
                        "ec2:DescribeNetworkAcls",
                        "ec2:DescribeNetworkInterfaces",
                        "ec2:DescribePrefixLists",
                        "ec2:DescribeRouteTables",
                        "ec2:DescribeSecurityGroups",
                        "ec2:DescribeSubnets",
                        "ec2:DescribeVpcAttribute",
                        "ec2:DescribeVpcEndpoints",
                        "ec2:DescribeVpcEndpointServices",
                        "ec2:DescribeVpcPeeringConnection",
                        "ec2:DescribeVpcs",
                        "ec2:DescribeVpnConnections",
                        "ec2:DescribeVpnGateways"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAIICZJNOJN36GTG6CM",
        "PolicyName": "AmazonVPCReadOnlyAccess",
        "UpdateDate": "2015-05-07T18:01:28+00:00",
        "VersionId": "v2"
    },
    "AmazonWorkMailFullAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonWorkMailFullAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-03-24T18:12:57+00:00",
        "DefaultVersionId": "v2",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "ds:AuthorizeApplication",
                        "ds:CheckAlias",
                        "ds:CreateAlias",
                        "ds:CreateDirectory",
                        "ds:CreateDomain",
                        "ds:DeleteAlias",
                        "ds:DeleteDirectory",
                        "ds:DescribeDirectories",
                        "ds:ExtendDirectory",
                        "ds:GetDirectoryLimits",
                        "ds:ListAuthorizedApplications",
                        "ds:UnauthorizeApplication",
                        "ec2:AuthorizeSecurityGroupEgress",
                        "ec2:AuthorizeSecurityGroupIngress",
                        "ec2:CreateNetworkInterface",
                        "ec2:CreateSecurityGroup",
                        "ec2:CreateSubnet",
                        "ec2:CreateTags",
                        "ec2:CreateVpc",
                        "ec2:DeleteSecurityGroup",
                        "ec2:DeleteSubnet",
                        "ec2:DeleteVpc",
                        "ec2:DescribeAvailabilityZones",
                        "ec2:DescribeDomains",
                        "ec2:DescribeRouteTables",
                        "ec2:DescribeSubnets",
                        "ec2:DescribeVpcs",
                        "ec2:RevokeSecurityGroupEgress",
                        "ec2:RevokeSecurityGroupIngress",
                        "kms:DescribeKey",
                        "kms:ListAliases",
                        "ses:*",
                        "workmail:*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJQVKNMT7SVATQ4AUY",
        "PolicyName": "AmazonWorkMailFullAccess",
        "UpdateDate": "2015-03-24T18:16:18+00:00",
        "VersionId": "v2"
    },
    "AmazonWorkMailReadOnlyAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonWorkMailReadOnlyAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:40:42+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "ses:Describe*",
                        "ses:Get*",
                        "workmail:Describe*",
                        "workmail:Get*",
                        "workmail:List*",
                        "workmail:Search*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJHF7J65E2QFKCWAJM",
        "PolicyName": "AmazonWorkMailReadOnlyAccess",
        "UpdateDate": "2015-02-06T18:40:42+00:00",
        "VersionId": "v1"
    },
    "AmazonWorkSpacesAdmin": {
        "Arn": "arn:aws:iam::aws:policy/AmazonWorkSpacesAdmin",
        "AttachmentCount": 0,
        "CreateDate": "2015-09-22T22:21:15+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "workspaces:CreateWorkspaces",
                        "workspaces:DescribeWorkspaces",
                        "workspaces:RebootWorkspaces",
                        "workspaces:RebuildWorkspaces",
                        "workspaces:TerminateWorkspaces",
                        "workspaces:DescribeWorkspaceDirectories",
                        "workspaces:DescribeWorkspaceBundles"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJ26AU6ATUQCT5KVJU",
        "PolicyName": "AmazonWorkSpacesAdmin",
        "UpdateDate": "2015-09-22T22:21:15+00:00",
        "VersionId": "v1"
    },
    "AmazonWorkSpacesApplicationManagerAdminAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonWorkSpacesApplicationManagerAdminAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-04-09T14:03:18+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": "wam:AuthenticatePackager",
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJPRL4KYETIH7XGTSS",
        "PolicyName": "AmazonWorkSpacesApplicationManagerAdminAccess",
        "UpdateDate": "2015-04-09T14:03:18+00:00",
        "VersionId": "v1"
    },
    "AmazonZocaloFullAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonZocaloFullAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:41:13+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "zocalo:*",
                        "ds:*",
                        "ec2:AuthorizeSecurityGroupEgress",
                        "ec2:AuthorizeSecurityGroupIngress",
                        "ec2:CreateNetworkInterface",
                        "ec2:CreateSecurityGroup",
                        "ec2:CreateSubnet",
                        "ec2:CreateTags",
                        "ec2:CreateVpc",
                        "ec2:DescribeAvailabilityZones",
                        "ec2:DescribeNetworkInterfaces",
                        "ec2:DescribeSubnets",
                        "ec2:DescribeVpcs",
                        "ec2:DeleteNetworkInterface",
                        "ec2:DeleteSecurityGroup",
                        "ec2:RevokeSecurityGroupEgress",
                        "ec2:RevokeSecurityGroupIngress"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJLCDXYRINDMUXEVL6",
        "PolicyName": "AmazonZocaloFullAccess",
        "UpdateDate": "2015-02-06T18:41:13+00:00",
        "VersionId": "v1"
    },
    "AmazonZocaloReadOnlyAccess": {
        "Arn": "arn:aws:iam::aws:policy/AmazonZocaloReadOnlyAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:41:14+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "zocalo:Describe*",
                        "ds:DescribeDirectories",
                        "ec2:DescribeVpcs",
                        "ec2:DescribeSubnets"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAISRCSSJNS3QPKZJPM",
        "PolicyName": "AmazonZocaloReadOnlyAccess",
        "UpdateDate": "2015-02-06T18:41:14+00:00",
        "VersionId": "v1"
    },
    "AutoScalingNotificationAccessRole": {
        "Arn": "arn:aws:iam::aws:policy/service-role/AutoScalingNotificationAccessRole",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:41:22+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "sqs:SendMessage",
                        "sqs:GetQueueUrl",
                        "sns:Publish"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/service-role/",
        "PolicyId": "ANPAIO2VMUPGDC5PZVXVA",
        "PolicyName": "AutoScalingNotificationAccessRole",
        "UpdateDate": "2015-02-06T18:41:22+00:00",
        "VersionId": "v1"
    },
    "CloudFrontFullAccess": {
        "Arn": "arn:aws:iam::aws:policy/CloudFrontFullAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-05-04T17:52:23+00:00",
        "DefaultVersionId": "v2",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "s3:ListAllMyBuckets"
                    ],
                    "Effect": "Allow",
                    "Resource": "arn:aws:s3:::*"
                },
                {
                    "Action": [
                        "cloudfront:*",
                        "iam:ListServerCertificates"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAIPRV52SH6HDCCFY6U",
        "PolicyName": "CloudFrontFullAccess",
        "UpdateDate": "2015-05-04T17:54:14+00:00",
        "VersionId": "v2"
    },
    "CloudFrontReadOnlyAccess": {
        "Arn": "arn:aws:iam::aws:policy/CloudFrontReadOnlyAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-05-04T17:56:12+00:00",
        "DefaultVersionId": "v2",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "cloudfront:Get*",
                        "cloudfront:List*",
                        "iam:ListServerCertificates",
                        "route53:List*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJJZMNYOTZCNQP36LG",
        "PolicyName": "CloudFrontReadOnlyAccess",
        "UpdateDate": "2015-05-04T17:58:09+00:00",
        "VersionId": "v2"
    },
    "CloudSearchFullAccess": {
        "Arn": "arn:aws:iam::aws:policy/CloudSearchFullAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:39:56+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "cloudsearch:*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAIM6OOWKQ7L7VBOZOC",
        "PolicyName": "CloudSearchFullAccess",
        "UpdateDate": "2015-02-06T18:39:56+00:00",
        "VersionId": "v1"
    },
    "CloudSearchReadOnlyAccess": {
        "Arn": "arn:aws:iam::aws:policy/CloudSearchReadOnlyAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:39:57+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "cloudsearch:Describe*",
                        "cloudsearch:List*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJWPLX7N7BCC3RZLHW",
        "PolicyName": "CloudSearchReadOnlyAccess",
        "UpdateDate": "2015-02-06T18:39:57+00:00",
        "VersionId": "v1"
    },
    "CloudWatchActionsEC2Access": {
        "Arn": "arn:aws:iam::aws:policy/CloudWatchActionsEC2Access",
        "AttachmentCount": 0,
        "CreateDate": "2015-07-07T00:00:33+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "cloudwatch:Describe*",
                        "ec2:Describe*",
                        "ec2:RebootInstances",
                        "ec2:StopInstances",
                        "ec2:TerminateInstances"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAIOWD4E3FVSORSZTGU",
        "PolicyName": "CloudWatchActionsEC2Access",
        "UpdateDate": "2015-07-07T00:00:33+00:00",
        "VersionId": "v1"
    },
    "CloudWatchFullAccess": {
        "Arn": "arn:aws:iam::aws:policy/CloudWatchFullAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:40:00+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "autoscaling:Describe*",
                        "cloudwatch:*",
                        "logs:*",
                        "sns:*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAIKEABORKUXN6DEAZU",
        "PolicyName": "CloudWatchFullAccess",
        "UpdateDate": "2015-02-06T18:40:00+00:00",
        "VersionId": "v1"
    },
    "CloudWatchLogsFullAccess": {
        "Arn": "arn:aws:iam::aws:policy/CloudWatchLogsFullAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:40:02+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "logs:*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJ3ZGNWK2R5HW5BQFO",
        "PolicyName": "CloudWatchLogsFullAccess",
        "UpdateDate": "2015-02-06T18:40:02+00:00",
        "VersionId": "v1"
    },
    "CloudWatchLogsReadOnlyAccess": {
        "Arn": "arn:aws:iam::aws:policy/CloudWatchLogsReadOnlyAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:40:03+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "logs:Describe*",
                        "logs:Get*",
                        "logs:TestMetricFilter"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJ2YIYDYSNNEHK3VKW",
        "PolicyName": "CloudWatchLogsReadOnlyAccess",
        "UpdateDate": "2015-02-06T18:40:03+00:00",
        "VersionId": "v1"
    },
    "CloudWatchReadOnlyAccess": {
        "Arn": "arn:aws:iam::aws:policy/CloudWatchReadOnlyAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:40:01+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "autoscaling:Describe*",
                        "cloudwatch:Describe*",
                        "cloudwatch:Get*",
                        "cloudwatch:List*",
                        "logs:Get*",
                        "logs:Describe*",
                        "logs:TestMetricFilter",
                        "sns:Get*",
                        "sns:List*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJN23PDQP7SZQAE3QE",
        "PolicyName": "CloudWatchReadOnlyAccess",
        "UpdateDate": "2015-02-06T18:40:01+00:00",
        "VersionId": "v1"
    },
    "DMSVPCManagementRole": {
        "Arn": "arn:aws:iam::aws:policy/service-role/DMSVPCManagementRole",
        "AttachmentCount": 0,
        "CreateDate": "2015-09-22T18:03:17+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "ec2:AuthorizeSecurityGroupIngress",
                        "ec2:CreateNetworkInterface",
                        "ec2:CreateSecurityGroup",
                        "ec2:DescribeAvailabilityZones",
                        "ec2:DescribeInternetGateways",
                        "ec2:DescribeSecurityGroups",
                        "ec2:DescribeSubnets",
                        "ec2:DescribeVpcAttribute",
                        "ec2:DescribeVpcs",
                        "ec2:DeleteNetworkInterface",
                        "ec2:DeleteSecurityGroup",
                        "ec2:RevokeSecurityGroupIngress"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/service-role/",
        "PolicyId": "ANPAJBODEMXSL5VOGBPFO",
        "PolicyName": "DMSVPCManagementRole",
        "UpdateDate": "2015-09-22T18:03:17+00:00",
        "VersionId": "v1"
    },
    "IAMFullAccess": {
        "Arn": "arn:aws:iam::aws:policy/IAMFullAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:40:38+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": "iam:*",
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAI7XKCFMBPM3QQRRVQ",
        "PolicyName": "IAMFullAccess",
        "UpdateDate": "2015-02-06T18:40:38+00:00",
        "VersionId": "v1"
    },
    "IAMReadOnlyAccess": {
        "Arn": "arn:aws:iam::aws:policy/IAMReadOnlyAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-04-21T16:01:34+00:00",
        "DefaultVersionId": "v2",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "iam:GenerateCredentialReport",
                        "iam:Get*",
                        "iam:List*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJKSO7NDY4T57MWDSQ",
        "PolicyName": "IAMReadOnlyAccess",
        "UpdateDate": "2015-04-21T16:03:51+00:00",
        "VersionId": "v2"
    },
    "IAMUserSSHKeys": {
        "Arn": "arn:aws:iam::aws:policy/IAMUserSSHKeys",
        "AttachmentCount": 0,
        "CreateDate": "2015-07-09T17:08:54+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "iam:DeleteSSHPublicKey",
                        "iam:GetSSHPublicKey",
                        "iam:ListSSHPublicKeys",
                        "iam:UpdateSSHPublicKey",
                        "iam:UploadSSHPublicKey"
                    ],
                    "Effect": "Allow",
                    "Resource": "arn:aws:iam::*:user/${aws:username}"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJTSHUA4UXGXU7ANUA",
        "PolicyName": "IAMUserSSHKeys",
        "UpdateDate": "2015-07-09T17:08:54+00:00",
        "VersionId": "v1"
    },
    "PowerUserAccess": {
        "Arn": "arn:aws:iam::aws:policy/PowerUserAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:39:47+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Effect": "Allow",
                    "NotAction": "iam:*",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJYRXTHIB4FOVS3ZXS",
        "PolicyName": "PowerUserAccess",
        "UpdateDate": "2015-02-06T18:39:47+00:00",
        "VersionId": "v1"
    },
    "RDSCloudHsmAuthorizationRole": {
        "Arn": "arn:aws:iam::aws:policy/service-role/RDSCloudHsmAuthorizationRole",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:41:29+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "cloudhsm:CreateLunaClient",
                        "cloudhsm:GetClientConfiguration",
                        "cloudhsm:DeleteLunaClient",
                        "cloudhsm:DescribeLunaClient",
                        "cloudhsm:ModifyLunaClient",
                        "cloudhsm:DescribeHapg",
                        "cloudhsm:ModifyHapg",
                        "cloudhsm:GetConfig"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/service-role/",
        "PolicyId": "ANPAIWKFXRLQG2ROKKXLE",
        "PolicyName": "RDSCloudHsmAuthorizationRole",
        "UpdateDate": "2015-02-06T18:41:29+00:00",
        "VersionId": "v1"
    },
    "ReadOnlyAccess": {
        "Arn": "arn:aws:iam::aws:policy/ReadOnlyAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-11-02T23:13:14+00:00",
        "DefaultVersionId": "v6",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "appstream:Get*",
                        "autoscaling:Describe*",
                        "cloudformation:DescribeStackEvents",
                        "cloudformation:DescribeStackResource",
                        "cloudformation:DescribeStackResources",
                        "cloudformation:DescribeStacks",
                        "cloudformation:GetTemplate",
                        "cloudformation:List*",
                        "cloudfront:Get*",
                        "cloudfront:List*",
                        "cloudsearch:Describe*",
                        "cloudsearch:List*",
                        "cloudtrail:DescribeTrails",
                        "cloudtrail:GetTrailStatus",
                        "cloudwatch:Describe*",
                        "cloudwatch:Get*",
                        "cloudwatch:List*",
                        "codecommit:BatchGetRepositories",
                        "codecommit:Get*",
                        "codecommit:GitPull",
                        "codecommit:List*",
                        "codedeploy:Batch*",
                        "codedeploy:Get*",
                        "codedeploy:List*",
                        "config:Deliver*",
                        "config:Describe*",
                        "config:Get*",
                        "datapipeline:DescribeObjects",
                        "datapipeline:DescribePipelines",
                        "datapipeline:EvaluateExpression",
                        "datapipeline:GetPipelineDefinition",
                        "datapipeline:ListPipelines",
                        "datapipeline:QueryObjects",
                        "datapipeline:ValidatePipelineDefinition",
                        "directconnect:Describe*",
                        "dynamodb:BatchGetItem",
                        "dynamodb:DescribeTable",
                        "dynamodb:GetItem",
                        "dynamodb:ListTables",
                        "dynamodb:Query",
                        "dynamodb:Scan",
                        "ec2:Describe*",
                        "ec2:GetConsoleOutput",
                        "ecs:Describe*",
                        "ecs:List*",
                        "elasticache:Describe*",
                        "elasticache:List*",
                        "elasticbeanstalk:Check*",
                        "elasticbeanstalk:Describe*",
                        "elasticbeanstalk:List*",
                        "elasticbeanstalk:RequestEnvironmentInfo",
                        "elasticbeanstalk:RetrieveEnvironmentInfo",
                        "elasticloadbalancing:Describe*",
                        "elasticmapreduce:Describe*",
                        "elasticmapreduce:List*",
                        "elastictranscoder:List*",
                        "elastictranscoder:Read*",
                        "firehose:Describe*",
                        "firehose:List*",
                        "iam:GenerateCredentialReport",
                        "iam:Get*",
                        "iam:List*",
                        "inspector:Describe*",
                        "inspector:Get*",
                        "inspector:List*",
                        "inspector:LocalizeText",
                        "inspector:PreviewAgentsForResourceGroup",
                        "iot:Describe*",
                        "iot:Get*",
                        "iot:List*",
                        "kinesis:Describe*",
                        "kinesis:Get*",
                        "kinesis:List*",
                        "kms:Describe*",
                        "kms:Get*",
                        "kms:List*",
                        "lambda:List*",
                        "lambda:Get*",
                        "logs:Describe*",
                        "logs:Get*",
                        "logs:TestMetricFilter",
                        "opsworks:Describe*",
                        "opsworks:Get*",
                        "rds:Describe*",
                        "rds:ListTagsForResource",
                        "redshift:Describe*",
                        "redshift:ViewQueriesInConsole",
                        "route53:Get*",
                        "route53:List*",
                        "route53domains:CheckDomainAvailability",
                        "route53domains:GetDomainDetail",
                        "route53domains:GetOperationDetail",
                        "route53domains:ListDomains",
                        "route53domains:ListOperations",
                        "route53domains:ListTagsForDomain",
                        "s3:Get*",
                        "s3:List*",
                        "sdb:GetAttributes",
                        "sdb:List*",
                        "sdb:Select*",
                        "ses:Get*",
                        "ses:List*",
                        "sns:Get*",
                        "sns:List*",
                        "sqs:GetQueueAttributes",
                        "sqs:ListQueues",
                        "sqs:ReceiveMessage",
                        "storagegateway:Describe*",
                        "storagegateway:List*",
                        "swf:Count*",
                        "swf:Describe*",
                        "swf:Get*",
                        "swf:List*",
                        "tag:Get*",
                        "trustedadvisor:Describe*",
                        "waf:Get*",
                        "waf:List*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAILL3HVNFSB6DCOWYQ",
        "PolicyName": "ReadOnlyAccess",
        "UpdateDate": "2015-11-02T23:13:14+00:00",
        "VersionId": "v6"
    },
    "ResourceGroupsandTagEditorFullAccess": {
        "Arn": "arn:aws:iam::aws:policy/ResourceGroupsandTagEditorFullAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:39:53+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "tag:getResources",
                        "tag:getTagKeys",
                        "tag:getTagValues",
                        "tag:addResourceTags",
                        "tag:removeResourceTags"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJNOS54ZFXN4T2Y34A",
        "PolicyName": "ResourceGroupsandTagEditorFullAccess",
        "UpdateDate": "2015-02-06T18:39:53+00:00",
        "VersionId": "v1"
    },
    "ResourceGroupsandTagEditorReadOnlyAccess": {
        "Arn": "arn:aws:iam::aws:policy/ResourceGroupsandTagEditorReadOnlyAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:39:54+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "tag:getResources",
                        "tag:getTagKeys",
                        "tag:getTagValues"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJHXQTPI5I5JKAIU74",
        "PolicyName": "ResourceGroupsandTagEditorReadOnlyAccess",
        "UpdateDate": "2015-02-06T18:39:54+00:00",
        "VersionId": "v1"
    },
    "SecurityAudit": {
        "Arn": "arn:aws:iam::aws:policy/SecurityAudit",
        "AttachmentCount": 0,
        "CreateDate": "2015-06-15T22:13:40+00:00",
        "DefaultVersionId": "v3",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "autoscaling:Describe*",
                        "cloudformation:DescribeStack*",
                        "cloudformation:GetTemplate",
                        "cloudformation:ListStack*",
                        "cloudfront:Get*",
                        "cloudfront:List*",
                        "cloudwatch:Describe*",
                        "codedeploy:Batch*",
                        "codedeploy:Get*",
                        "codedeploy:List*",
                        "config:Deliver*",
                        "config:Describe*",
                        "config:Get*",
                        "datapipeline:DescribeObjects",
                        "datapipeline:DescribePipelines",
                        "datapipeline:EvaluateExpression",
                        "datapipeline:GetPipelineDefinition",
                        "datapipeline:ListPipelines",
                        "datapipeline:QueryObjects",
                        "datapipeline:ValidatePipelineDefinition",
                        "directconnect:Describe*",
                        "dynamodb:ListTables",
                        "ec2:Describe*",
                        "ecs:Describe*",
                        "ecs:List*",
                        "elasticache:Describe*",
                        "elasticbeanstalk:Describe*",
                        "elasticloadbalancing:Describe*",
                        "elasticmapreduce:DescribeJobFlows",
                        "elasticmapreduce:ListClusters",
                        "glacier:ListVaults",
                        "iam:GenerateCredentialReport",
                        "iam:Get*",
                        "iam:List*",
                        "kms:Describe*",
                        "kms:Get*",
                        "kms:List*",
                        "rds:Describe*",
                        "rds:DownloadDBLogFilePortion",
                        "rds:ListTagsForResource",
                        "redshift:Describe*",
                        "route53:GetChange",
                        "route53:GetCheckerIpRanges",
                        "route53:GetGeoLocations",
                        "route53:GetHealthCheck",
                        "route53:GetHealthCheckCount",
                        "route53:GetHealthCheckLastFailureReason",
                        "route53:GetHostedZone",
                        "route53:GetHostedZone",
                        "route53:GetHostedZoneCount",
                        "route53:GetReusableDelegationSet",
                        "route53:ListGeoLocations",
                        "route53:ListHealthChecks",
                        "route53:ListHostedZones",
                        "route53:ListHostedZones",
                        "route53:ListHostedZonesByName",
                        "route53:ListResourceRecordSets",
                        "route53:ListReusableDelegationSets",
                        "route53:ListTagsForResource",
                        "route53:ListTagsForResources",
                        "route53domains:GetDomainDetail",
                        "route53domains:GetOperationDetail",
                        "route53domains:ListDomains",
                        "route53domains:ListOperations",
                        "route53domains:ListTagsForDomain",
                        "s3:GetBucket*",
                        "s3:GetLifecycleConfiguration",
                        "s3:GetObjectAcl",
                        "s3:GetObjectVersionAcl",
                        "s3:ListAllMyBuckets",
                        "sdb:DomainMetadata",
                        "sdb:ListDomains",
                        "sns:GetTopicAttributes",
                        "sns:ListTopics",
                        "sqs:GetQueueAttributes",
                        "sqs:ListQueues",
                        "tag:GetResources",
                        "tag:GetTagKeys"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAIX2T3QCXHR2OGGCTO",
        "PolicyName": "SecurityAudit",
        "UpdateDate": "2015-06-15T22:15:17+00:00",
        "VersionId": "v3"
    },
    "ServiceCatalogAdminFullAccess": {
        "Arn": "arn:aws:iam::aws:policy/ServiceCatalogAdminFullAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-09-29T18:39:43+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "catalog-admin:*",
                        "catalog-user:*",
                        "cloudformation:CreateStack",
                        "cloudformation:DeleteStack",
                        "cloudformation:DescribeStackEvents",
                        "cloudformation:DescribeStacks",
                        "cloudformation:GetTemplateSummary",
                        "cloudformation:SetStackPolicy",
                        "cloudformation:ValidateTemplate",
                        "cloudformation:UpdateStack",
                        "iam:GetGroup",
                        "iam:GetRole",
                        "iam:GetUser",
                        "iam:ListGroups",
                        "iam:ListRoles",
                        "iam:ListUsers",
                        "iam:PassRole",
                        "s3:CreateBucket",
                        "s3:GetObject",
                        "s3:PutObject",
                        "servicecatalog:*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAIKTX42IAS75B7B7BY",
        "PolicyName": "ServiceCatalogAdminFullAccess",
        "UpdateDate": "2015-09-29T18:39:43+00:00",
        "VersionId": "v1"
    },
    "ServiceCatalogAdminReadOnlyAccess": {
        "Arn": "arn:aws:iam::aws:policy/ServiceCatalogAdminReadOnlyAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-09-29T18:40:35+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "catalog-admin:DescribeConstraints",
                        "catalog-admin:DescribeListingForProduct",
                        "catalog-admin:DescribeListings",
                        "catalog-admin:DescribePortfolios",
                        "catalog-admin:DescribeProductVersions",
                        "catalog-admin:GetPortfolioCount",
                        "catalog-admin:GetPortfolios",
                        "catalog-admin:GetProductCounts",
                        "catalog-admin:ListAllPortfolioConstraints",
                        "catalog-admin:ListPortfolioConstraints",
                        "catalog-admin:ListPortfolios",
                        "catalog-admin:ListPrincipalConstraints",
                        "catalog-admin:ListProductConstraints",
                        "catalog-admin:ListResourceUsers",
                        "catalog-admin:ListTagsForResource",
                        "catalog-admin:SearchListings",
                        "catalog-user:*",
                        "cloudformation:DescribeStackEvents",
                        "cloudformation:DescribeStacks",
                        "cloudformation:GetTemplateSummary",
                        "iam:GetGroup",
                        "iam:GetRole",
                        "iam:GetUser",
                        "iam:ListGroups",
                        "iam:ListRoles",
                        "iam:ListUsers",
                        "s3:GetObject",
                        "servicecatalog:DescribePackage",
                        "servicecatalog:DescribeStack",
                        "servicecatalog:GetProductVersionSummary",
                        "servicecatalog:ListStackEvents",
                        "servicecatalog:ListStacks"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJ7XOUSS75M4LIPKO4",
        "PolicyName": "ServiceCatalogAdminReadOnlyAccess",
        "UpdateDate": "2015-09-29T18:40:35+00:00",
        "VersionId": "v1"
    },
    "ServiceCatalogEndUserAccess": {
        "Arn": "arn:aws:iam::aws:policy/ServiceCatalogEndUserAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-09-29T18:41:33+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "catalog-user:*",
                        "s3:GetObject",
                        "servicecatalog:*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJ56OMCO72RI4J5FSA",
        "PolicyName": "ServiceCatalogEndUserAccess",
        "UpdateDate": "2015-09-29T18:41:33+00:00",
        "VersionId": "v1"
    },
    "ServiceCatalogEndUserFullAccess": {
        "Arn": "arn:aws:iam::aws:policy/ServiceCatalogEndUserFullAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-09-29T18:41:01+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "catalog-user:*",
                        "cloudformation:CreateStack",
                        "cloudformation:DeleteStack",
                        "cloudformation:DescribeStackEvents",
                        "cloudformation:DescribeStacks",
                        "cloudformation:GetTemplateSummary",
                        "cloudformation:SetStackPolicy",
                        "cloudformation:ValidateTemplate",
                        "cloudformation:UpdateStack",
                        "s3:GetObject",
                        "servicecatalog:*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAJIW7AFFOONVKW75KU",
        "PolicyName": "ServiceCatalogEndUserFullAccess",
        "UpdateDate": "2015-09-29T18:41:01+00:00",
        "VersionId": "v1"
    },
    "SimpleWorkflowFullAccess": {
        "Arn": "arn:aws:iam::aws:policy/SimpleWorkflowFullAccess",
        "AttachmentCount": 0,
        "CreateDate": "2015-02-06T18:41:04+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "swf:*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/",
        "PolicyId": "ANPAIFE3AV6VE7EANYBVM",
        "PolicyName": "SimpleWorkflowFullAccess",
        "UpdateDate": "2015-02-06T18:41:04+00:00",
        "VersionId": "v1"
    },
    "VMImportExportRoleForAWSConnector": {
        "Arn": "arn:aws:iam::aws:policy/service-role/VMImportExportRoleForAWSConnector",
        "AttachmentCount": 0,
        "CreateDate": "2015-09-03T20:48:59+00:00",
        "DefaultVersionId": "v1",
        "Document": {
            "Statement": [
                {
                    "Action": [
                        "s3:ListBucket",
                        "s3:GetBucketLocation",
                        "s3:GetObject"
                    ],
                    "Effect": "Allow",
                    "Resource": [
                        "arn:aws:s3:::import-to-ec2-*"
                    ]
                },
                {
                    "Action": [
                        "ec2:ModifySnapshotAttribute",
                        "ec2:CopySnapshot",
                        "ec2:RegisterImage",
                        "ec2:Describe*"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ],
            "Version": "2012-10-17"
        },
        "IsAttachable": True,
        "IsDefaultVersion": True,
        "Path": "/service-role/",
        "PolicyId": "ANPAJFLQOOJ6F5XNX4LAW",
        "PolicyName": "VMImportExportRoleForAWSConnector",
        "UpdateDate": "2015-09-03T20:48:59+00:00",
        "VersionId": "v1"
    }
}