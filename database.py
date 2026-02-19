import sqlite3
from expansion import Expansion

db_name = "database.db"



def get_connection() -> sqlite3.Connection:
    connection_obj = sqlite3.connect(db_name)
    return connection_obj

def init_db():
    """Creates the expansions and cards tables"""
    
    conn = get_connection()
    c = conn.cursor()

    # check if any table in db exists
    listOfTables = c.execute("""SELECT count(*) FROM sqlite_master WHERE type='table' AND name='cards' or name='expansions'; """).fetchall()
    if listOfTables != []:
        conn.close()
        return

    create_expansions_table = """CREATE TABLE IF NOT EXISTS expansions (
    code TEXT PRIMARY KEY ,
    name TEXT UNIQUE
    )
    """
    create_cards_table = """CREATE TABLE IF NOT EXISTS cards (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        number TEXT NOT NULL,
        exp_code TEXT NOT NULL,
        FOREIGN KEY (exp_code) REFERENCES expansions(code)
        )
    """


    c.execute(create_expansions_table)
    print("exp table init")
    c.execute(create_cards_table)
    print("card table created")

    conn.commit()
    conn.close()
class Database:
    def __init__(self):
        init_db()
        self.conn = get_connection()


    def create_expansion(self, exp: Expansion) -> None:
        """Creates an expansion in the database"""

        c = self.conn.cursor()
        # Find if the code that is trying to be created is already in use
        c.execute("""SELECT * FROM expansions WHERE code = ?""", (exp.code,))
        if c.fetchone():
            print("This expansion already exists in the db.")
            return 
        c.execute("""INSERT INTO expansions (code,name) VALUES (?,?)""",(exp.code,exp.name))

        self.conn.commit()
        print(f"Expansion {exp} succesfully added into the database")
        self.conn.close()


if __name__ == "__main__":
    exp1 = Expansion("BLK","Black Bolt")
    db = Database()
    db.create_expansion(exp1)

