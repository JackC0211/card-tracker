from database import Database
from expansion import Expansion

def main():
    db_obj = Database()
    blk_blt = Expansion('BLK',"Black Bolt")
    db_obj.add_expansion(blk_blt)


if __name__ == "__main__":
    main()