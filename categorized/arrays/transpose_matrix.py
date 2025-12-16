# https://leetcode.com/problems/transpose-matrix/submissions/1857051481

from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        matrix_T = [[0 for _ in range(rows)] for _ in range(cols) ]

        for i in range(rows):
            for j in range(cols):
                matrix_T[j][i] = matrix[i][j]
        return matrix_T



if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    # matrix = [[1,2,3],[4,5,6]]
    sol = Solution()
    sol.transpose(matrix)
    print(matrix)
