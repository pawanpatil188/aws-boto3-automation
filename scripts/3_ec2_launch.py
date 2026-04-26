import boto3

REGION = "us-east-1"

ec2 = boto3.resource('ec2', region_name=REGION)

try:
    instances = ec2.create_instances(
        ImageId="ami-0c02fb55956c7d316",  # Amazon Linux 2 (US East)
        InstanceType="t3.micro",
        MinCount=1,
        MaxCount=1,

        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [{'Key': 'Name', 'Value': 'boto3-demo'}]
            }
        ]
    )

    instance = instances[0]

    print("✅ EC2 Launched Successfully")
    print("Instance ID:", instance.id)

except Exception as e:
    print("❌ EC2 Launch Failed:", str(e))