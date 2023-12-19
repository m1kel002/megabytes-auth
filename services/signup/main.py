import json
from constants import config
import boto3


def handler(event, context):
    print(f"Event signup triggered", json.dumps(event))
    body = json.loads(event['body'])

    try:
        kwargs = {
            'ClientId':
            config.CLIENT_ID,
            'Username':
            body['username'],
            'Password':
            body['password'],
            'UserAttributes': [{
                'Name': 'email',
                'Value': body['email']
            }, {
                'Name': 'gender',
                'Value': body['gender']
            }, {
                'Name': 'birthdate',
                'Value': body['birthdate']
            }, {
                'Name': 'name',
                'Value': body['name']
            }]
        }

        client = boto3.client('cognito-idp')
        response = client.sign_up(**kwargs)
        print(f"SIGNUP RESPONSE: {response}")
        return make_response({'message': 'Successfully signed up!'}, 200)
    except Exception as err:
        print(f"ERROR: {str(err)}")
        return make_response({'message': str(err)}, 500)

def make_response(body: dict, code: int):
    return {
        'statusCode': code,
        'body': json.dumps(body),
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True
        }
    }
