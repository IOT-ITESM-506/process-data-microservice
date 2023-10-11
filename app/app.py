"""Script to process the SQS event and insert the data into the database"""
from db.postgres_connection import PostgresDatabase
from db.postgres_config import db_config
from services.sqs_event_processor import SQSEventProcessor
from queries.insert_data import generate_insert_query
import json

sqs_event_processor = SQSEventProcessor()

def lambda_handler(event, context):
    """
        Handler function for the Lambda function
        :param event: The event data passed to the Lambda function
        :param context: The context data passed to the Lambda function

        :return: A response object containing the status code and body
    """
    with PostgresDatabase(config=db_config) as connection:
        sqs_data = sqs_event_processor.listener(event)
        query, values = generate_insert_query(sqs_data)
        cursor = connection.cursor()
        cursor.execute(query)

        return {
            'statusCode': 200,
            'body': json.dumps('Mensaje procesado'),
        }