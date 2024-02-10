from aws_cdk import (Stack, aws_iam, aws_dynamodb as db)
from constructs import Construct
from config import STACK_FAMILY


class MegabytesStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, config,
                 **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.config = config
        self.create_ddb_tables()
        self.create_policies()
        self.create_roles()

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

    def create_policies(self):
        self.dynamo_writer = aws_iam.ManagedPolicy(
            self,
            'DynamoWriter',
            managed_policy_name=f"{STACK_FAMILY}-DynamoWriter",
            statements=[
                aws_iam.PolicyStatement(actions=[
                    'dynamodb:Query', 'dynamodb:PutItem', 'dynamodb:GetItem',
                    'dynamodb:UpdateItem'
                ],
                                        resources=[
                                            self.data_table.table_arn,
                                            self.user_table.table_arn
                                        ]),
            ])

    def create_roles(self):
        self.writer_role = aws_iam.Role(
            self,
            'WriterRole',
            role_name=f"{STACK_FAMILY}-writerRole",
            managed_policies=[self.dynamo_writer],
            assumed_by=aws_iam.ServicePrincipal('lambda.amazonaws.com'))
