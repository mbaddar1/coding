from typing import List, Tuple


class Solution:
    def __init__(self):
        self.visited = set()
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        max_area = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    a = self.area(i,j,grid)
                    max_area = max(max_area, a)
                    # print(a)
                    for idx in self.visited:
                        grid[idx[0]][idx[1]] = -1
                    self.visited.clear()
        return max_area
    @staticmethod
    def get_neighbors(i, j, n, m) -> List[Tuple[int,int]]:
        neighbors = []
        deltas = [(-1,0),(1,0),(0,-1),(0,1)]
        for delta in deltas:
            i1 = i + delta[0]
            j1 = j + delta[1]
            if 0 <= i1 < n and 0 <= j1 < m and grid[i1][j1] == 1:
                neighbors.append((i1,j1))
        return neighbors

    def area(self,i,j,grid: List[List[int]]):
        self.visited.add((i,j))
        neighbors = self.get_neighbors(i,j,len(grid),len(grid[0]))
        neighbors_area = 0
        for neighbor in neighbors:
            if not (neighbor in self.visited):
                neighbors_area += self.area(neighbor[0],neighbor[1],grid)
        return 1+neighbors_area

if __name__=="__main__":
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    sol = Solution()
    r = sol.maxAreaOfIsland(grid)
    print(r)