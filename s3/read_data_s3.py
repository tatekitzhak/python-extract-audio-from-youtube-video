import boto3
import os
from dotenv import load_dotenv
load_dotenv()


S3_ACCESS_KEY =  os.getenv("S3AccessKeyID")
s3_SECRET_KEY =  os.getenv("S3SecretAccessKey")

#  access all s3 resources 
client = boto3.client('s3',aws_access_key_id=S3_ACCESS_KEY,aws_secret_access_key=s3_SECRET_KEY)

response = client.get_object(Bucket='ctxt-1',Key='file/test.txt')

print(response['Body'].read())