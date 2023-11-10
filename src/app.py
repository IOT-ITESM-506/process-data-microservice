"""Script to process the SQS event and insert the data into the database"""
import json
from services.sqs_event_processor import SQSEventProcessor
from db.postgres_config import db_config
from db.postgres_connection import PostgresDatabase
from queries.insert_record_data import insert_record_data

import uuid

def handler(event, context):
    """
        Handler function for the Lambda function
        :param event: The event data passed to the Lambda function
        :param context: The context data passed to the Lambda function

        :return: A response object containing the status code and body
    """
    sqs_event_processor = SQSEventProcessor(event)

    try:
        with PostgresDatabase(db_config) as connection:
            cursor = connection.cursor()
            processed_data = sqs_event_processor.process_message()
            processed_data['id'] = str(uuid.uuid4())

            insert_record_data_query = insert_record_data(processed_data)

            print('Inserting record data: ', insert_record_data_query)

            cursor.execute(insert_record_data_query)
            connection.commit()


            return {
                'statusCode': 200,
                'body': json.dumps({'message': 'Record inserted successfully'})
            }

    except Exception as e:
        print('Error: ', e)
        raise e