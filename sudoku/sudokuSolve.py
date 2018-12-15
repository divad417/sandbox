import numpy as np
import sudokuInput
import sudoku


input = sudokuInput.generate('Medium')
puzzle = np.copy(input)
solved = 0

# Try solving each method in turn, note sucesses
while solved == 0:
    change = 0

    # Basic counting rules algorithm (elimination)
    puzzle, tmpchg = sudoku.basicRules(puzzle)
    change += tmpchg

    # Placing values in cells algorithm
    puzzle, tmpchg = sudoku.placeValues(puzzle)
    change += tmpchg

    if change == 0:
        break
    if np.all(puzzle !=0):
        solved = 1

sudoku.printSudoku(input, puzzle)
print sudoku.message(solved)
