import json
import boto3

def create_iam_policy():
    # Create IAM client
    iam = boto3.client('iam')

    # Create a policy
    my_managed_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
        "Effect": "Allow",
        "Action": [
            "autoscaling:Describe*",
            "batch:Describe*",
            "batch:List*",
            "cloudformation:Describe*",
            "cloudformation:List*",
            "cloudfront:ListDistributions*",
            "cloudtrail:Describe*",
            "cloudtrail:Get*",
            "cloudtrail:List*",
            "cloudtrail:LookupEvents",
            "cloudwatch:Describe*",
            "cloudwatch:GetMetric*",
            "cloudwatch:ListMetrics",
            "cognito-idp:ListResourcesForWebACL",
            "cognito-sync:GetCognitoEvents",
            "config:Describe*",
            "dynamodb:Describe*",
            "dynamodb:List*",
            "ec2:Describe*",
            "ecr:Describe*",
            "ecr:GetRegistryScanningConfiguration",
            "ecr:GetRepositoryPolicy",
            "ecr:List*",
            "ecr:StartImageScan",
            "ecr-public:Describe*",
            "ecr-public:GetRepositoryPolicy",
            "ecr-public:List*",
            "ecs:Describe*",
            "ecs:List*",
            "eks:Describe*",
            "eks:List*",
            "elasticache:Describe*",
            "elasticache:List*",
            "elasticbeanstalk:Describe*",
            "elasticbeanstalk:List*",
            "elasticloadbalancing:Describe*",
            "elasticmapreduce:Describe*",
            "elasticmapreduce:List*",
            "es:Describe*",
            "es:List*",
            "events:ListRules",
            "iam:Generate*",
            "iam:Get*",
            "iam:List*",
            "identitystore:Describe*",
            "inspector2:List*",
            "iot:GetTopicRule",
            "kms:Describe*",
            "kms:GetKey*",
            "kms:List*",
            "kinesis:Describe*",
            "kinesis:List*",
            "lambda:Get*Policy",
            "lambda:GetAccountSettings",
            "lambda:List*",
            "logs:Describe*",
            "organizations:Describe*",
            "organizations:List*",
            "rds:Describe*",
            "rds:List*",
            "redshift:Describe*",
            "redshift:List*",
            "route53:Get*",
            "route53:List*",
            "route53domains:Get*",
            "route53domains:List*",
            "route53resolver:Get*",
            "route53resolver:List*",
            "s3:Describe*",
            "s3:GetAccessPoint*",
            "s3:GetAccountPublicAccessBlock",
            "s3:GetBucket*",
            "s3:GetEncryptionConfiguration",
            "s3:GetJobTagging",
            "s3:GetLifecycleConfiguration",
            "s3:ListAccessPoints",
            "s3:ListAllMyBuckets",
            "s3:ListBucketVersions",
            "s3:ListJobs",
            "secretsmanager:Describe*",
            "secretsmanager:GetResourcePolicy",
            "secretsmanager:List*",
            "sns:Get*",
            "sns:List*",
            "sqs:Get*",
            "sqs:List*",
            "ssm:Describe*",
            "ssm:List*",
            "sso:Describe*",
            "sso:Get*",
            "sso:List*",
            "sso-directory:List*",
            "sso-directory:Search*",
            "sts:DecodeAuthorizationMessage",
            "tag:Get*",
            "wafv2:Get*",
            "wafv2:List*"
        ],
        "Resource": "*"
        },
        {
        "Effect": "Allow",
        "Action": [
            "s3:GetBucketLocation",
            "s3:GetObject",
            "s3:ListBucket"
        ],
        "Resource":[
            "arn:aws:s3:::elasticbeanstalk-*",
            "arn:aws:s3:::aws-cloudtrail-logs-ermetic",
            "arn:aws:s3:::aws-cloudtrail-logs-ermetic/*"
        ] 
        },
        {
        "Effect": "Allow",
        "Action": "apigateway:Get*",
        "NotResource": "arn:aws:apigateway:*::/apikeys*"
        }
    ]
    }
    response = iam.create_policy(
        PolicyName='ErmeticReadOnlyPolicy',
        PolicyDocument=json.dumps(my_managed_policy)
    )
    print(response)

create_iam_policy()