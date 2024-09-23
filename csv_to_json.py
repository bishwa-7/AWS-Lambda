import boto3
import csv
import json
import os


# create an s3 client using boto3
s3 = boto3.client('s3')
def lambda_handler(event, context):
    # get the bucket name and the file/key name from the event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    csv_file_key = event['Records'][0]['s3']['object']['key']

    # download the CSV file from the S3 bucket
    download_path = f"/tmp/{os.path.basename(csv_file_key)}"
    s3.download_file(bucket_name, csv_file_key, download_path)

    # convert CSV to json
    json_data = csv_to_json(download_path)

    # generate the JSON file name
    json_file_key = csv_file_key.replace('.csv', '.json')

    # upload the JSON file back to the same S3 bucket
    upload_path = f"/tmp/{os.path.basename(json_file_key)}"
    with open(upload_path, 'w') as json_file:
        json.dump(json_data, json_file)
    
    s3.upload_file(upload_path, bucket_name, json_file_key)

    return{
        'statusCode':200,
        'body':f"CSV file '{csv_file_key}' converted to JSON and saved as '{json_file_key}'"
    }

def csv_to_json(file_path):
    json_output = []

    with open(file_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            json_output.append(row)
    return json_output