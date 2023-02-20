import boto3
import global_var

client = boto3.client('s3')

def create_bucket():

    response = client.create_bucket(
        Bucket= global_var.bucket_name
    ),
    client.put_public_access_block(
        Bucket= global_var.bucket_name,
        PublicAccessBlockConfiguration={
            'BlockPublicAcls': True,
            'IgnorePublicAcls': True,
            'BlockPublicPolicy': True,
            'RestrictPublicBuckets': True
        },
        ExpectedBucketOwner= global_var.account_id
    ),
    client.put_bucket_encryption(
    Bucket= global_var.bucket_name,
    ServerSideEncryptionConfiguration={
        'Rules': [
            {
                'ApplyServerSideEncryptionByDefault': {
                    'SSEAlgorithm': 'AES256'
                },
            },
        ]
    })
    print(response)
    return response


create_bucket()
