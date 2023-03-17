from dataclasses import dataclass
from wdg.core.Node import Node
from wdg.core.Edge import Edge
from utils import JSONFile
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
