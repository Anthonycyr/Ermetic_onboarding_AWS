import boto3
import global_var

client = boto3.client('s3')

def create_bucket():

    response = client.create_bucket(
        Bucket= global_var.bucket_name
    )
    print(response)
    return response

def put_bucket_encryption():
    response = client.put_bucket_encryption(
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

    return response
    


create_bucket()
put_bucket_encryption()