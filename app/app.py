"""Script to process the SQS event and insert the data into the database"""
import json
from services.sqs_event_processor import SQSEventProcessor

def handler(event, context):
    """
        Handler function for the Lambda function
        :param event: The event data passed to the Lambda function
        :param context: The context data passed to the Lambda function

        :return: A response object containing the status code and body
    """
    sqs_event_processor = SQSEventProcessor(event)
    processed_data = sqs_event_processor.process_message()

    print('Processed data: {}'.format(processed_data))
    
    return {
        'statusCode': 200,
        'body': json.dumps('AWS Lambda function executed successfully!')
    }
    