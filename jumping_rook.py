#!/usr/local/bin/python3

import numpy as np
import matplotlib.pyplot as plt

class vec:
    '''2D X-Y location.'''
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return '{}, {}'.format(self.x, self.y)

    def __hash__(self):
        return hash((self.x, self.y))
    
    def __eq__(self, obj):
        return self.x == obj.x and self.y == obj.y

    def __add__(self, new):
        return (vec(self.x + new.x, self.y + new.y))

    def __getitem__(self, key):
        # For conversion to numpy array
        if key == 0:
            return self.x
        if key == 1:
            return self.y
        if key > 1:
            raise IndexError

    def __len__(self):
        # For conversion to numpy array
        return 2

    @property
    def max(self):
        return max([abs(self.x), abs(self.y)])


class Ulam:
    '''Ulam spiral.'''

    directions = [vec(0, 1),
                  vec(-1, 0),
                  vec(0, -1),
                  vec(1, 0)]

    def __init__(self, start=1):
        self.spiral = {vec(0, 0): start}
        self.max = start
        self.size = 1

    def __repr__(self):
        return 'Ulam spiral: size {}, max {}'.format(self.size, self.max)

    def __str__(self):
        coords = range(-self.size + 1, self.size)
        format = '{{:{}}}'.format(len(str(self.max)) + 1)
        return '\n'.join([
            (format * (self.size * 2 - 1)).format(
                *[self.spiral[vec(x, -y)] for x in coords]
            ) for y in coords
        ])

    def __call__(self, target: vec):
        if target.max >= self.size:
            self._add_loop()
            self.__call__(target)
        return self.spiral[target]

    def _add_loop(self):
        self.size += 1
        pos = vec(self.size - 1, 1 - self.size)
        for dpos in self.directions:
            for _ in range(2 * (self.size - 1)):
                self.max += 1
                pos += dpos
                self.spiral[pos] = self.max


class Rook:
    # The rook is jumping on an Ulam spiral board
    board = Ulam()

    # It starts in the center
    locations = [vec(0, 0)]

    # Legal rook moves
    legal_moves = (vec(2, 1),
                   vec(1, 2),
                   vec(-1, 2),
                   vec(-2, 1),
                   vec(-2, -1),
                   vec(-1, -2),
                   vec(1, -2),
                   vec(2, -1))

    def jump(self):
        destination = False
        value = float('inf')
        for move in self.legal_moves:
            target = self.locations[-1] + move
            if not target in self.locations:
                if self.board(target) < value:
                    value = self.board(target)
                    destination = target
        if not destination:
            return False
        self.locations.append(destination)
        return True

    def print(self):
        print(self.locations[-1])

    def print_final(self):
        print('Final location {} after {} jumps with value {}'.format(
            self.locations[-1], len(self.locations), self.board(self.locations[-1])
        ))

    def plot(self):
        locations = np.array(self.locations)
        plt.plot(locations[:,0], locations[:,1], '0.45', linewidth=0.8)
        plt.axis('equal')
        plt.axis('off')
        plt.tight_layout()
        plt.show()


if __name__ == '__main__':
    rook = Rook()
    while rook.jump():
        pass
    rook.print_final()
    rook.plot()
