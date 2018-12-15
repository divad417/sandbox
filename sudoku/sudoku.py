# Sudoku solver
import numpy as np
import math
from color import color

def basicRules(puzzle):
    """
    Use basic counting rules to find solution
    """
    change  = 0
    box     = 0

    while box < 81:
        # Get row, col for current box
        row = box % 9
        col = np.int(np.floor(box/9))

        # Continue to next unsolved box
        if puzzle[row,col] != 0:
            box += 1
            continue
        
        # Get options for current box
        options     = boxOptions(row, col, puzzle)

        # Fill in cell if possible
        if options.size == 1:
            puzzle[row, col] = options
            change  = 1
            box     = -1

        # Go to next box
        box += 1

    return puzzle, change

def placeValues(puzzle):
    """
    Go through cells and place values
    """
    change  = 0
    cell    = 0

    # Cycle through cells
    while cell < 9:
        # Get cell contents and options
        filled, blank = currentCell(cell, puzzle)
        filled  = filled[filled != 0]
        options = np.setxor1d(filled,range(1,10))

        # Cycle through each option
        for n in options:
            loc = []

            # Cycle through each blank box
            for i in range(blank.shape[1]):
                # Find what will work in that box
                boxopt  = boxOptions(blank[0,i], blank[1,i], puzzle)
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

def boxOptions(row, col, puzzle):
    """
    Get contents of each row and column and cell
    """
    rowconts            = puzzle[row,:].T
    colconts            = puzzle[:,col]
    cellconts           = currentCell(row,col,puzzle)[0]
    filled              = np.unique(np.concatenate((rowconts, colconts, cellconts),0))
    filled              = filled[filled != 0]
    options             = np.setxor1d(filled,range(1,10))

    return options


def currentCell(*args):
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
    filled  = np.sort(out.flatten())

    # Find empty boxes in current cell
    x, y    = np.nonzero(out==0)
    blank   = np.vstack((np.add(x,rows[0]), np.add(y,cols[0])))

    return filled, blank


def printSudoku(original, *args):
    """
    Display a Sudoku puzzle. Original values in bold. Accepts either form:
        printSudoku(puzzle)
        printSudoku(puzzle, solution)
    """

    # If called with one input, use as puzzle and solution
    if not args:
        solution = original
    else:
        solution = args[0]

    line = '-------------------------'
    print line

    for i in range(9):
        for j in range(9):
            if j%3 == 0:
                print '|',

            if solution[i,j] == 0:
                print ' ',
            elif original[i,j] != 0:
                print solution[i,j],
            else:
                print color.CYAN + str(solution[i,j]) + color.END,

            if j%9 == 8:
                print '|'

        if i%3 == 2:
            print line

    return

def message(solved):
    outString = {0: 'The puzzle cannot currently be solved',\
                 1: 'The puzzle has been solved!'}
    return outString[solved]