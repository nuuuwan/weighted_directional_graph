from dataclasses import dataclass

from utils import JSONFile

from wdg.core.Edge import Edge
from wdg.core.Node import Node


@dataclass
class WDGraph:
    nodes: list[Node]
    edges: list[Edge]

    @staticmethod
    def load_from_file(path: str):
        data = JSONFile(path).read()
        nodes = [Node(**node) for node in data['nodes']]
        edges = [Edge(**edge) for edge in data['edges']]
        return WDGraph(nodes, edges)
