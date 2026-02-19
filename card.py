from dataclasses import dataclass

class Card:
    name: str
    number: str
    set_code: str
    rarity: str
    quantity: int = 0

