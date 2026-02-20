from dataclasses import dataclass

@dataclass
class Card:
    name: str
    number: str
    exp_code: str
    rarity: str
    quantity: int = 0
    card_id:int|None = None

    @classmethod
    def from_db_str(cls, db_str: str):
        if db_str == 'None':
            return None
        card_stats = []
        for x in [item.strip() for item in db_str.split(',')]:
            for ch in ['\\','`','*','_','{','}','[',']','(',')','>','#','+','-','.','!','$','\'']:
                if ch in x:
                    x = x.replace(ch,"")
                    card_stats.append(x)
        card_id, name, number, exp_code, rarity, quantity = card_stats
        return cls(name, number, exp_code, rarity, quantity, card_id)
