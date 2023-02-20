import boto3
import global_var

client = boto3.client('s3')

def create_bucket():

    response = client.create_bucket(
        Bucket= global_var.bucket_name,
        PublicAccessBlockConfiguration={
            'BlockPublicAcls': True,
            'IgnorePublicAcls': True,
            'BlockPublicPolicy': True,
            'RestrictPublicBuckets': True
        },
        ServerSideEncryptionConfiguration={
            'Rules': [
                {
                    'ApplyServerSideEncryptionByDefault': {
                        'SSEAlgorithm': 'AES256'
                    },
                },
            ]
        }
    )
    print(response)
    return response

create_bucket()
