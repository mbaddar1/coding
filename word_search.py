"""
https://leetcode.com/problems/word-search/
"""
from typing import List

import numpy as np


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        visited = np.zeros((m, n))
        for i in range(m):
            for j in range(n):
                r = self.exist_root(board, word, i, j,visited)
                if r:
                    return True
        return False

    def exist_root(self, board: List[List[str]], word: str, i, j, visited) -> bool:
        m = len(board)
        n = len(board[0])
        # visited = np.zeros(shape=(m, n))
        # for i in range(m):
        #     for j in range(n):
        #         # if visited[i][j] == 0:

        if board[i][j] == word[0] and visited[i][j] == 0:
            visited[i][j] = 1
            if len(word) == 1:
                return True
            else:
                neigh = self.getNieghbors(i, j, m, n)
                for ix, jx in neigh:
                    r = self.exist_root(board, word[1:], ix, jx, visited)
                    if r:
                        return True
                return False
        else:
            return False

    def getNieghbors(self, i, j, m, n):
        neigh = []
        if i > 0:
            neigh.append((i - 1, j))
        if i < m - 1:
            neigh.append((i + 1, j))
        if j > 0:
            neigh.append((i, j - 1))
        if j < n - 1:
            neigh.append((i, j + 1))
        return neigh


if __name__ == '__main__':
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    s = Solution()
    print(s.exist(board, word))

    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "SEE"
    print(s.exist(board, word))

    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCB"
    print(s.exist(board, word))
