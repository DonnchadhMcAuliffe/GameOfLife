# Python Standard
from typing import List, Optional

# Third-party
import numpy


class GameOfLife:
    def __init__(self, lenth_of_square: int):
        """Create a square grid of zeros. """
        self.lenth_of_square = lenth_of_square
        self.grid = numpy.zeros((self.lenth_of_square, self.lenth_of_square), dtype=int)
        self.grid_shape = self.grid.shape

    def copy_grid(self):
        return self.grid.copy()

    def set_initial_state(self, positions: List[list]):
        """For every position given set its co-ordinate on the grid to 1. """
        for pos in positions:
            self.grid[pos[0]][pos[1]] = 1

    def dead_becomes_alive(self, pos: List) -> bool:
        """Evaluate whether a 'dead' cell (value 0) becomes 'alive'."""
        return self.get_total_number_of_neighbours(pos) == 3

    def alive_remains_alive(self, pos: List) -> bool:
        """Evaluate whether a 'alive' cell (value 1) remains 'alive'."""
        return 2 <= self.get_total_number_of_neighbours(pos) <= 3

    def compute_new_grid(self):
        """Evaluate the game of life and as a result update 'self.grid'"""
        # make a copy of the grid
        new_grid = self.copy_grid()

        # evaluate each cell in the grid
        for row_num in range(0, self.grid_shape[0]):
            for col_num in range(0, self.grid_shape[1]):
                if self.grid[row_num, col_num]:
                    if not self.alive_remains_alive([row_num, col_num]):
                        new_grid[row_num, col_num] = 0
                else:
                    if self.dead_becomes_alive([row_num, col_num]):
                        new_grid[row_num, col_num] = 1
        self.grid = new_grid

    def get_total_number_of_neighbours(self, pos: List) -> int:
        """Return the total number of 'alive' cells around a given cell in the grid."""
        neighbours = 0
        if self.get_top_left(pos):
            neighbours += 1
        if self.get_top_center(pos):
            neighbours += 1
        if self.get_top_right(pos):
            neighbours += 1
        if self.get_center_left(pos):
            neighbours += 1
        if self.get_center_right(pos):
            neighbours += 1
        if self.get_bottom_left(pos):
            neighbours += 1
        if self.get_bottom_center(pos):
            neighbours += 1
        if self.get_bottom_right(pos):
            neighbours += 1
        return neighbours

    def get_top_left(self, pos: List) -> Optional[int]:
        top_left = [pos[0] - 1, pos[1] - 1]
        if all(i >= 0 for i in top_left):
            return self.grid[top_left[0], top_left[1]]

    def get_top_center(self, pos: List) -> Optional[int]:
        top_middle = [pos[0] - 1, pos[1]]
        if all(i >= 0 for i in top_middle):
            return self.grid[top_middle[0], top_middle[1]]

    def get_top_right(self, pos: List) -> Optional[int]:
        top_right = [pos[0] - 1, pos[1] + 1]
        if top_right[0] >= 0 and top_right[1] < self.grid_shape[1]:
            return self.grid[top_right[0], top_right[1]]

    def get_center_left(self, pos: List) -> Optional[int]:
        center_left = [pos[0], pos[1] - 1]
        if all(i >= 0 for i in center_left):
            return self.grid[center_left[0], center_left[1]]

    def get_center_right(self, pos: List) -> Optional[int]:
        center_right = [pos[0], pos[1] + 1]
        if center_right[1] < self.grid_shape[1]:
            return self.grid[center_right[0], center_right[1]]

    def get_bottom_left(self, pos: List) -> Optional[int]:
        bottom_left = [pos[0] + 1, pos[1] - 1]
        if bottom_left[0] < self.grid_shape[0] and bottom_left[1] >= 0:
            return self.grid[bottom_left[0], bottom_left[1]]

    def get_bottom_center(self, pos: List) -> Optional[int]:
        bottom_center = [pos[0] + 1, pos[1]]
        if bottom_center[0] < self.grid_shape[0]:
            return self.grid[bottom_center[0], bottom_center[1]]

    def get_bottom_right(self, pos: List) -> Optional[int]:
        bottom_right = [pos[0] + 1, pos[1] + 1]
        if bottom_right[0] < self.grid_shape[0] and bottom_right[1] < self.grid_shape[1]:
            return self.grid[bottom_right[0], bottom_right[1]]
