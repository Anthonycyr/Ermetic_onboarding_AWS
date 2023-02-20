import boto3
# import create_trail

def get_account_id():
    client = boto3.client("sts")
    return client.get_caller_identity()["Account"]

if __name__ == "__main__":
    print(get_account_id())


###################################
id = get_account_id()
account_id = get_account_id()
region = "ca-central-1"
external_id = "25b1295f-19eb-4614-ae75-e6b3833c9cd0"
ermetic_account_id = "081802104111"
trail_name = 'Ermetic_trail'
role_name = "ErmeticRole"
role_arn = f"arn:aws:iam::{account_id}:role/{role_name}"
bucket_name = f"aws-cloudtrail-logs-ermetic-{account_id}"

