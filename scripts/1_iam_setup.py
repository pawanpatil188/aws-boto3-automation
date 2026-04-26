import boto3

iam = boto3.client('iam')

user_name = "boto3-demo-user"

response = iam.create_user(UserName=user_name)

print("IAM User Created:", response['User']['UserName'])