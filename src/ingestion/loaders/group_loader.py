from sqlalchemy import text


class GroupLoader:
    """
    Handles database operations for groups.
    """

    def __init__(self, db):
        self.db = db

    def upsert(self, group: dict) -> int:
        """
        Insert or update a group and return its group_id.

        Args:
            group (dict): A dictionary containing group data.

        Returns:
            int: The group_id of the inserted or updated group.
        """

        query = text("""
            INSERT INTO groups (name, agency_id, debut_date)
            VALUES (:name, :agency_id, :debut_date)
            ON CONFLICT (name)
            DO UPDATE SET
                agency_id = EXCLUDED.agency_id,
                debut_date = EXCLUDED.debut_date
            RETURNING group_id; 
        """)

        result = self.db.execute(query, group)

        # Fetch the returned id
        row = result.fetchone()
        return row[0]
