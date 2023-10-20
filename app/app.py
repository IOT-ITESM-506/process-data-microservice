"""Script to process the SQS event and insert the data into the database"""
import json

def lambda_handler(event, context):
    """
        Handler function for the Lambda function
        :param event: The event data passed to the Lambda function
        :param context: The context data passed to the Lambda function

        :return: A response object containing the status code and body
    """
    print('Event: ', event)
    return {
        'statusCode': 200,
        'body': json.dumps('Mensaje procesado'),
    }