from dataclasses import dataclass


@dataclass
class Option:
    variable: bool
    name: str
    description: str
    rate: float
    payment: float
    income_fraction: float
