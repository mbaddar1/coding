"""
https://leetcode.com/explore/interview/card/facebook/52/trees-and-graphs/274/
"""
import numpy as np


class Solution(object):
    def numIslands(self, grid):
        if grid is None is grid is not isinstance(list):
            return 0
        m = len(grid)
        n = 0 if m == 0 else len(grid[0])
        # 0 : not visited or added 1 : visited
        status = np.full(shape=(m, n), fill_value=0, dtype=int)
        queue_ = []
        island_counter = 0
        for i in range(m):
            for j in range(n):
                dummy1 = grid[i][j]
                dummy2 = status[i][j]
                if grid[i][j] == '1' and status[i][j] == 0:  # seed point for an island
                    island_counter += 1
                    queue_.append((i, j))
                    status[i][j] = 1
                    while len(queue_) > 0:
                        # print(f'queue = {queue_}')
                        i_, j_ = queue_.pop(0)
                        status[i_, j_] = 1
                        adjacents = Solution.get_unvisited_land_adjacents(grid, status, i_, j_, m, n)
                        for adj_i, adj_j in adjacents:
                            queue_.append((adj_i, adj_j))
                            status[adj_i][adj_j] = 1
        # print(status)
        return island_counter

    @staticmethod
    def get_unvisited_land_adjacents(grid, status, i, j, m, n):
        adjacents = []
        # upper
        if i - 1 >= 0 and grid[i - 1][j] == '1' and status[i - 1][j] == 0:
            adjacents.append((i - 1, j))
        # lower
        if i + 1 < m and grid[i + 1][j] == '1' and status[i + 1][j] == 0:
            adjacents.append((i + 1, j))
        # right
        if j + 1 < n and grid[i][j + 1] == '1' and status[i][j + 1] == 0:
            adjacents.append((i, j + 1))
        # left
        if j - 1 >= 0 and grid[i][j - 1] == '1' and status[i][j - 1] == 0:
            adjacents.append((i, j - 1))
        return adjacents


if __name__ == '__main__':
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    s = Solution()
    r = s.numIslands(grid)
    assert r == 1

    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    s = Solution()
    r = s.numIslands(grid)
    assert r == 3

    grid = [
        ["1", "0", "0", "0", "0"],
        ["0", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "0"]
    ]
    s = Solution()
    r = s.numIslands(grid)
    assert r == 4, f"r={r}"

    grid = [
        ["0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    s = Solution()
    r = s.numIslands(grid)
    assert r == 0, f"r={r}"
