#!/usr/local/bin/python3

import numpy as np
import matplotlib.pyplot as plt

from graph.vectors import vec

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

    def __str__(self) -> str:
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

    def jump(self) -> bool:
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

        plt.figure()
        plt.plot(locations[:,0], locations[:,1], '0.45', linewidth=0.8)
        plt.axis('equal')
        plt.axis('off')
        plt.tight_layout()
        plt.savefig('jumping_rook.png', dpi=300, transparent=True)


if __name__ == '__main__':
    rook = Rook()
    while rook.jump():
        pass
    rook.print_final()
    rook.plot()
