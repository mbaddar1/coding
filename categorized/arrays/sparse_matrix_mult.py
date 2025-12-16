# https://leetcode.com/problems/sparse-matrix-multiplication/submissions/1857111332
from typing import List


class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        n = len(mat1)
        m = len(mat1[0])
        assert m == len(mat2)
        q = len(mat2[0])
        res = [[0 for _ in range(q)] for _ in range(n)]
        for i in range(n):
            for k in range(q):
                for j in range(m):
                    if mat1[i][k] ==0 or  mat2[k][j]==0:
                        continue
                    res[i][k]+= mat1[i][j]*mat2[j][k]
        return res


if __name__ == "__main__":
    mat1 = [[1, 0, 0], [-1, 0, 3]]
    mat2 = [[7, 0, 0], [0, 0, 0], [0, 0, 1]]
    sol = Solution()
    r = sol.multiply(mat1, mat2)
    print(r)
