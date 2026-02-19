import sqlite3
db_name = "database.db"


expansions_table = """CREATE TABLE IF NOT EXISTS expansions (
    code TEXT PRIMARY KEY ,
    name TEXT UNIQUE
    )
"""
cards_table = """CREATE TABLE IF NOT EXISTS cards (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    number TEXT NOT NULL,
    exp_code TEXT NOT NULL,
    FOREIGN KEY (exp_code) REFERENCES expansions(code)
    )
"""
def connect_db() -> sqlite3.Cursor:
    connection_obj = sqlite3.connect(db_name)
    cursor_obj = connection_obj.cursor()
    return cursor_obj

def init_db():
    c = connect_db()
    c.execute(expansions_table)
    print("exp init")
    c.execute(cards_table)
    print("cards init")
    print("fully init")

if __name__ == "__main__":
    init_db()