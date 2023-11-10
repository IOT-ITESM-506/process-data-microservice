import json
import uuid

class SQSEventProcessor:
    def __init__(self, event):
        self.event = event

    def process_message(self):
        processed_data = {
            'id': None,
            'temperature': None,
            'humidity': None,
            'luminosity': None,
            'timestamp': None,
            'greenhouse_id': None,
        }

        records = self.event.get('Records', [])

        if records:
            record = records[0]
            message_body = record.get('body', None)

            if message_body:
                try:
                    sns_message = json.loads(message_body)                    
                    message_data = json.loads(sns_message.get('Message', '{}'))
                    processed_data.update({
                        'id': str(uuid.uuid4()),
                        'temperature': message_data.get('temperature', None),
                        'humidity': message_data.get('humidity', None),
                        'luminosity': message_data.get('luminosity', None),
                        'timestamp': message_data.get('timestamp', None),
                        'greenhouse_id': message_data.get('sensor_record_circuit_id', None),
                    })
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON: {e}")
            else:
                print("No 'body' field in the record.")

        return processed_data