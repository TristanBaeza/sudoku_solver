import numpy as np


class Sudoku_grid:
    def __init__(self, id: int, puzzle: str, solution: str, difficulty: float):
        self.id = id
        self.difficulty = difficulty
        self.puzzle = self.puzzle_to_array(puzzle)
        self.solution = self.puzzle_to_array(solution)

    def puzzle_to_array(self, puzzle: str) -> np.ndarray:
        puzzle_array = np.zeros(shape=(9, 9), dtype=int)
        for index in range(81):
            element = puzzle[index]
            if element == ".":
                puzzle_array[index // 9, index % 9] = 0
            else:
                puzzle_array[index // 9, index % 9] = int(element)
        return puzzle_array
