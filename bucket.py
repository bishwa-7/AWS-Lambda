import boto3

def create_s3_bucket(bucket_name, region=None):
    s3_client = boto3.client('s3')

    if region is None:
        response = s3_client.create_bucket(Bucket=bucket_name)
    else:
        response = s3_client.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                'LocationConstraint':region
            }
        )

    return response


if __name__=='__main__':
    bucket_name='lambda-learning-bishwa-01'
    region = 'us-west-1'
    response = create_s3_bucket(bucket_name, region)
    print(response)