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
    return {'statusCode': code, 'body': json.dumps(body)}
    

# try:
#             kwargs = {
#                 "ClientId": self.client_id,
#                 "Username": user_name,
#                 "Password": password,
#                 "UserAttributes": [{"Name": "email", "Value": user_email}],
#             }
#             if self.client_secret is not None:
#                 kwargs["SecretHash"] = self._secret_hash(user_name)
#             response = self.cognito_idp_client.sign_up(**kwargs)
#             confirmed = response["UserConfirmed"]
#         except ClientError as err:
#             if err.response["Error"]["Code"] == "UsernameExistsException":
#                 response = self.cognito_idp_client.admin_get_user(
#                     UserPoolId=self.user_pool_id, Username=user_name
#                 )
#                 logger.warning(
#                     "User %s exists and is %s.", user_name, response["UserStatus"]
#                 )
#                 confirmed = response["UserStatus"] == "CONFIRMED"
#             else:
#                 logger.error(
#                     "Couldn't sign up %s. Here's why: %s: %s",
#                     user_name,
#                     err.response["Error"]["Code"],
#                     err.response["Error"]["Message"],
#                 )
#                 raise
#         return confirmed
