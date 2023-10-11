from db.postgres_connection import PostgresDatabase
from db.postgres_config import db_config

def lambda_handler(event, context):
    """
        Handler function for the Lambda function
        :param event: The event data passed to the Lambda function
        :param context: The context data passed to the Lambda function

        :return: A response object containing the status code and body
    """
    with PostgresDatabase(config=db_config) as connection:
        cursor = connection.cursor()
        

        cursor.execute("SELECT * FROM USERS;")
        version = cursor.fetchone()
        print(f"PostgreSQL version: {version}")
    