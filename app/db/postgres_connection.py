import psycopg2
from psycopg2 import OperationalError
from db.postgres_config import DatabaseConfig

class PostgresDatabase:
    def __init__(self, config: DatabaseConfig):
        self.config = config
        self._connection = None

    def __enter__(self):
        try:
            self._connection = psycopg2.connect(
                database=self.config.database,
                user=self.config.user,
                password=self.config.password,
                host=self.config.host,
                port=self.config.port,
            )
        except OperationalError as e:
            print(f"The error '{e}' occurred")
            raise

        return self._connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._connection is not None:
            self._connection.close()
