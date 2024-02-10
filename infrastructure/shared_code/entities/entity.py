from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, UTCDateTimeAttribute
from infrastructure.config import STACK_FAMILY


class Entity(Model):

    class Meta:
        table_name = f'{STACK_FAMILY}-data'
        region = 'ap-southeast-1'

    id = UnicodeAttribute(hash_key=True)
    category = UnicodeAttribute(range_key=True)
    createdAt = UTCDateTimeAttribute(null=True)
    updatedAt = UTCDateTimeAttribute(null=True)
    uniqueId = UnicodeAttribute(null=False)
