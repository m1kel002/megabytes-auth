import json
import boto3
from infrastructure.config import CLIENT_ID
from infrastructure.shared_code.utils.main import make_response


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
        return make_response(
            dict(message='User signup successfully confirmed!'), 200)
    except Exception as err:
        print(f"Confirm Signup failed: {str(err)}")
        return make_response(dict(message=str(err)), 500)
