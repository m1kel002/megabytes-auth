import aws_cdk as cdk
import config

from stacks.megabytes_stack import MegabytesStack

app = cdk.App()

env = dict(account=config.ACCOUNT_ID, region=config.REGION)

MegabytesStack(
    app,
    f"{config.STACK_FAMILY}-service",
    config=config,
    env=env

    # Uncomment the next line if you know exactly what Account and Region you
    # want to deploy the stack to. */

    #env=cdk.Environment(account='123456789012', region='us-east-1'),

    # For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html
)

app.synth()
