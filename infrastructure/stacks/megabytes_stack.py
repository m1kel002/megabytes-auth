from aws_cdk import (Stack, aws_dynamodb as db)
from constructs import Construct


class MegabytesStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, config,
                 **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.config = config
        self.create_ddb_tables()

    def create_ddb_tables(self):
        self.user_table = db.Table(
            self,
            id=f"{self.config.STACK_FAMILY}-users",
            table_name=f"{self.config.STACK_FAMILY}-users",
            partition_key=db.Attribute(name='id',
                                       type=db.AttributeType.STRING),
            sort_key=db.Attribute(name='category',
                                  type=db.AttributeType.STRING))

        self.data_table = db.Table(
            self,
            id=f"{self.config.STACK_FAMILY}-data",
            table_name=f"{self.config.STACK_FAMILY}-data",
            partition_key=db.Attribute(name='id',
                                       type=db.AttributeType.STRING),
            sort_key=db.Attribute(name='category',
                                  type=db.AttributeType.STRING))
