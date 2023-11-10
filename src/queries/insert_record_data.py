def insert_record_data(data):
    """
        Function to insert record data into the database
        :param data: The data to be inserted into the database
        :return: The query to insert the data into the database
    """
    
    id = data['id']
    temperature = data['temperature']
    humidity = data['humidity']
    luminosity = data['luminosity']
    timestamp = data['timestamp']
    greenhouse_id = data['greenhouse_id']

    try:
        query = f"""
            INSERT INTO core_sensorrecord (id, temperature, humidity, luminosity, timestamp, greenhouse_id)
            VALUES ('{id}', {temperature}, {humidity}, {luminosity}, '{timestamp}', '{greenhouse_id}';
        """
        return query
    except Exception as e:
        return None, f"Error inserting record data: {e}"
