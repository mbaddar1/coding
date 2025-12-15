# https://leetcode.com/problems/rotate-image/description/
# https://leetcode.com/problems/rotate-image/submissions/1856443513
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        for i in range(n // 2):
            for j in range(i, n - i-1):
                # first overwrite : bottom-row => left-column

                row1 = j
                col1 = i
                tmp = matrix[row1][col1]
                row2 = n - 1 - i
                col2 = j
                matrix[row1][col1] = matrix[row2][col2]

                # 2nd overwrite right-col -> bottom row
                col1 = col2
                row1 = row2

                col2 = n-1-i
                row2 = n-1-j
                matrix[row1][col1] = matrix[row2][col2]

                # 3rd overwrite upper row -> right col
                col1 = col2
                row1 = row2
                col2 = n-1-j
                row2 = i
                matrix[row1][col1] = matrix[row2][col2]

                # 4th overite - left-col -> upper row
                col1 = col2
                row1 = row2
                matrix[row1][col1] = tmp


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    sol = Solution()
    sol.rotate(matrix)
    print(matrix)

    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    sol.rotate(matrix)
    print(matrix)
