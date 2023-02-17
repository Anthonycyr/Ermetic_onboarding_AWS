import boto3
import json
import global_var

def attach_bucket_policy():        

    # Create a bucket policy
    bucket_name = global_var.bucket_name
    policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "AWSCloudTrailAclCheck",
                "Effect": "Allow",
                "Principal": {"Service": "cloudtrail.amazonaws.com"},
                "Action": "s3:GetBucketAcl",
                'Resource': f'arn:aws:s3:::{bucket_name}',
            },
            {
                "Sid": "AWSCloudTrailWrite",
                "Effect": "Allow",
                "Principal": {"Service": "cloudtrail.amazonaws.com"},
                "Action": "s3:PutObject",
                "Resource": f"arn:aws:s3:::{bucket_name}/AWSLogs/{global_var.account_id}/*",
                "Condition": {
                    "StringEquals": {
                        "s3:x-amz-acl": "bucket-owner-full-control",
                    }
                }
            }
        ]
    }
    
    bucket_policy = json.dumps(policy)
    s3 = boto3.client('s3')
    response = s3.put_bucket_policy(
        Bucket = bucket_name,
        Policy = bucket_policy
        )
    print(response)
    return response
attach_bucket_policy()

# J'ai du enlever cette partie la dans les deux policy dans la section Condition pour que ca fonctionne  
# "aws:SourceArn": f"arn:aws:cloudtrail:{global_var.region}:{global_var.account_id}:trail/{global_var.trail_name}"

