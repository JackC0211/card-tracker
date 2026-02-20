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
    def from_row(cls, row: tuple):
        if row is None:
            return None

        card_id, name, number, exp_code, rarity, quantity = row

        return cls(
            name=name,
            number=number,
            exp_code=exp_code,
            rarity=rarity,
            quantity=quantity,
            card_id=card_id
    )