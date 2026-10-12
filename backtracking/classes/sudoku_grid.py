import numpy as np


class Sudoku_grid:
    def __init__(self, id: int, puzzle: str, solution: str, difficulty: float):
        self.id = id
        self.difficulty = difficulty
        self.puzzle = self.puzzle_to_array(puzzle)
        self.solution = self.solution_to_array(solution)
        self.path_taken = []

    def puzzle_to_array(self, puzzle: str) -> np.ndarray:
        puzzle_array = np.ones(shape=(9, 9, 9), dtype=bool)
        for index in range(81):
            element = puzzle[index]
            if element != ".":
                puzzle_array[index // 9, index % 9, : int(element) - 1] = False
                puzzle_array[index // 9, index % 9, int(element) :] = False

        return puzzle_array

    def solution_to_array(self, puzzle: str) -> np.ndarray:
        puzzle_array = np.zeros(shape=(9, 9), dtype=int)
        for index in range(81):
            element = puzzle[index]
            puzzle_array[index // 9, index % 9] = int(element)
        return puzzle_array

    def select_case(
        self, coordinates: tuple[int, int], number: int, back_off: bool
    ) -> None:
        x, y = coordinates
        self.puzzle[x, :, number - 1] = back_off
        self.puzzle[:, y, number - 1] = back_off
        self.puzzle[x // 3 : x // 3 + 2, y // 3 : y // 3 + 2, number - 1] = back_off
        self.puzzle[x, y, number - 1] = not back_off
        self.path_taken.append((coordinates, number))

    def backward(self) -> None:
        coordinates, number = self.path_taken.pop()
        self.select_case(coordinates, number, True)
