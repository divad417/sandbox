#!/usr/local/bin/python3

from typing import List

import numpy as np
import matplotlib.pyplot as plt


class Node():
    max_id = 0

    def __init__(self):
        self.id = self.max_id
        self.max_id +=1
        self.edges = []
        self.parent = None

    def _check_node(self, node: 'Node'):
        if not node.id < self.max_id:
            raise ValueError('Invalid node')

    def connect(self, edge: 'Node'):
        self._check_node(edge)
        if edge in self.edges:
            continue
        self.edges.append(edge)

    def set_parent(self, node: 'Node'):
        self._check_node(node)
        if self not in node.edges:
            raise ValueError('Parent not connected')
        self.parent = node

    def set_position(self, index):
        self.row = index[0]
        self.col = index[1]

class Graph:

    def __init__(self):
        self.nodes = []

    def from_image(self, array):
        # Create nodes
        iterator = np.nditer(array, flags=['multi_index'])
        while not iterator.finished:
            if iterator.value == Image.BLOCKED:
                iterator.iternext()
                continue
            self.nodes.append(Node())
            self.nodes[-1].set_position(iterator.multi_index)
            iterator.iternext()

        connections = ([1, 0],
                       [0, 1],
                       [-1, 0],
                       [0, -1])

        def _get_id_by_location(row, col):
            return id

        def _connect_if_valid(node, row, col):
            if not (0 <= row < array.shape[0] and
                    0 <= col < array.shape[1]):
                return
            if array(row, col) == Image.BLOCKED:
                return
            node.connect(self._get_id_by_location(row, col))

        # Connect nodes
        for node in self.nodes():
            for drow, dcol in connections:
                self._connect_if_valid(node, node.row + drow, node.col + dcol)
            


        
        # Go through each pixel
            # Create a node if it's not filled
            # Conenct the node to nearby elements
    
    def reduce(self):
        pass
        # Remove unnessary nodes

class Image:
    FREE = 0
    BLOCKED = 1
    PATH = 2

    def __init__(self, array_like):
        # Check that all pixels are valid
        self.map = array_like

    @property
    def make_graph(self):
        self._graph = Graph()
        self._graph.from_image(self.map)
        self._graph.reduce()

    def show(self):
        colors = {self.FREE : (255, 255, 255),
                  self.BLOCKED : (0, 0, 0),
                  self.PATH : (255, 0, 0)}

        # Create an image by replacing scalar values with RGB values.
        image_flat = [colors[pixel] for pixel in self.map.flat]
        image = np.reshape(image_flat, self.map.shape + (3,))

        # Display the image.
        fig, ax = plt.subplots()
        fig.set_facecolor('gray')
        ax.imshow(image)
        ax.set_axis_off()
        plt.show()


if __name__ == '__main__':
    a = Image(np.identity(6) * Image.BLOCKED)
    a.map[0, 0] = Image.PATH
    a.make_graph
    a.show()



# Create an image
# Create a graph from the image
# Find a way through that graph

# G - cost of path to start
# H - cost of path to goal
# F - sum of cost