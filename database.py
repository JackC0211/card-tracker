import sqlite3
from expansion import Expansion

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

def get_connection() -> sqlite3.Connection:
    connection_obj = sqlite3.connect(db_name)
    return connection_obj

def init_db():
    conn = get_connection()
    c = conn.cursor()
    
    c.execute(expansions_table)
    print("exp init")
    c.execute(cards_table)
    print("cards init")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()

