import json
from infrastructure.shared_code.utils.main import make_response
from infrastructure.shared_code.services.user_service import UserService


def handler(event, context):
    print(f'Event Triggered: {json.dumps(event)}')
    query_params = event['queryStringParameters']
    username = query_params['username']
    user = UserService.get_user_by_username(username)
    user_info = UserService.to_simple_response(user)
    return make_response(body=user_info, code=200)
