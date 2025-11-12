# https://leetcode.com/problems/merge-intervals/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
from typing import List, Tuple, Dict, Set


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        r = Solution.findPath(grid, (0, 0), set(), len(grid))
        return r

    @staticmethod
    @staticmethod
    def get_adjacent(grid: List[List[int]], pos: (int, int), n: int) -> List[Tuple[int, int]]:
        adj_list = []
        i: int = pos[0]
        j: int = pos[1]

        # left
        if j > 0 and grid[i][j - 1] == 0:
            adj_list.append((i, j - 1))
        # right:
        if j < n - 1 and grid[i][j + 1] == 0:
            adj_list.append((i, j + 1))
        # top
        if i > 0 and grid[i - 1][j] == 0:
            adj_list.append((i - 1, j))
        # bottom
        if i < n - 1 and grid[i + 1][j] == 0:
            adj_list.append((i + 1, j))
        # top-right
        if i > 0 and j < n - 1 and grid[i - 1][j + 1] == 0:
            adj_list.append((i - 1, j + 1))
        # top-left
        if i > 0 and j > 0 and grid[i - 1][j - 1] == 0:
            adj_list.append((i - 1, j - 1))
        # bottom-right
        if i < n - 1 and j < n - 1 and grid[i + 1][j + 1] == 0:
            adj_list.append((i + 1, j + 1))
        # bottom-left
        if i < n - 1 and j > 0 and grid[i + 1][j - 1] == 0:
            adj_list.append((i + 1, j - 1))
        return adj_list

    @staticmethod
    def findPath(grid: List[List[int]], curr_pos: Tuple[int, int], visited: Set[Tuple[int, int]], n: int) -> int:
        i = curr_pos[0]
        j = curr_pos[1]
        if curr_pos == (n - 1, n - 1) and grid[n - 1][n - 1] == 0:
            return 1
        if grid[i][j] == 1:
            return -1
        visited.add(curr_pos)
        adj_list = Solution.get_adjacent(grid, curr_pos, n)
        all_visited = True
        minPathLen: int = -1
        for adj_pos in adj_list:
            if adj_pos not in visited:
                all_visited = False
                path_len = Solution.findPath(grid, adj_pos, visited, n)
                if minPathLen == -1:
                    if path_len > 0:
                        minPathLen = path_len
                else:
                    if path_len > 0:
                        minPathLen = min(minPathLen, path_len)
        visited.remove(curr_pos)
        if all_visited:
            return -1
        if minPathLen == -1:
            return -1
        return 1 + minPathLen


if __name__ == "__main__":
    grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
    s = Solution()
    r = s.shortestPathBinaryMatrix(grid)
    pass
