from typing import List
# submisstion
# https://leetcode.com/submissions/detail/777704275/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n == 0:
            return [[]]
        max_i = int((n - 1) / 2)
        i = 0
        while i <= max_i:

            corner1 = i, i
            corner2 = i, n - 1 - i
            corner3 = n - 1 - i, n - 1 - i
            corner4 = n - 1 - i, i
            offset = 0
            max_offset = n - 2 * (i + 1)
            max_offset = max_offset if max_offset >= 0 else 0
            while offset <= max_offset:
                idx1 = corner1[0], corner1[1] + offset
                idx2 = corner2[0] + offset, corner2[1]
                idx3 = corner3[0], corner3[1] - offset
                idx4 = corner4[0] - offset, corner1[1]
                tmp = matrix[idx1[0]][idx1[1]]
                matrix[idx1[0]][idx1[1]] = matrix[idx4[0]][idx4[1]]
                matrix[idx4[0]][idx4[1]] = matrix[idx3[0]][idx3[1]]
                matrix[idx3[0]][idx3[1]] = matrix[idx2[0]][idx2[1]]
                matrix[idx2[0]][idx2[1]] = tmp
                offset += 1
            i += 1


if __name__ == '__main__':
    # matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    # matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # matrix = [[5]]
    # matrix = [[1,2],[3,4]]
    # matrix = [[]]
    matrix = [[2, 29, 20, 26, 16, 28], [12, 27, 9, 25, 13, 21], [32, 33, 32, 2, 28, 14], [13, 14, 32, 27, 22, 26],
              [33, 1, 20, 7, 21, 7], [4, 24, 1, 6, 32, 34]]
    print(matrix)
    s = Solution()
    s.rotate(matrix)
    print(matrix)

    # TODO
    # https://leetcode.com/submissions/detail/776885897/
    # [[4,33,13,32,12,2],[24,1,14,33,27,29],[1,20,32,32,9,20],[6,7,27,2,25,26],[32,21,22,28,13,16],[34,7,26,14,21,28]]