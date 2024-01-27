import os


def get_env(var_name: str):
    value = os.getenv(var_name)
    if value is None:
        raise RuntimeError(f"{var_name} does not exists")
    return value


CLIENT_ID = get_env('CLIENT_ID')
USER_POOL_ID = get_env('USER_POOL_ID')
STAGE = get_env('STAGE')
ACCOUNT_NAME = get_env('ACCOUNT_NAME')
REGION = get_env('REGION')
STACK_FAMILY = get_env('STACK_FAMILY')
ACCOUNT_ID = get_env('ACCOUNT_ID')
