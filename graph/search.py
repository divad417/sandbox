import graph

class Dykstra(graph.SearchAlgorithm):
    def solve(self, graph: graph.Graph):
        pass

class AStar(graph.SearchAlgorithm):
    def __init__(self, heuristic):
        self._h = heuristic

    def solve(self, graph: graph.Graph):
        if not graph.start or not graph.goal:
            raise RuntimeError('Start and/or Goal not defined')

        graph.start.g = 0
        open = [graph.start]
        closed = []

        while open:
            for node in open:
                node.f = self._f(node)
            node_current = min(open, key=lambda node: node.f)
            if node_current == graph.goal:
                break

            open.remove(node_current)
            for node_successor in node_current.edges:
                successor_current_cost = node_current.g + node_current.cost(node_successor)
                if node_successor in open:
                    if node_successor.g <= successor_current_cost:
                        continue
                elif node_successor in closed:
                    if node_successor.g <= successor_current_cost:
                        continue
                    closed.remove(node_successor)
                else:
                    node_successor.h = self._h(node_successor)
                open.append(node_successor)
                node_successor.g = successor_current_cost
                node_successor.set_parent(node_current)
            closed.append(node_current)

        if node_current != graph.goal:
            raise RuntimeError('Unable to find path')

    def _f(self, node: graph.Node) -> int:
        return node.g + self._h(node)
