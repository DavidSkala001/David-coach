from dataclasses import dataclass


@dataclass
class Athlete:

    ftp: int = 250

    weight: float = 72.0

    name: str = "David"
