from sqlalchemy import text


class AgencyLoader:
    """
    Handles database operations for agencies.
    """

    def __init__(self, db):
        self.db = db

    def get_or_create(self, agency_name: str) -> int:
        """
        Get the ID of an agency or create it if it doesn't exist.

        Args:
            agency_name (str): The name of the agency.

        Returns:
            int: The ID of the agency.
        """
        query = text("""
            INSERT INTO agencies (name)
            VALUES (:name)
            ON CONFLICT (name)
            DO UPDATE SET name = EXCLUDED.name
            RETURNING agency_id;
        """)

        result = self.db.execute(query, {"name": agency_name})
        return result.fetchone()[0]
