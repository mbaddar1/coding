"""
https://leetcode.com/problems/zigzag-conversion/
"""
import numpy as np


def zigzag(l, rows):
    if rows == 1:
        return l
    l = [c for c in l]
    res = []
    for r in range(rows):
        if r == 0 or r == rows - 1:
            k = 0
            finished = False
            while not finished:
                idx = r + k * 2 * (rows - 1)
                if 0 <= idx <= (len(l) - 1):
                    res.append(l[idx])
                if idx > (len(l) - 1):
                    finished = True
                k = k + 1
        else:
            k = 0
            finished = False
            while not finished:
                idx1 = r + k * 2 * (rows - 1) - 2 * r
                idx2 = r + k * 2 * (rows - 1)
                if 0 <= idx1 <= (len(l) - 1):
                    res.append(l[idx1])
                if 0 <= idx2 <= (len(l) - 1):
                    res.append(l[idx2])
                if idx2 > (len(l) - 1):
                    finished = True
                k = k + 1
    return ''.join(res)
    #


if __name__ == '__main__':
    # l = list(np.arange(20))
    # res = zigzag_list(l, 5)
    # print(res)
    # in_ = "PAYPALISHIRING"
    # out_ = "PAHNAPLSIIGYIR"
    # r = zigzag_list(in_, 3)
    # assert r == out_
    #
    # in_ = "PAYPALISHIRING"
    # out_ = "PINALSIGYAHRPI"
    # r = zigzag_list(in_, 4)
    # assert r == out_

    in_ = "A"
    out_ = "A"
    r = zigzag(in_, 1)
    assert r == out_
