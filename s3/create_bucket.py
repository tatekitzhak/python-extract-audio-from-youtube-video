import boto3
import os
import datetime
from dotenv import load_dotenv
load_dotenv()


S3_ACCESS_KEY =  os.getenv("S3AccessKeyID")
s3_SECRET_KEY =  os.getenv("S3SecretAccessKey")




def make_bucket():
	#  access all s3 resources 
	s3_client = boto3.client('s3',aws_access_key_id=S3_ACCESS_KEY,aws_secret_access_key=s3_SECRET_KEY)

	time_now = datetime.datetime.now()
	year = '{:02d}'.format(time_now.year)
	month = '{:02d}'.format(time_now.month)
	day = '{:02d}'.format(time_now.day)
	hour = '{:02d}'.format(time_now.hour)
	minute = '{:02d}'.format(time_now.minute)

	current_time = '{}-{}-{}-{}-{}'.format(year, month, day, hour, minute)
	print('ctxt'+current_time)
	response = s3_client.create_bucket(ACL='private',Bucket='ctxt{}'.format(current_time),CreateBucketConfiguration={'LocationConstraint': 'us-east-2'})
	print('ctxt:',response)

make_bucket()