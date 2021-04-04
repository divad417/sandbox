import numpy as np
import sudoku


puzzles = {
    'Basic': [
        0, 2, 3, 4, 5, 6, 7, 8, 9,
        4, 5, 6, 0, 8, 9, 1, 2, 3,
        7, 8, 9, 1, 2, 3, 0, 5, 6,
        2, 0, 4, 5, 6, 7, 8, 9, 1,
        5, 6, 7, 8, 9, 0, 2, 3, 4,
        8, 9, 1, 2, 3, 4, 5, 6, 0,
        3, 0, 0, 6, 7, 8, 9, 1, 2,
        6, 7, 0, 9, 1, 0, 3, 4, 5,
        9, 1, 2, 3, 4, 5, 6, 7, 0],
    'Medium':[
        0, 0, 9, 4, 0, 1, 0, 0, 0,
        0, 0, 5, 0, 0, 0, 9, 0, 2,
        7, 0, 2, 0, 0, 6, 4, 0, 0,
        0, 2, 0, 6, 0, 8, 0, 0, 1,
        0, 3, 7, 0, 5, 9, 0, 4, 6,
        8, 0, 0, 0, 0, 4, 2, 0, 0,
        4, 6, 0, 0, 0, 0, 3, 0, 0,
        0, 0, 8, 1, 0, 0, 0, 9, 4,
        5, 9, 0, 0, 0, 0, 0, 0, 0]
    }


def main(puzzle):
    # Try solving each method in turn, note sucesses
    solved = False
    while not solved:
        change = 0

        # Basic counting rules algorithm (elimination)
        puzzle, tmpchg = sudoku.basic_rules(puzzle)
        change += tmpchg

        # Placing values in cells algorithm
        puzzle, tmpchg = sudoku.place_values(puzzle)
        change += tmpchg

        if change == 0:
            break
        if np.all(puzzle !=0):
            solved = True

    print(puzzle)
    print(sudoku.message(solved))

if __name__ == '__main__':
    puzzle = sudoku.Puzzle(puzzles['Basic'])
    main(puzzle)