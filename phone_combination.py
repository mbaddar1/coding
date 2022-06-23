"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""
from typing import List


class Solution:
    def __init__(self):
        self.map_ = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

    def letterCombinations(self, digits: str) -> List[str]:

        d = digits[0]
        mapped = self.map_[d]
        if len(digits) == 1:
            l = [str(c) for c in mapped]
            return l

        else:
            res2 = []
            res = self.letterCombinations(digits[1:])
            for c in mapped:
                for r in res:
                    res2.append(str(c) + r)
            return res2


if __name__ == '__main__':
    s = Solution()

    r = s.letterCombinations("23")
    print(r)
    assert len(r) == 9
    r = s.letterCombinations("2")
    print(r)
    assert len(r) == 3
    r = s.letterCombinations("234")
    assert len(r) == 27
    print(r)
