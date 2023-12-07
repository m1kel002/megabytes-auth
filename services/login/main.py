import json

def handler(event, context):
    print(f"Event Triggered: {event}")
    # response = {"statusCode": 200, "body": json.dumps(body)}
    body = dict(message="hello world")
    response = dict(statusCode=200, body=json.dumps(body))
    return response

    
