from __future__ import annotations

import os
from dataclasses import dataclass

import mysql.connector
from dotenv import load_dotenv


@dataclass
class DBConfig:
    host: str = os.getenv("MYSQL_HOST", "localhost")
    port: int = int(os.getenv("MYSQL_PORT", "3306"))
    database: str = os.getenv("MYSQL_DATABASE", "eshop_database")
    user: str = os.getenv("MYSQL_USER", "test")
    password: str = os.getenv("MYSQL_PASSWORD", "test")


def get_connection():
    """Create a MySQL connection using env vars (and .env if present)."""
    load_dotenv()
    cfg = DBConfig()
    return mysql.connector.connect(
        host=cfg.host,
        port=cfg.port,
        user=cfg.user,
        password=cfg.password,
        database=cfg.database,
    )
