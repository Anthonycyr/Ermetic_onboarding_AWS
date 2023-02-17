import boto3
import global_var

def get_account_name():
    org = boto3.client('organizations')
    account_name = org.describe_account(AccountId= global_var.account_id).get('Account')
    return account_name['Name']

print(get_account_name())