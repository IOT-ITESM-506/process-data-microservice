import json
import boto3

def lambda_handler(event, context):
    """
        Handler function for the Lambda function
        :param event: The event data passed to the Lambda function
        :param context: The context data passed to the Lambda function

        :return: A response object containing the status code and body
    """

    response = {
        "statusCode": 200,
        "body": json.dumps({"message": "¡Hola desde AWS Lambda!"})
    }
    
    return response