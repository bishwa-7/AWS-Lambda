# Lambda integration with IAM, EC2 and CloudWatch

## Create an EC2 instance:
- create and EC2 instance using AWS console
- create a key pair as well

## Configure IAM Role:
- Every service if they want to use other service, they must have IAM roles and permissions
- Create Role:
    - Trusted entity type: AWS service
    - Use case: Lambda
    - Do not add permission right now
    - Role name: LambdaSnap
    - Create role

- Add Permissions:
    - Choose the role
    - Under permission, click Add permissions
        - Choose Create inline policy
        - Click JSON:
            - Erase the existing text
            - Paste the following text:
            {
"Version": "2012-10-17",
"Statement": [
{
"Effect": "Allow",
"Action": [
"logs:*"
],
"Resource": "arn:aws:logs:*:*:*"
},
{
"Effect": "Allow",
"Action": [
"ec2:CreateSnapshot",
"ec2:DeleteSnapshot",
"ec2:Describe*",
"ec2:CreateTags",
"ec2:ModifySnapshotAttribute",
"ec2:ResetSnapshotAttribute"
],
"Resource": [
"*"
]
}
]
}

            - Click Next
            - Policy name: TrainingLamda
            - Click Create Policy



## Create Lambda Function:
    - Role:
        - Use an existing role
        - Existing role: LambdaSnap
    
### Add trigger:
    - Click Triggers
    - Add trigger:
        - Select a source: EventBridge (CloudWatch Events)
        - Rule: Create a new rule
        - Rule name: DailyEC2Snap
        - Rule type: Schedule expression
        - Schedule expression: rate (1 day)
        - Click Add

### Test:
    - create new event on test tab
    - Event name: test2
    - Private should be selected by default
    - Template: Choose Cloudwatch
    - Click save
    - Click Test

