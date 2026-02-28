from typing import List
"""

https://leetcode.com/problems/minimum-path-sum/submissions/1863637115/
"""
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        arr = [[0 for _ in range(m)] for _ in range(n)]
        arr[0][0] = grid[0][0]
        for j in range(1,m):
            arr[0][j] = arr[0][j-1] + grid[0][j]
        for i in range(1,n):
            arr[i][0] = arr[i-1][0] + grid[i][0]
        for i in range(1,n):
            for j in range(1,m):
                arr[i][j] = grid[i][j] + min(arr[i-1][j], arr[i][j-1])
        return arr[n-1][m-1]

if __name__=="__main__":
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    sol = Solution()
    r = sol.minPathSum(grid)
    print(r)

    grid = [[1, 2, 3], [4, 5, 6]]
    sol = Solution()
    r = sol.minPathSum(grid)
    print(r)
