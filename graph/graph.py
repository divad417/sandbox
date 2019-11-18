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

    def connect(self, edges: List[Node]):
        for edge in edges:
            self._check_node(edge)
            if edge in self.edges:
                continue
            self.edges.append(edge)

    def set_parent(self, node: Node):
        self._check_node(node)
        if self not in node.edges:
            raise ValueError('Parent not connected')
        self.parent = node

    def _check_node(self, node: Node):
        if not node.id < self.max_id:
            raise ValueError('Invalid node')


class Graph:

    def __init__(self):
        self.nodes = []

    def from_array(self, array):
        pixel = np.nditer(array, flags=['multi_index'])
        while not pixel.finished:
            if pixel[0] == Image.BLOCKED:
                pixel.iternext()
                continue
            node = Node()
            node.row, node.col = pixel.multi_index

            # Find edges above
            if node.row > 0:
                pass
            # Find edges below
            if node.row < array.shape[0]:
                pass
            # Find edges left
            if node.col > 0:
                pass
            # Find edges right
            if node.col < array.shape[1]:
                pass

            self.nodes.append(node)
            pixel.iternext()

        
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
        self.grid = array_like

    @property
    def graph(self):
        self._graph = Graph()
        self._graph.from_array(self.grid)
        return self._graph

    def show(self):
        colors = {self.FREE : (255, 255, 255),
                  self.BLOCKED : (0, 0, 0),
                  self.PATH : (255, 0, 0)}

        # Create an image by replacing scalar values with RGB values.
        image_flat = [colors[pixel] for pixel in self.grid.flat]
        image = np.reshape(image_flat, self.grid.shape + (3,))

        # Display the image.
        fig, ax = plt.subplots()
        fig.set_facecolor('gray')
        ax.imshow(image)
        ax.set_axis_off()
        plt.show()


if __name__ == '__main__':
    a = Image(np.identity(5))
    a.grid[0, 0] = Image.PATH
    a.graph
    a.show()



# Create an image
# Create a graph from the image
# Find a way through that graph

# G - cost of path to start
# H - cost of path to goal
# F - sum of cost