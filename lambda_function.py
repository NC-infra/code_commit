import json

def lambda_handler(event, context):
    # Example: return a simple HTML response
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/html"
        },
        "body": "<h1>Hello from AWS Lambda!</h1><p>This is a simple Python app.</p>"
    }
