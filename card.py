from dataclasses import dataclass

@dataclass
class Card:
    name: str
    number: str
    exp_code: str
    rarity: str
    quantity: int = 0

