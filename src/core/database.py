import os
from pathlib import Path
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from dotenv import load_dotenv


class DatabaseError(RuntimeError):
    """Raised when a database connection or query fails."""


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

        # Load .env variables from file if not in a containerized environment
        project_root = Path(__file__).resolve().parents[2]
        in_container = Path("/.dockerenv").exists() or os.getenv(
            "REMOTE_CONTAINERS"
        ) == "true"

        if not in_container:
            load_dotenv(dotenv_path=project_root / ".env", override=True)

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

    def execute(self, query: str, params: dict | None = None) -> list:
        """
        Execute a SQL query against the connected database.

        Args:
            query (str): The SQL query to execute.
            params (dict, optional): Parameters for the SQL query.

        Returns:
            list: The results of the query as a list of rows.
        """
        if self.engine is None:
            raise DatabaseError(
                "Database connection not established. Call connect() first."
            )

        try:
            with self.engine.begin() as conn:
                result = conn.execute(text(query), params)
                if result.returns_rows:
                    return list(result.fetchall())
                return []
        except SQLAlchemyError as exc:
            raise DatabaseError(f"Database query failed: {exc}") from exc
