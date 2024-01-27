import aws_cdk as cdk
import config

from stacks.megabytes_stack import MegabytesStack

app = cdk.App()

env = dict(account=config.ACCOUNT_ID, region=config.REGION)

MegabytesStack(app, f"{config.STACK_FAMILY}-service", config=config, env=env)

app.synth()
