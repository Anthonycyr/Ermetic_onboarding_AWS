import boto3
import global_var

def create_trails():

    client = boto3.client('cloudtrail')

    response = client.create_trail(
        Name= global_var.trail_name,
        S3BucketName= global_var.bucket_name,
        IncludeGlobalServiceEvents=True,
        IsMultiRegionTrail=True,
        EnableLogFileValidation=True,
        IsOrganizationTrail=False,
        TagsList = [{
            'Key': 'ermetic'
        }]
    )
    print(response)
    return response 
    
create_trails()