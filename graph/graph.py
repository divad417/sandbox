import abc
from typing import Type, List, TypeVar


class Node(abc.ABC):
    max_id = 0

    def __init__(self):
        self.id = self.max_id
        Node.max_id += 1
        self.edges = []
        self.parent = None

    def __repr__(self) -> str:
        return f'Node {self.id}'

    def _check_node(self, node: 'Node'):
        if not node.id < Node.max_id:
            raise ValueError('Invalid node')

    def connect(self, edge: 'Node'):
        self._check_node(edge)
        if edge not in self.edges:
            self.edges.append(edge)

    def set_parent(self, node: 'Node'):
        self._check_node(node)
        if self not in node.edges:
            raise ValueError('Current node not an edge of requested parent')
        self.parent = node

    def generate_path(self, path=[]) -> List['Node']:
        path.append(self)
        if self.parent:
            self.parent.generate_path(path)
        path.reverse()
        return path

    @abc.abstractmethod
    def cost(self, node: Type('Node')) -> int:
        if node not in self.edges:
            return None


class SearchAlgorithm(abc.ABC):
    @abc.abstractmethod
    def solve(self):
        pass


class Graph(abc.ABC):
    def __init__(self):
        self.nodes = set()
        self.start = None
        self.goal = None
            
    def simplify(self):
        for node in self.nodes:
            if node in (self.start, self.goal):
                continue
            if len(node.edges) < 3:
                pass

    @abc.abstractmethod
    def solve(self, search_algorithm: SearchAlgorithm):
        # Solve in place by determining each parent
        pass