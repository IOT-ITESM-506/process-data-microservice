def generate_insert_query(data):
    columns = ", ".join(data.keys())
    placeholders = ", ".join(["%s"] * len(data))
    values = tuple(data.values())

    query = f"INSERT INTO sensor_data ({columns}) VALUES ({placeholders});"
    
    return query, values