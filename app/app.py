"""Script to process the SQS event and insert the data into the database"""
import json
from services.sqs_event_processor import SQSEventProcessor

sqs_processor = SQSEventProcessor()

def handler(event, context):
    """
        Handler function for the Lambda function
        :param event: The event data passed to the Lambda function
        :param context: The context data passed to the Lambda function

        :return: A response object containing the status code and body
    """
    try:
        data = sqs_processor.listener(event)
        print('Mensaje procesado', data)
        return {
            'statusCode': 200,
            'body': json.dumps('Mensaje procesado')
        }
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': json.dumps('Error al procesar el mensaje')
        }