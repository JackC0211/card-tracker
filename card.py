from dataclasses import dataclass

@dataclass
class Card:
    _name: str
    _number: str
    _exp_code: str
    _rarity: str
    _quantity: int = 0
    _card_id:int|None = None

    @property
    def name(self):
        return self._name
    @property
    def number(self):
        return self._number
    @property
    def exp_code(self):
        return self._exp_code
    @property
    def rarity(self):
        return self._rarity
    @property
    def quantity(self):
        return self._quantity
    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise ValueError("Quantity has to be positive")
        self._quantity = value

    @property
    def card_id(self):
        return self._card_id

    @property
    def label(self) -> str:
        return f"({self.exp_code}) - {self.name} [{self.number}] ({self.rarity})"

    @classmethod
    def from_row(cls, row: tuple):
        if row is None:
            return None

        card_id, name, number, exp_code, rarity, quantity = row

        return cls(
            _name=name,
            _number=number,
            _exp_code=exp_code,
            _rarity=rarity,
            _quantity=quantity,
            _card_id=card_id
    )

    def to_dict(self):
        return {"name": self._name,
                "number": self._number,
                "exp_code": self._exp_code,
                "rarity": self._rarity,
                "quantity": self._quantity,
                "label": self.label
                }
