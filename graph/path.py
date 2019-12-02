#!/usr/local/bin/python3

import numpy as np
import matplotlib.pyplot as plt

import search
import graph
from vectors import vec

class Node2D(graph.Node):
    def __init__(self):
        super().__init__()
        self.position = None

    def cost(self, edge) -> float:
        super().cost(edge)
        return abs(self.position - edge.position)


class Graph2D(graph.Graph):
    def distance(self, node) -> float:
        return abs(node.position - self.goal.position)

    def from_array(self, array):
        # Create nodes
        iterator = np.nditer(array._data, flags=['multi_index'])
        while not iterator.finished:
            if not iterator.value:
                iterator.iternext()
                continue
            new_node = Node2D()
            new_node.position = vec(iterator.multi_index)
            self.nodes.add(new_node)
            iterator.iternext()
        self._node_map = {node.position : node for node in self.nodes}

        # Connect nodes
        connections = (vec(1, 0),
                       vec(1, 1),
                       vec(0, 1),
                       vec(-1, 1),
                       vec(-1, 0),
                       vec(-1, -1),
                       vec(0, -1),
                       vec(1, -1))

        for node in self.nodes:
            for connection in connections:
                edge_position = node.position + connection
                if edge_position in self._node_map:
                    node.connect(self._node_map[edge_position])

    def set_bounds(self, start: vec, goal: vec):
        self.start = self._node_map[start]
        self.goal = self._node_map[goal]

    def solve(self, search_algorithm: graph.SearchAlgorithm):
        super().solve(search_algorithm)
        solver = search_algorithm(self.distance)
        solver.solve(self)

    def to_array(self):
        pass


class Image:
    BLOCKED = 0
    FREE = 1
    START = 2
    GOAL = 3
    PATH = 4

    def __init__(self, array_like):
        # TODO check that array_like is actually array like
        # TODO check that all pixels are valid
        self._data = array_like

    def __getitem__(self, index):
        if type(index) not in {'int', 'tuple'}:
            raise IndexError
        return self._data[index]

    def __setitem__(self, index, value):
        if not isinstance(index, (int, tuple)):
            raise IndexError
        # TODO check that shape of value is same as shape described by index
        self._data[index] = value

    def show(self):
        colors = {self.FREE : (255, 255, 255),
                  self.BLOCKED : (0, 0, 0),
                  self.START : (0, 255, 0),
                  self.GOAL : (255, 0, 0),
                  self.PATH : (0, 63, 255)}

        # Create an image by replacing scalar values with RGB values.
        image_flat = [colors[pixel] for pixel in self._data.flat]
        image = np.reshape(image_flat, self._data.shape + (3,))

        # Display the image.
        fig, ax = plt.subplots()
        fig.set_facecolor('gray')
        ax.imshow(image)
        ax.set_axis_off()
        plt.show()


if __name__ == '__main__':
    # Create a map
    image = Image(np.ones((6, 6)) * Image.FREE)
    image[1, 1] = Image.BLOCKED
    image[1, 2] = Image.BLOCKED

    # Convert to a graph
    graph = Graph2D()
    graph.from_array(image)
    graph.set_bounds(start=vec(0, 0), goal=vec(4, 5))
    graph.solve(search_algorithm=search.AStar)
    
    path = graph.goal.generate_path()
    path = [node.position for node in path]

    for point in path:
        image[point.x, point.y] = Image.PATH
    image[graph.start.position.x, graph.start.position.y] = Image.START
    image[graph.goal.position.x, graph.goal.position.y] = Image.GOAL

    image.show()
