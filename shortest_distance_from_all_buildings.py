"""
https://leetcode.com/explore/interview/card/facebook/52/trees-and-graphs/3026/
https://leetcode.com/problems/shortest-distance-from-all-buildings/solution/
"""
# TODO
"""
submitted and got time exceed error
review your solution with leetcode one esp. the last optimized one

"""
import numpy as np

MAX_ = 100000000


class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid is None:
            return -1
        if len(grid) == 0:
            return -1
        if len(grid[0]) == 0:
            return -1
        m = len(grid)
        n = len(grid[0])
        distances = np.zeros(shape=(m, n), dtype=int)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    distances_ij = self.find_distances(i, j, m, n, grid)
                    distances = distances + distances_ij
        # print(f'\n{distances}\n')
        soln_found = False
        min_ = MAX_
        for i2 in range(m):
            for j2 in range(n):
                if distances[i2][j2] < min_:
                    soln_found = True
                    min_ = distances[i2][j2]

        if soln_found:
            return min_
        else:
            return -1

    def find_distances(self, i, j, m, n, grid):
        distances_ij = np.full(shape=(m, n), fill_value=MAX_, dtype=int)
        visited = np.zeros(shape=(m, n))
        queue_ = []
        queue_.append((i, j, 0))
        while len(queue_) > 0:
            i_, j_, d_ = queue_.pop(0)
            visited[i_][j_] = 1
            neighbors = self.get_unvisited_valid_neighbors(i_, j_, m, n, visited, grid)
            for neighbor_i, neighbor_j in neighbors:
                distances_ij[neighbor_i, neighbor_j] = d_ + 1
                queue_.append((neighbor_i, neighbor_j, d_ + 1))
        return distances_ij

    def get_unvisited_valid_neighbors(self, i, j, m, n, visited, grid):
        neighbors = []
        # left
        if j - 1 >= 0 and visited[i][j - 1] == 0 and grid[i][j - 1] == 0:
            neighbors.append((i, j - 1))
        # right
        if j + 1 < n and visited[i][j + 1] == 0 and grid[i][j + 1] == 0:
            neighbors.append((i, j + 1))
        # up
        if i - 1 >= 0 and visited[i - 1][j] == 0 and grid[i - 1][j] == 0:
            neighbors.append((i - 1, j))
        # down
        if i + 1 < m and visited[i + 1][j] == 0 and grid[i + 1][j] == 0:
            neighbors.append((i + 1, j))
        return neighbors


if __name__ == '__main__':
    grid = [[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]
    s = Solution()
    r = s.shortestDistance(grid)
    assert r == 7

    grid = [[1, 0]]
    s = Solution()
    r = s.shortestDistance(grid)
    assert r == 1

    grid = [[1]]
    s = Solution()
    r = s.shortestDistance(grid)
    assert r == -1

    grid = [[1, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2]]
    s = Solution()
    r = s.shortestDistance(grid)
    assert r == -1

    grid = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
    s = Solution()
    r = s.shortestDistance(grid)
    assert r == -1

    grid = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 0]]
    s = Solution()
    r = s.shortestDistance(grid)
    assert r == -1

    grid = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
    s = Solution()
    r = s.shortestDistance(grid)
    assert r == -1

    grid = [[1, 0, 1], [0, 0, 0], [0, 1, 0]]
    s = Solution()
    r = s.shortestDistance(grid)
    #assert r == 4
