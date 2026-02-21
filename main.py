from database import Database
from models.expansion import Expansion
from models.card import Card
from models.rarities import Rarity

def main():
    db_obj = Database()
    blk_blt = Expansion('BLK',"Black Bolt").to_dict()
    wht_flr = Expansion('WHT', "White Flare").to_dict()
    db_obj.add_expansion(blk_blt)
    db_obj.add_expansion(wht_flr)
    crd1 = Card("Servine", "088", "BLK",Rarity.ILLUSTRATION_RARE, 1).to_dict()
    crd2 = Card("Vanillish", "112", "WHT",Rarity.ILLUSTRATION_RARE, 1).to_dict()
    db_obj.add_new_card(crd2, True)

if __name__ == "__main__":
    main()