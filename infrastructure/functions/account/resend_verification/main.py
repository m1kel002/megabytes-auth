import json
import boto3
from infrastructure.config import CLIENT_ID


def handler(event, context):
    print(f"Event Triggered: {json.dumps(event)}")
    body = json.loads(event['body'])
    username = body['username']
    client = boto3.client('cognito-idp')
    try:
        response = client.resend_confirmation_code(ClientId=CLIENT_ID,
                                                   Username=username)
        print(f"Successfully resent confirmation code")
        return dict(
            statusCode=200,
            body=json.dumps(
                dict(message='Confirmation Code resent. Check your email.')))
    except Exception as err:
        print(f"Failed to resend confirmation code: {str(err)}")
        return dict(statusCode=500, body=json.dumps(dict(message=str(err))))
