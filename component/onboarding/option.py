from dataclasses import dataclass


@dataclass
class Option:
    name: str
    description: str
    rate: float
    payment: float
