import boto3

s3 = boto3.client("s3")

s3.delete_bucket(
    Bucket="tech610-montezer-test-boto3"
)

print("Bucket deleted")