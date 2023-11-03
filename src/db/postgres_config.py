from config.db_config import DatabaseConfig
import os

db_config = DatabaseConfig(
    database = os.environ['DB_NAME'],
    user = os.environ['DB_USER'],
    password = os.environ['DB_PASSWORD'],
    host = os.environ['DB_HOST'],
    port = os.environ['DB_PORT']
)
