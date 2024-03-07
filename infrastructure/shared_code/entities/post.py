import uuid
from pynamodb.attributes import UnicodeAttribute, NumberAttribute
from infrastructure.shared_code.entities.entity import Entity
from infrastructure.config import REGION, STACK_FAMILY
from infrastructure.shared_code.utils.main import now


class Post(Entity):

    class Meta:
        table_name = f'{STACK_FAMILY}-data'
        region = REGION

    message = UnicodeAttribute(null=True)
    upvote = NumberAttribute(null=True, default=0)
    downvote = NumberAttribute(null=True, default=0)
    createdById = UnicodeAttribute(null=True)

    def category_name(self):
        return 'post'

    def update_fields(self):
        id = str(uuid.uuid4())
        self.uniqueId = id
        self.id = id
        self.category = self.category_name()
        self.createdAt = now()
