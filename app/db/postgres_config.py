from config.db_config import DatabaseConfig
import os

db_config = DatabaseConfig(
    database = 'postgres',
    user = 'edu',
    password = 'T3rraPass2023',
    host = 'education.ccsdodpf4r0e.us-east-1.rds.amazonaws.com',
    port = '5432'
)
