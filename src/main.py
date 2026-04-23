from database.database import Database


def test_connection():
    """
    Simple test function to verify database connection and query execution.
    """
    db = Database()
    db.connect()

    result = db.execute("SELECT 1;")
    print(f"DB Connected: {result}")


if __name__ == "__main__":
    test_connection()
