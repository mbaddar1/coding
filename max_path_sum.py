# https://leetcode.com/problems/minimum-path-sum/
from typing import List


class Solution:
    def getNeighbors(self, i, j, m, n):
        neighbors = []
        # down
        if i + 1 <= m - 1:
            neighbors.append((i + 1, j))
        # right
        if j + 1<=n-1:
            neighbors.append((i, j + 1))
        return neighbors

    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        r = self.__minPathSum(0, 0, m, n, grid)
        return r

    def __minPathSum(self, i, j, m, n, grid):
        if i == m - 1 and j == n - 1:
            return grid[i][j]
        else:
            neighbors = self.getNeighbors(i, j, m, n)
            min_ = None
            for neighbor in neighbors:
                path_val = self.__minPathSum(neighbor[0], neighbor[1], m, n, grid)
                if min_ is None:
                    min_ = path_val
                else:
                    min_ = min(min_, path_val)
            val = grid[i][j] + min_
            return val


if __name__ == '__main__':
    s = Solution()
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    r = s.minPathSum(grid)
    print(r)

    grid = [[1, 2, 3], [4, 5, 6]]
    r = s.minPathSum(grid)
    print(r)

