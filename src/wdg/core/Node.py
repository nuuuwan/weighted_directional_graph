from dataclasses import dataclass


@dataclass
class Node:
    id: str
    label: str
    xy: list[float]
