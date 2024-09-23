## Learning:

### Installation:

- create virtual environment
- install boto3
- install aws cli
    - https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
- create a user and configure access id and secret key
- write lambda code and package it into a zip file containing dependencies and the lambda file
    - mkdir lambda_package
    - pip3 install requests -t lambda_package/
    - mv lambda_function.py lambda_package
    - cd lambda_package 
    - zip -r ../lambda_package.zip .

- create IAM role for lambda with necessary permission using policy:
    - create policy: https://us-east-1.console.aws.amazon.com/iam/home#/policies
    - create role: https://us-east-1.console.aws.amazon.com/iam/home#/roles

- create S3 trigger in lambda
- clean up the resources
    - delete lambda function
    - delete execution role
    - delete s3 bucket

### Change handler:
- https://docs.aws.amazon.com/lambda/latest/dg/python-handler.html
- Go to code section and change the handler function
- Default: lambda_function.lambda_handler