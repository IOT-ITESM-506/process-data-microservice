def insert_record_data(data):
    try:
        """
            :param data: The data to be inserted into the database
            :return: A tuple containing the query and values to be inserted into the database
        """
        query = """
            INSERT INTO core_sensor_record (temperature, humidity, luminosity, CO2_level, soil_moisture, pH, nutrient_level, timestamp, greenhouse_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, (SELECT id FROM greenhouse WHERE name=%s));
        """
        values = (
            data['temperature'],
            data['humidity'],
            data['luminosity'],
            data['CO2_level'],
            data['soil_moisture'],
            data.get('pH', None),
            data.get('nutrient_level', None),
            data.get('timestamp', None),
            data['greenhouse_name']
        )
        return query, values
    except Exception as e:
        return None, f"Error inserting record data: {e}"