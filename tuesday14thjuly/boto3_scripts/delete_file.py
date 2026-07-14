import boto3

s3 = boto3.client("s3")

s3.delete_object(
    Bucket="tech610-montezer-test-boto3",
    Key="test.txt"
)

print("File deleted")