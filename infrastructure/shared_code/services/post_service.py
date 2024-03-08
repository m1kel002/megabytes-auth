from typing import Dict
from infrastructure.shared_code.entities.post import Post
from infrastructure.shared_code.services.user_service import UserService


class PostService():

    @classmethod
    def create(cls, params: dict) -> Post:
        params.update(dict(upvote=0, downvote=0))
        post = Post(**params)
        post.update_fields()
        post.save()
        return post

    @classmethod
    def get(cls, id: str):
        return Post.get(id, Post.category_name())

    @classmethod
    def get_posts(cls):
        return list(Post.scan())

    @classmethod
    def to_response(cls, entity: Post):
        return dict(id=entity.id,
                    message=entity.message,
                    upvote=entity.upvote,
                    downvote=entity.downvote,
                    createdAt=str(entity.createdAt),
                    author=cls.get_author_details(entity.createdById))

    @classmethod
    def get_author_details(cls, user_id: str) -> Dict:
        user_info = UserService.get(user_id)
        return dict(userId=user_info.id,
                    name=f'{user_info.firstName} {user_info.lastName}')
