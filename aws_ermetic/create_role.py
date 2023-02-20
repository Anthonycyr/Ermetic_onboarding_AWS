import json
import boto3
import global_var

def create_iam_role():
    iam = boto3.client("iam")
    

    
    assume_role_policy_document = json.dumps({
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "sts:AssumeRole",
            "Principal": {
                "AWS": global_var.ermetic_account_id
            },
            "Condition": {
                "StringEquals": {
                    "sts:ExternalId": global_var.external_id
                }
            }
        }
    ]
    })
    response = iam.create_role(
        Path = "/", 
        RoleName = global_var.role_name,
        AssumeRolePolicyDocument = assume_role_policy_document,
    )
    print(response)
    return response["Role"]["RoleName"] 

create_iam_role()