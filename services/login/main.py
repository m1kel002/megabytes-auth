import json
import boto3
from constants.config import USER_POOL_ID, CLIENT_ID


def handler(event, context):
    print(f"Event Triggered: {json.dumps(event)}")
    # response = {"statusCode": 200, "body": json.dumps(body)}
    body = json.loads(event['body'])
    # response = dict(statusCode=200, body=json.dumps(body))
    try:
        username = body['username']
        password = body['password']
        client = boto3.client('cognito-idp')
        response = client.admin_initiate_auth(UserPoolId=USER_POOL_ID,
                                              ClientId=CLIENT_ID,
                                              AuthFlow='ADMIN_NO_SRP_AUTH',
                                              AuthParameters={
                                                  'USERNAME': username,
                                                  'PASSWORD': password
                                              })
        print(f"login successful: {response}")
        return dict(statusCode=200, body=json.dumps(response))
    except Exception as err:
        print(f"login failed: {str(err)}")
        return dict(statusCode=500, body=str(err))
