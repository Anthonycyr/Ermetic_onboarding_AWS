import boto3

    
def get_account_id():
    client = boto3.client("sts")
    return client.get_caller_identity()["Account"]


if __name__ == "__main__":
    print(get_account_id())

account_id = get_account_id()

role_name = "ErmeticRole"
policy_arn = "arn:aws:iam::"+ account_id +":policy/ErmeticReadOnlyPolicy"

def attach_iam_policy(policy_arn, role_name):
    iam = boto3.client("iam")

    response = iam.attach_role_policy(
        RoleName= role_name,
        PolicyArn= policy_arn
    )

    print(response)

attach_iam_policy(policy_arn, role_name)