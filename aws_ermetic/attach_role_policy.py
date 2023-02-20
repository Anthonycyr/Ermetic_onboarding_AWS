import boto3
import global_var

role_name = global_var.role_name
policy_arn = "arn:aws:iam::aws:policy/SecurityAudit"
    

def attach_iam_policy(policy_arn, role_name):
    iam = boto3.client("iam")

    response = iam.attach_role_policy(
        RoleName= role_name,
        PolicyArn= policy_arn
    )

    print(response)

attach_iam_policy(policy_arn, role_name)