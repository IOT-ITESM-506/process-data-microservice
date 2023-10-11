import boto3
import json

class SQSEventProcessor:
    def __init__(self):
        self.sqs = boto3.client('sqs')

    def lambda_handler(self, event, context):
        """Función que AWS Lambda ejecutaría en respuesta a un nuevo mensaje"""
        
        for record in event['Records']:
            body = json.loads(record['body'])
            self.process_message(body)

    def process_message(self, message):
        """Lógica personalizada para procesar el mensaje"""

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
