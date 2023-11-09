def insert_record_data(data):
    try:
        query = """
            INSERT INTO core_sensorrecord (id, temperature, humidity, luminosity, timestamp, greenhouse_id)
            VALUES (%s, %s, %s, %s, %s, %s);
        """
        return query
    except Exception as e:
        return None, f"Error inserting record data: {e}"
