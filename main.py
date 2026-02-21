from database import Database
from expansion import Expansion
from card import Card

def main():
    db_obj = Database()
    # blk_blt = Expansion('BLK',"Black Bolt")
    # wht_flr = Expansion('WHT', "White Flare")
    # db_obj.add_expansion(blk_blt)
    # db_obj.add_expansion(wht_flr)
    crd1 = Card("Servine", "088", "BLK", "Art Rare", 0)
    crd2 = Card("Vanillish", "112", "WHT", "Art Rare", 0)
    db_obj.add_new_card(crd2.to_dict(), True)

if __name__ == "__main__":
    main()