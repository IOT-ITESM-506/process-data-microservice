def insert_record_data(data):
    try:
        query = """
            INSERT INTO core_sensorrecord (id, temperature, humidity, luminosity, timestamp, greenhouse_id)
            VALUES (%s, %s, %s, %s, %s, %s);
        """

        values = (
            data['id'],
            data['temperature'],
            data['humidity'],
            data['luminosity'],
            data['timestamp'],
            data['sensor_record_circuit_id']
        )
        return query, values
    except Exception as e:
        return None, f"Error inserting record data: {e}"
