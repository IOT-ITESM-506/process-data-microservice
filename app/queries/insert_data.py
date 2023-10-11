def insert_data_into_db(name: str):
    return """
INSERT INTO users (name) VALUES ('{}')

"""