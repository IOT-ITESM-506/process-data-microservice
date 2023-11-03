import json

class SQSEventProcessor:
    def __init__(self, event):
        self.event = event

    def process_message(self):
        processed_data = {
            'temperature': None,
            'humidity': None,
            'luminosity': None,
            'co2_level': None,
            'soil_moisture': None,
            'ph': None,
            'nutrient_level': None,
            'timestamp': None,
            'sensor_record_circuit_id': None,
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
                        'temperature': message_data.get('temperature', None),
                        'humidity': message_data.get('humidity', None),
                        'luminosity': message_data.get('luminosity', None),
                        'co2_level': message_data.get('co2_level', None),
                        'soil_moisture': message_data.get('soil_moisture', None),
                        'ph': message_data.get('ph', None),
                        'nutrient_level': message_data.get('nutrient_level', None),
                        'timestamp': message_data.get('timestamp', None),
                        'sensor_record_circuit_id': message_data.get('sensor_record_circuit_id', None),
                    })
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON: {e}")
            else:
                print("No 'body' field in the record.")

        return processed_data