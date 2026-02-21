import sqlite3
from typing import Any, Mapping

from expansion import Expansion

db_name = "database.db"
cardValueKeys = ("card_id","name", "number","exp_code","rarity","quantity")

def get_connection() -> sqlite3.Connection:
    """Connects to the database\n
    Returns the connection object"""
    connection_obj = sqlite3.connect(db_name)
    return connection_obj

def init_db() -> None: # creates the tables (ownedCards, expansions) in the databsae
    """Creates the expansions and cards tables"""
    
    conn = get_connection()
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS expansions (
        code TEXT PRIMARY KEY ,
        name TEXT UNIQUE
    )
    """)
    c.execute("""
    CREATE TABLE IF NOT EXISTS ownedCards (
        card_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        number TEXT NOT NULL,
        exp_code TEXT NOT NULL,
        rarity TEXT NOT NULL,
        quantity INTEGER NOT NULL DEFAULT 0,
        FOREIGN KEY (exp_code) REFERENCES expansions(code)
    )
    """)
    conn.commit()
    conn.close()
class Database:
    """Object that interacts with the database"""
    def __init__(self):
        init_db()

    def add_expansion(self, expansion: dict[str,Any]) -> None:
        """Creates an expansion in the database

        Inputs
        ------
        expansion: *dict[str:Any]* = The expansion to be added
        """
        conn = get_connection()
        c = conn.cursor()
        # Find if the code that is trying to be created is already in use
        c.execute("""SELECT * FROM expansions WHERE code = ?""", (expansion["code"],))

        if c.fetchone(): # Prevents multiple of the same set being created
            print("This expansion already exists in the db.") 
            return 
        c.execute("""INSERT INTO expansions
                  (code,name)VALUES (?,?)""",
                  (expansion["code"],expansion["name"]))

        conn.commit()
        print(f"Expansion {expansion} succesfully added into the database")

        conn.close()
        return

    def add_new_card(self, card: dict[str,Any], owned: bool):
        """Adds a new card into the database"""
        conn = get_connection()
        c = conn.cursor()

        c.execute("""SELECT * FROM expansions WHERE code = ?""", (card['exp_code'],))
        if not c.fetchone():
            print("This expansion code does not exist in the database")
            return
        
        if self.check_exists_card(newCard=card):
            return

        if owned:
            tableName = "ownedCards"
        else:
            tableName = "ownedCards" #Change this

        c.execute("""INSERT OR IGNORE INTO ?
                  (name, number, exp_code, rarity, quantity) VALUES (?,?,?,?,?)""",
                  (tableName, card['name'], card['number'], card['exp_code'], card['rarity'], card['quantity']))
        conn.commit()
        print(f"card {card['label']} succesfully added to db")
        conn.close()

    def check_exists_card(self, newCard: dict[str,Any]) -> bool:
        """Checks if a card with matching information is in the database"""
        
        conn = get_connection()
        c = conn.cursor()

        c.execute("""SELECT card_id, name, number, exp_code, rarity, quantity 
                  FROM ownedCards
                  WHERE (name, number, exp_code, rarity) = (?,?,?,?)""",
                  (newCard['name'], newCard['number'], newCard['exp_code'], newCard['rarity'])
                  )
        
        row = c.fetchone() #checks if an instance exists
        if row is None: # returns None if no instance
            print("Card does not exist")
            conn.close()
            return False
        
        similar_card = dict(zip(cardValueKeys,row)) # creates a dict of the card with info from the db

        self.increase_quantity(similar_card['quantity'], similar_card['card_id'], newCard['quantity'])

        conn.close()
        return True
        
    def increase_quantity(self, card_quantity: int, card_id: int, quantity: int):
        """Increase the quantity of a card in the database"""
        card_quantity += quantity
        conn = get_connection()
        c= conn.cursor()
        c.execute("""
                  UPDATE ownedCards
                  SET quantity = ?
                  WHERE card_id = ?""",
                  (card_quantity, card_id))
        
        print(f"Quantity of id: {card_id} increased ")
        conn.commit()
        conn.close()