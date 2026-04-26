import boto3
import time
from config import REGION

s3 = boto3.client('s3', region_name=REGION)

# ✅ Create unique bucket name using timestamp
bucket_name = f"boto3-demo-bucket-{int(time.time())}"

try:
    response = s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': REGION
        }
    )

    print("✅ S3 Bucket Created Successfully!")
    print("Bucket Name:", bucket_name)

except Exception as e:
    print("❌ Error creating bucket:", str(e))