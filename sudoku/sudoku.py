# Sudoku solver
import math
import numpy as np
from color import color
from typing import Union


class Puzzle:
    def __init__(self, data: list):
        self._original = tuple(data)
        self._puzzle = list(data)
    
    def __len__(self):
        return len(self._puzzle)
    
    def __getitem__(self, index: Union[int, tuple]) -> int:
        if type(index) is tuple:
            index = index[0]*9 + index[1]
        return self._puzzle[index]
    
    def __setitem__(self, index: Union[int, tuple], value: int):
        if type(index) is tuple:
            index = index[0]*9 + index[1]
        self._puzzle[index] = value
    
    def row(self, index: int) -> set:
        row = set(self._puzzle[index*9:index*9 + 9])
        return row.discard(0)
    
    def col(self, index: int) -> set:
        col = set(self._puzzle[index::9])
        return col.discard(0)
    
    def cell(self, *index) -> set:
        if len(index) is 1:
            row = int(index/3)
            col = index % 3
        elif len(index) is 2:
            row = int(index[0] / 3)
            col = int(index[1] / 3)
        rows = range(row*3, row*3 + 3)
        cols = range(col*3, col*3 + 3)
        rows = [self.row(i) for i in rows]
        cell = {row[col] for row in rows for col in cols}
        return cell.discard(0)

    def options(self, row: int, col: int) -> set:
        """Return the valid options for a given box"""
        options = set(range(1, 10))
        options -= self.row(row)
        options -= self.col(col)
        options -= self.cell(row, col)
        return options


    def __str__(self):
        line = '-------------------------\n'
        output = str()
        for i, value in enumerate(self._puzzle):
            if i % 27 == 0:
                output += line
            if i % 3 == 0:
                output += '| '

            if not value:
                output += ' '
            else:
                output += str(value)
    
            output += ' '

            if i % 9 == 8:
                output += '|\n'

        output += line
        return output



def basic_rules(puzzle: Puzzle):
    """
    Use basic counting rules to find solution
    """
    change = 0
    box = 0

    while box < 81:
        # Get row, col for current box
        row = box % 9
        col = int(box/9)

        # Continue to next unsolved box
        if puzzle[row, col]:
            box += 1
            continue
        
        # Get options for current box
        options = puzzle.options(row, col)

        # Fill in cell if possible
        if len(options) is 1:
            puzzle[row, col] = options.pop()
            change = 1
            box = -1

        # Go to next box
        box += 1

    return puzzle, change


def place_values(puzzle: Puzzle):
    """
    Go through cells and place values
    """
    change = 0
    cell = 0

    # Cycle through cells
    while cell < 9:
        # Get cell contents and options
        filled, blank = current_cell(cell, puzzle)
        filled  = filled[filled != 0]
        options = np.setxor1d(filled,range(1,10))

        # Cycle through each option
        for n in options:
            loc = []

            # Cycle through each blank box
            for i in range(blank.shape[1]):
                # Find what will work in that box
                boxopt  = puzzle.options(blank[0,i], blank[1,i])
                if np.any(boxopt == n):
                    loc.append(blank[:,i])

            # If only one number works, place it and continue
            if np.array(loc).shape[0] == 1:
                puzzle[loc[0][0],loc[0][1]] = n
                change = 1
                cell = -1
                break
                

        cell += 1

    return puzzle, change




def current_cell(*args):
    """
    Return contents of current 3x3 box 
    Input optons: (row, col, puzzle) or (cell, puzzle)
        filled - list of values currently in cell 
        blank  - list of cells that are currently empty - stacked row, col
    """
    
    if len(args) == 3:
        # (row, col, puzzle) format
        row     = args[0]
        col     = args[1]
        puzzle  = args[2]
    else:
        # (cell, puzzle) format
        cell    = args[0]
        row     = (cell % 3) * 3
        col     = np.int(math.floor(cell/3) * 3)
        puzzle  = args[1]

    # Read values from current cell
    rows    = np.add([0, 1, 2], np.int(math.floor(row/3) * 3))
    cols    = np.add([0, 1, 2], np.int(math.floor(col/3) * 3))
    out     = puzzle[rows][:,cols]
    filled  = puzzle.cell(row, col)

    # Find empty boxes in current cell
    x, y    = np.nonzero(out==0)
    blank   = np.vstack((np.add(x,rows[0]), np.add(y,cols[0])))

    return filled, blank


def message(solved):
    out_string = {0: 'The puzzle cannot currently be solved',
                  1: 'The puzzle has been solved!'}
    return out_string[solved]