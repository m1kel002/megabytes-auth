from pynamodb.attributes import UnicodeAttribute, UTCDateTimeAttribute
from shared_code.entities.entity import Entity
from config import STACK_FAMILY


class User(Entity):

    class Meta:
        table_name = f'{STACK_FAMILY}-data'
        region = 'ap-southeast-1'

    username: UnicodeAttribute(null=True)
    first_name: UnicodeAttribute(null=True)
    last_name: UnicodeAttribute(null=True)
    gender: UnicodeAttribute(null=True)
    birthdate: UnicodeAttribute(null=True)
    email: UnicodeAttribute(null=True)
