# https://leetcode.com/problems/valid-sudoku/
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])
        rows_sets = [set() for i in range(rows)]
        cols_sets = [set() for i in range(cols)]
        sub_boxes_sets = [[set() for j in range(int(cols / 3))] for i in range(int(rows / 3))]
        for i in range(rows):
            for j in range(cols):
                if board[i][j] != ".":
                    if board[i][j] in rows_sets[i]:
                        return False
                    rows_sets[i].add(board[i][j])
                    if board[i][j] in cols_sets[j]:
                        return False
                    cols_sets[j].add(board[i][j])
                    i_ = int(i / 3)
                    j_ = int(j / 3)
                    if board[i][j] in sub_boxes_sets[i_][j_]:
                        return False
                    sub_boxes_sets[i_][j_].add(board[i][j])
        return True


if __name__ == '__main__':
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    s = Solution()
    r = s.isValidSudoku(board)
    print(r)

    board = [["8", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    r = s.isValidSudoku(board)
    print(r)