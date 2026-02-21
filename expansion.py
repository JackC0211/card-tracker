from dataclasses import dataclass

@dataclass
class Expansion:
    code: str
    name: str
    
    def to_dict(self):
        return {
            "code": self.code,
            "name": self.name
        }