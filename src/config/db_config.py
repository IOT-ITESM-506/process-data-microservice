"""Database configuration module."""
from dataclasses import dataclass

@dataclass
class DatabaseConfig:
    database: str
    user: str
    password: str
    host: str
    port: str