import json


def make_response(body: dict, code: int):
    return {
        'statusCode': code,
        'body': json.dumps(body),
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True
        }
    }
