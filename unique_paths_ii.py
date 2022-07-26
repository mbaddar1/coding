# https://leetcode.com/problems/unique-paths-ii/
from typing import List


class Solution:
    @staticmethod
    def getNeighbors(i, j, m, n, obstacleGrid):
        neighbors = []
        # down
        if (i + 1) <= m - 1 and obstacleGrid[i + 1][j] == 0:
            neighbors.append((i + 1, j))
        # right
        if (j + 1) <= n - 1 and obstacleGrid[i][j + 1] == 0:
            neighbors.append((i, j + 1))
        return neighbors

    def __init__(self):
        self.mem = {}

    def __unique_paths(self, i, j, m, n, obstacleGrid):
        if (i, j) in self.mem.keys():
            return self.mem[(i, j)]
        neighbors = Solution.getNeighbors(i, j, m, n, obstacleGrid)
        for neighbor in neighbors:
            if neighbor == (m - 1, n - 1):
                return 1
        ctr = 0
        for neighbor in neighbors:
            v = self.__unique_paths(neighbor[0], neighbor[1], m, n, obstacleGrid)
            ctr += v
        return ctr

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        r = self.__unique_paths(0, 0, m, n, obstacleGrid)
        return r


if __name__ == '__main__':
    s = Solution()
    obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    r = s.uniquePathsWithObstacles(obstacleGrid)
    print(r)
    obstacleGrid = [[0, 1], [0, 0]]
    r = s.uniquePathsWithObstacles(obstacleGrid)
    print(r)
