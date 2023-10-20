"""SQS event processor"""
import boto3
import json

class SQSEventProcessor:
    def __init__(self):
        self.sqs = boto3.client('sqs')

    def listener(self, event):
        """AWS Lambda function handler"""
        for record in event['Records']:
            body = json.loads(record['body'])
            self.process_message(body)

    def process_message(self, message):
        """Process a message from the SQS queue"""

        return {
            'statusCode': 200,
            'body': json.dumps('Mensaje procesado'),
            'payload': {
                'greenhouse_id': message['greenhouse_id'],
                'temperature': message['temperature'],
                'humidity': message['humidity'],
                'luminosity': message['luminosity'],
                'CO2_level': message['CO2_level'],
                'soil_moisture': message['soil_moisture'],
                'pH': message['pH'],
                'nutrient_level': message['nutrient_level'],
                'timestamp': message['timestamp']
            }
        }
