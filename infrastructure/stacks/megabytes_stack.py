from aws_cdk import (Stack, aws_iam, aws_dynamodb as db)
from constructs import Construct
from config import STACK_FAMILY, REGION, PROJECT_NAME, STAGE


class MegabytesStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, config,
                 **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.config = config
        self.create_ddb_tables()
        self.add_global_secondary_index()
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

    def add_global_secondary_index(self):
        self.user_table.add_global_secondary_index(
            index_name='UsernameIndex',
            read_capacity=1,
            write_capacity=1,
            projection_type=db.ProjectionType.ALL,
            partition_key=db.Attribute(name='username',
                                       type=db.AttributeType.STRING))

    def create_policies(self):
        self.cognito_authenticator = aws_iam.ManagedPolicy(
            self,
            'CognitoAuthenticator',
            managed_policy_name=f"{STACK_FAMILY}-CognitoAuthenticator",
            statements=[
                aws_iam.PolicyStatement(actions=[
                    'cognito-idp:AdminInitiateAuth',
                    'cognito-idp:AdminCreateUser',
                    'cognito-idp:AdminSetUserPassword'
                ],
                                        resources=['*'])
            ])
        self.dynamo_writer = aws_iam.ManagedPolicy(
            self,
            'DynamoWriter',
            managed_policy_name=f"{STACK_FAMILY}-DynamoWriter",
            statements=[
                aws_iam.PolicyStatement(actions=[
                    'dynamodb:Query', 'dynamodb:PutItem', 'dynamodb:GetItem',
                    'dynamodb:UpdateItem', 'dynamodb:Scan'
                ],
                                        resources=[
                                            self.data_table.table_arn,
                                            self.user_table.table_arn
                                        ]),
            ])

        self.dynamo_reader = aws_iam.ManagedPolicy(
            self,
            'DynamoReader',
            managed_policy_name=f"{STACK_FAMILY}-DynamoReader",
            statements=[
                aws_iam.PolicyStatement(
                    actions=[
                        'dynamodb:Query', 'dynamodb:Scan', 'dynamodb:GetItem'
                    ],
                    resources=[
                        self.data_table.table_arn,
                        f'{self.data_table.table_arn}/index/*',
                        self.user_table.table_arn,
                        f'{self.user_table.table_arn}/index/*'
                    ])
            ])

        self.logger = aws_iam.ManagedPolicy(
            self,
            'LogsWriter',
            managed_policy_name=f"{STACK_FAMILY}-Logger",
            statements=[
                aws_iam.PolicyStatement(
                    actions=[
                        'logs:CreateLogStream', 'logs:CreateLogGroup',
                        'logs:PutLogEvents'
                    ],
                    resources=[
                        '*'
                        #    'arn:aws:logs:ap-southeast-1:462813044872:log-group:/aws/lambda/megabytes-auth-dev*:*',
                        # 'arn:aws:logs:{REGION}:log-group:/aws/lambda/{PROJECT_NAME}-auth-{STAGE}*:*'
                    ])
            ])

    def create_roles(self):
        self.cognito_authenticator_role = aws_iam.Role(
            self,
            'AuthenticatorRole',
            role_name=f'{STACK_FAMILY}-authenticatorRole',
            managed_policies=[
                self.dynamo_reader, self.logger, self.cognito_authenticator
            ],
            assumed_by=aws_iam.ServicePrincipal('lambda.amazonaws.com'))

        self.writer_role = aws_iam.Role(
            self,
            'WriterRole',
            role_name=f"{STACK_FAMILY}-writerRole",
            managed_policies=[self.dynamo_writer, self.logger],
            assumed_by=aws_iam.ServicePrincipal('lambda.amazonaws.com'))

        self.reader_role = aws_iam.Role(
            self,
            'ReaderRole',
            role_name=f"{STACK_FAMILY}-readerRole",
            managed_policies=[self.dynamo_reader, self.logger],
            assumed_by=aws_iam.ServicePrincipal('lambda.amazonaws.com'))
