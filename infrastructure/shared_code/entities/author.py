from pynamodb.attributes import UnicodeAttribute, MapAttribute


class Author(MapAttribute):
    userId = UnicodeAttribute(null=False)
    name = UnicodeAttribute(null=True)
