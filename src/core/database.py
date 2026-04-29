import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv


class Database:
    """
    Simple PostgreSQL database wrapper using SQLAlchemy intended for
    lightweight data engineering pipelines and prototyping.
    """

    def __init__(self):
        """
        Initialize database configuration from enviornment variables.
        Connection must be established explicitly.
        """
        load_dotenv()

        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.host = os.getenv("DB_HOST")
        self.port = os.getenv("DB_PORT")
        self.db_name = os.getenv("DB_NAME")
        self.engine = None

    def connect(self):
        """
        Create a SQLAlchemy engine and establish connection configuration.

        Returns:
            sqlalchemy.Engine: Active database engine instance.
        """
        url = f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.db_name}"
        self.engine = create_engine(url)
        return self.engine

    def execute(self, query: str, params: dict = None) -> list:
        """
        Execute a SQL query against the connected database.

        Args:
            query (str): The SQL query to execute.
            params (dict, optional): Parameters for the SQL query.

        Returns:
            list: The results of the query as a list of rows.
        """
        if self.engine is None:
            raise Exception(
                "Database connection not established. Call connect() first.")

        with self.engine.connect() as conn:
            result = conn.execute(text(query), params)
            return list(result.fetchall())
