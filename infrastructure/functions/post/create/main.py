import json
from infrastructure.shared_code.services.post_service import PostService
from infrastructure.shared_code.utils.main import make_response


def handler(event, context):
    print(f'Event Triggered: {event}')
    post_params = json.loads(event['body'])
    post = PostService.create(post_params)
    formatted_post = PostService.to_response(post)
    return make_response(formatted_post, 201)
