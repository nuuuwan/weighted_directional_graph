from dataclasses import dataclass


@dataclass
class Edge:
    id: str
    source: str
    target: str
    weight: float
