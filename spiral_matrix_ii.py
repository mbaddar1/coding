# https://leetcode.com/problems/spiral-matrix-ii/
from typing import List

import numpy as np


class Solution:
    @staticmethod
    def increment_index(i, j, direction):
        if direction == 'right':
            return i, j + 1
        if direction == 'down':
            return i + 1, j
        if direction == 'left':
            return i, j - 1
        if direction == 'up':
            return i - 1, j

    @staticmethod
    def will_hit_a_wall(i, j, n, grid, direction):
        if direction == 'right':
            if j + 1 > n - 1 or grid[i][j + 1] != -1:
                return True
        elif direction == 'down':
            if i + 1 > n - 1 or grid[i + 1][j] != -1:
                return True
        elif direction == 'left':
            if j - 1 < 0 or grid[i][j - 1] != -1:
                return True
        elif direction == 'up':
            if i - 1 < 0 or grid[i - 1][j] != -1:
                return True
        return False

    @staticmethod
    def change_direction(direction):
        if direction == 'right':
            new_direction = 'down'
        elif direction == 'down':
            new_direction = 'left'
        elif direction == 'left':
            new_direction = 'up'
        elif direction == 'up':
            new_direction = 'right'
        else:
            raise ValueError(f'Invalid direction {direction}')
        return new_direction

    def generateMatrix(self, n: int) -> List[List[int]]:
        u = 1
        grid = [[-1 for j in range(n)] for i in range(n)]
        i = 0
        j = 0
        direction = "right"
        while u <= (n * n):
            grid[i][j] = u
            u = u + 1
            if Solution.will_hit_a_wall(i, j, n, grid,direction):
                direction = Solution.change_direction(direction)
            i, j = Solution.increment_index(i, j, direction)

        return grid


if __name__ == '__main__':
    s = Solution()
    r = s.generateMatrix(4)
    print(r)
