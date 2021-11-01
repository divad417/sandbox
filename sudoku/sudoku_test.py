import unittest
import sudoku

class SudokuTest(unittest.TestCase):
    def test_iterator(self):
        puzzle = sudoku.Puzzle([1]*81)
        self.assertEqual(
            [i for i in puzzle],
            [1]*81
        )
    
    def test_index_by_scalar(self):
        puzzle = sudoku.Puzzle([1, 2, 3, 4, 0, 6, 7, 8, 9]*9)
        self.assertEqual(
            puzzle[4],
            0
        )
        puzzle[4] = 5
        self.assertEqual(
            puzzle[4],
            5
        )
    
    def test_index_by_tuple(self):
        puzzle = sudoku.Puzzle([1, 0, 3, 4, 5, 6, 7, 8, 9]*9)
        self.assertEqual(
            puzzle[1, 1],
            0
        )
        puzzle[1, 1] = 2
        self.assertEqual(
            puzzle[1, 1],
            2
        )


    def test_row(self):
        puzzle = sudoku.Puzzle([1, 2, 3]*27)
        self.assertEqual(
            puzzle.row(0),
            set(1, 2, 3)
        )
    
    def test_col(self):
        puzzle = sudoku.Puzzle([1, 2, 3]*27)
        self.assertEqual(
            puzzle.col(0),
            set(1)
        )
    
    def test_cell(self):
        puzzle = sudoku.Puzzle([1, 2, 3, 4, 5, 6, 7, 8, 9]*9)
        self.assertEqual(
            puzzle.cell(4, 4),
            set(4, 5, 6)
        )
    
    def test_options(self):
        puzzle = sudoku.Puzzle([0]*81)
        puzzle[0, 3] = 1
        puzzle[3, 0] = 2
        puzzle[2, 2] = 3
        self.assertEqual(
            puzzle.options(0, 0),
            {4, 5, 6, 7, 8, 9}
        )

    def test_print(self):
        puzzle = sudoku.Puzzle([1, 0, 2]*27)
        correct_output = '''-------------------------
| 1   2 | 1   2 | 1   2 |
| 1   2 | 1   2 | 1   2 |
| 1   2 | 1   2 | 1   2 |
-------------------------
| 1   2 | 1   2 | 1   2 |
| 1   2 | 1   2 | 1   2 |
| 1   2 | 1   2 | 1   2 |
-------------------------
| 1   2 | 1   2 | 1   2 |
| 1   2 | 1   2 | 1   2 |
| 1   2 | 1   2 | 1   2 |
-------------------------
'''
        self.assertEqual(
            str(puzzle), correct_output
        )
    
if __name__ == '__main__':
    unittest.main()
