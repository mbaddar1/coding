"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/submissions/1863341785/
"""
from typing import List
class Solution:
    def __init__(self):
        self.letter_map = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        self.memoization_map = {}
    def letterCombinations(self, digits: str) -> List[str]:
        return self.get_combinations(digits)
    def get_combinations(self,digits: str) -> List[str]:
        if len(digits) == 1:
            mapped_str = self.letter_map.get(digits[0])
            combs=[x for x in mapped_str]
            return combs
        else:
            combs = []
            mapped_str = self.letter_map.get(digits[0])
            sub_comps = self.get_combinations(digits[1:])
            for c in mapped_str:
                for sub_comp in sub_comps:
                    combs.append(str(c)+sub_comp)
            return combs

if __name__ == "__main__":
    digits = "23"
    sol = Solution()
    res = sol.letterCombinations(digits)