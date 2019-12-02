#!/usr/bin/env python3

class Test:
    def __init__(self):
        self._data = [[1, 2], [3, 4]]

    def __getitem__(self, index):
        print('Index is {}'.format(index))
        print('Index type is {}'.format(type(index)))