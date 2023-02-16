import boto3
import os
from dotenv import load_dotenv
load_dotenv()


S3_ACCESS_KEY =  os.getenv("S3AccessKeyID")
s3_SECRET_KEY =  os.getenv("S3SecretAccessKey")

#  access all s3 resources 
client = boto3.client('s3',aws_access_key_id=S3_ACCESS_KEY,aws_secret_access_key=s3_SECRET_KEY)

# create directory and upload file
for file in os.listdir():
	if '.txt' in file:
		upload_file_bucket = 'ctxt-1' # bucket name - container that holde objects
		upload_file_key = 'file/'+str(file) # folder_name/file_name (objects name)
		client.upload_file(file,upload_file_bucket,upload_file_key) # create a folder and upload files (objects)

on
on Tuesday morning
on Saturday mornings
on Sunday afternoon(s)
on Monday evening(s)



