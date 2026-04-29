from sqlalchemy import text
from src.ingestion.loaders.base_loader import BaseLoader


class AgencyLoader(BaseLoader):
    """
    Handles database operations for agencies.
    """

    def __init__(self, db, logger):
        super().__init__(db, logger)

    def get_or_create(self, agency_name: str) -> int:
        """
        Get the ID of an agency or create it if it doesn't exist.

        Args:
            agency_name (str): The name of the agency.

        Returns:
            int: The ID of the agency.
        """
        query = """
            INSERT INTO agencies (agency_name)
            VALUES (:agency_name)
            ON CONFLICT (agency_name)
            DO UPDATE SET agency_name = EXCLUDED.agency_name
            RETURNING agency_id;
        """

        result = self.db.execute(query, {"agency_name": agency_name})
        return result.fetchone()[0]
