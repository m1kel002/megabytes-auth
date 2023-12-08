import json
import boto3
from constants.config import CLIENT_ID


def handler(event, context):
    print(f"Event Triggered: {json.dumps(event)}")
    body = json.loads(event['body'])
    confirm_code = body['code']
    username = body['username']
    try:
        client = boto3.client('cognito-idp')
        response = client.confirm_sign_up(ClientId=CLIENT_ID,
                                          Username=username,
                                          ConfirmationCode=confirm_code)
        print(f"Confirm Signup success: {response}")
        return dict(statusCode=200,
                    body=json.dumps(
                        dict(message='User signup successfully confirmed!')))
    except Exception as err:
        print(f"Confirm Signup failed: {str(err)}")
        return dict(statusCode=500, body=json.dumps(dict(message=str(err))))
