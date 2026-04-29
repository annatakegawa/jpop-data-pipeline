import os
from pathlib import Path
from src.core.database import Database
from sqlalchemy import text


def load_sql_files(sql_dir: Path):
    files = sorted([p for p in sql_dir.iterdir() if p.suffix == '.sql'])
    for f in files:
        yield f


def main():
    root = Path(__file__).resolve().parents[2]
    sql_dir = root / 'sql'

    if not sql_dir.exists():
        print(f"SQL directory not found: {sql_dir}")
        return

    db = Database()
    engine = db.connect()

    for sql_file in load_sql_files(sql_dir):
        print(f"Applying: {sql_file.name}")
        sql = sql_file.read_text()
        # exec_driver_sql handles multiple statements in a file
        with engine.begin() as conn:
            conn.exec_driver_sql(sql)

    print("Schema applied.")


if __name__ == '__main__':
    main()
