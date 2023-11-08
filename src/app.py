"""Script to process the SQS event and insert the data into the database"""
import json
from services.sqs_event_processor import SQSEventProcessor
from db.postgres_config import db_config
from db.postgres_connection import PostgresDatabase


def handler(event, context):
    """
        Handler function for the Lambda function
        :param event: The event data passed to the Lambda function
        :param context: The context data passed to the Lambda function

        :return: A response object containing the status code and body
    """
    sqs_event_processor = SQSEventProcessor(event)

    with PostgresDatabase(db_config) as connection:
        cursor = connection.cursor()
        data = cursor.execute("SELECT * FROM core_user;")

        processed_data = sqs_event_processor.process_message()
        print('Data from database: ', data)
        print('Processed data: ', processed_data)
       
    return {
        'statusCode': 200,
        'body': json.dumps('AWS Lambda SQS event processed successfully!')
    }