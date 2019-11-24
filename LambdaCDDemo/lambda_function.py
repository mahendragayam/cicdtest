import boto3
import json
#test code1

ec2 = boto3.client('ec2')
def lambda_handler(event, context):
    response = ec2.describe_availability_zones()
    return {"statusCode": 200, "body": json.dumps(response)}
