import boto3

s3 = boto3.client("s3")

s3.create_bucket(
    Bucket="tech610-montezer-test-boto3",
    CreateBucketConfiguration={"LocationConstraint": "eu-west-1"}
)

print("Bucket created")