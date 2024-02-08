from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute
from config import STACK_FAMILY


class Entity(Model):

    class Meta:
        table_name = f'{STACK_FAMILY}-data'
        region = 'ap-southeast-1'

    id = UnicodeAttribute(hash_key=True)
    category = UnicodeAttribute(range_key=True)
    createdAt = UnicodeAttribute(null=True)
    updatedAt = UnicodeAttribute(null=True)
