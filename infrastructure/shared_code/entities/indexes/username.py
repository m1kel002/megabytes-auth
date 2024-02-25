from pynamodb.indexes import GlobalSecondaryIndex, AllProjection
from pynamodb.attributes import UnicodeAttribute


class UsernameIndex(GlobalSecondaryIndex):

    class Meta:
        index_name = 'UsernameIndex'
        projection = AllProjection()
        read_capacity_units = 1
        write_capacity_units = 1

    username = UnicodeAttribute(hash_key=True)
