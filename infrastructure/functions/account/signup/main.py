import json
from infrastructure import config
import boto3
from infrastructure.shared_code.utils.main import make_response
from infrastructure.shared_code.services.user_service import UserService


def handler(event, context):
    print(f"Event signup triggered: ", json.dumps(event))
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
                'Name':
                'name',
                'Value':
                f"{body['firstName']} {body['lastName']}"
            }]
        }

        client = boto3.client('cognito-idp')
        response = client.sign_up(**kwargs)
        print(f"SIGNUP RESPONSE: {response}")
        user_params = dict(username=body['username'],
                           gender=body['gender'],
                           birthdate=body['birthdate'],
                           firstName=body['firstName'],
                           lastName=body['lastName'],
                           email=body['email'])
        UserService.create(user_params)
        return make_response({'message': 'Successfully signed up!'}, 200)
    except Exception as err:
        print(f"ERROR: {str(err)}")
        return make_response({'message': str(err)}, 500)
