import json

def handler(event, context):
    body = dict(message="GET PROFILE")
    response = dict(statusCode=200, body=json.dumps(body))
    return response