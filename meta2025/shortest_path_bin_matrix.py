# https://leetcode.com/problems/merge-intervals/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Wrong answer
#   https://leetcode.com/problems/shortest-path-in-binary-matrix/submissions/1827798278
from typing import List, Tuple, Dict, Set


class Solution:
    INVALID = -100

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        minPaths = [[Solution.INVALID] * n for _ in range(n)]
        r = Solution.findPath(grid, (0, 0), set(), n, minPaths)
        return r

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
    def findPath(grid: List[List[int]], curr_pos: Tuple[int, int], visited: Set[Tuple[int, int]], n: int,
                 minPaths: List[List[int]]) -> int:
        i = curr_pos[0]
        j = curr_pos[1]
        if minPaths[i][j] != Solution.INVALID:
            return minPaths[i][j]
        if curr_pos == (n - 1, n - 1) and grid[n - 1][n - 1] == 0:
            r = 1
            minPaths[i][j] = r
            return r
        if grid[i][j] == 1:
            r = -1
            minPaths[i][j] = r
            return r
        visited.add(curr_pos)
        adj_list = Solution.get_adjacent(grid, curr_pos, n)
        all_visited = True
        minPathLen: int = -1
        for adj_pos in adj_list:
            if adj_pos not in visited:
                all_visited = False
                path_len = Solution.findPath(grid, adj_pos, visited, n,minPaths)
                if minPathLen == -1:
                    if path_len > 0:
                        minPathLen = path_len
                else:
                    if path_len > 0:
                        minPathLen = min(minPathLen, path_len)
        visited.remove(curr_pos)
        if all_visited:
            r = -1
            minPaths[i][j] = r
            return r
        if minPathLen == -1:
            r = -1
            minPaths[i][j] = r
            return r
        r = 1 + minPathLen
        minPaths[i][j] = r
        return r


if __name__ == "__main__":
    grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
    s = Solution()
    r = s.shortestPathBinaryMatrix(grid)
    assert r == 4
    ###
    grid = [[0, 1], [1, 0]]
    s = Solution()
    r = s.shortestPathBinaryMatrix(grid)
    assert r == 2

    # from leetcode
    grid = [[0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0]]
    s = Solution()
    r = s.shortestPathBinaryMatrix(grid)
    expected_val = 4
    assert r == expected_val,f"{r}!={expected_val}"
    print("ok")
