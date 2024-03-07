import json
from infrastructure.shared_code.services.post_service import PostService
from infrastructure.shared_code.utils.main import make_response


def handler(event, context):
    print(f'Event Triggered: {json.dumps(event)}')
    body = json.loads(event['body'])
    try:
        message = body['message']
        user_id = body['userId']
    except KeyError as err:
        return make_response(dict(message=str(err)), 400)
    post_params = dict(message=message, createdById=user_id)
    post = PostService.create(post_params)
    formatted_post = PostService.to_response(post)
    return make_response(formatted_post, 201)
