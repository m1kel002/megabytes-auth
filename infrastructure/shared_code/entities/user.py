from pynamodb.attributes import UnicodeAttribute
from infrastructure.shared_code.entities.entity import Entity
from infrastructure.config import STACK_FAMILY
import uuid


class User(Entity):

    class Meta:
        table_name = f'{STACK_FAMILY}-users'
        region = 'ap-southeast-1'

    username = UnicodeAttribute(null=True)
    firstName = UnicodeAttribute(null=True)
    lastName = UnicodeAttribute(null=True)
    gender = UnicodeAttribute(null=True)
    birthdate = UnicodeAttribute(null=True)
    email = UnicodeAttribute(null=True)

    def category_name(self):
        return 'user'

    def update_fields(self):
        id = str(uuid.uuid4())
        self.uniqueId = id
        self.id = id
        self.category = self.category_name()
