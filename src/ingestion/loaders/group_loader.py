from sqlalchemy import text
from src.ingestion.loaders.base_loader import BaseLoader


class GroupLoader(BaseLoader):
    """
    Handles database operations for groups.
    """

    def __init__(self, db, logger):
        super().__init__(db, logger)

    def upsert(self, data: dict) -> int:
        """
        Insert or update a group and return its group_id.

        Args:
            data (dict): A dictionary containing group data.

        Returns:
            int: The group_id of the inserted or updated group.
        """

        query = text("""
            INSERT INTO groups (group_name, agency_id, debut_date)
            VALUES (:group_name, :agency_id, :debut_date)
            ON CONFLICT (group_name)
            DO UPDATE SET
                agency_id = EXCLUDED.agency_id,
                debut_date = EXCLUDED.debut_date
            RETURNING group_id; 
        """)

        result = self.db.execute(query, data)

        # Fetch the returned id
        row = result.fetchone()
        return row[0]
