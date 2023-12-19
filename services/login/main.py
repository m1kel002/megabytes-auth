import json
import boto3
from botocore.exceptions import ClientError
from constants.config import USER_POOL_ID, CLIENT_ID


def handler(event, context):
    print(f"Event Triggered: {json.dumps(event)}")
    body = json.loads(event['body'])
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
        return make_response(json.dumps(response), 200)

    except ClientError as ufe:
        print(f"User does not exist {str(ufe)}")
        return make_response(body=json.dumps(
            dict(message='User does not exists')),
                             status_code=400)
    except Exception as err:
        print(f"login failed: {str(err)}")
        return make_response(body=json.dumps(body), status_code=500)


def make_response(body: str, status_code: int):
    return {
        'statusCode': status_code,
        'body': body,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True
        }
    }
