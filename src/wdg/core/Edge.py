from dataclasses import dataclass


@dataclass
class Edge:
    id: str
    label: str
    source: str
    target: str
    weight: float
