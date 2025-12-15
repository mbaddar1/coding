import numpy as np
import numpy.typing as npt


def get_max_row_values(matrix: npt.NDArray[np.int64]) -> npt.NDArray[np.int64]:
    """
    Return a NumPy array containing the maximum value of each row of the given matrix.
    The i-th element of the result should correspond to the i-th row of the matrix.
    """
    # implement this
    n = len(matrix[0])
    MIN_VAL = -1000
    max_rows = np.array([MIN_VAL] * n)
    for i in range(n):
        for j in range(n):
            max_rows[i]=np.maximum(max_rows[i],matrix[i][j])
    return max_rows

def get_max_column_values(matrix: npt.NDArray[np.int64]) -> npt.NDArray[np.int64]:
    """
    Return a NumPy array containing the maximum value of each column of the given matrix.
    The i-th element of the result should correspond to the i-th column of the matrix.
    """
    # implement this
    n = len(matrix[0])
    MIN_VAL = -1000
    max_cols = np.array([MIN_VAL] * n)
    for i in range(n):
        for j in range(n):
            max_cols[j] = np.maximum(max_cols[j], matrix[i][j])
    return max_cols


def solution(matrix: list[list[int]]) -> list[int]:
    np_matrix = np.array(matrix)
    return list(get_max_row_values(np_matrix) + get_max_column_values(np_matrix))

if __name__=="__main__":
    matrix = [[2, 5, 8],
              [1, 2, 10],
              [-2, 0, -1]]
    r = solution(matrix)
    print(r)

    matrix= [[-63]]
    r = solution(matrix)
    print(r)

    matrix = [[0]]
    r = solution(matrix)
    print(r)
