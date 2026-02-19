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

def create_expansion(exp: Expansion) -> None:
    """Creates an expansion in the database"""

    conn = get_connection()
    c = conn.cursor()
    # Find if the code that is trying to be created is already in use
    c.execute("""SELECT * FROM expansions WHERE code = ?""", (exp.code,))
    if c.fetchone():
        print("This expansion already exists in the db.")
        return 
    c.execute("""INSERT INTO expansions (code,name) VALUES (?,?)""",(exp.code,exp.name))

    conn.commit()
    print(f"Expansion {exp} succesfully added into the database")
    conn.close()


if __name__ == "__main__":
    exp1 = Expansion("BLK","Black Bolt")
    create_expansion(exp1)

