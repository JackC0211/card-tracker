from database import Database
from expansion import Expansion
from card import Card

def main():
    db_obj = Database()
    blk_blt = Expansion('BLK',"Black Bolt")
    crd1 = Card("Servine", "088", "BLK", "Art Rare", 1)
    db_obj.add_expansion(blk_blt)
    db_obj.add_new_card(crd1)

if __name__ == "__main__":
    main()