import json

from infrastructure.shared_code.utils.main import make_response
from infrastructure.shared_code.services.post_service import PostService


def handler(event, context):
    print(f'Event Triggered {json.dumps(event)}')
    posts = list(
        PostService.to_response(post) for post in PostService.get_posts())
    print(f'{posts}')
    return make_response(posts, 200)
