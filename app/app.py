
import json
import boto3

def lambda_handler(event, context):
    """Sample Lambda function to PUT an item to DynamoDB."""

    response = {
        "statusCode": 200,
        "body": json.dumps({"message": "¡Hola desde AWS Lambda!"})
    }
    
    return response