# https://leetcode.com/problems/generate-parentheses/
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]
        sub_r_list = self.generateParenthesis(n - 1)
        r_set = set()
        for r in sub_r_list:
            r_set.add(f'{r}()')
            r_set.add(f'({r})')
            r_set.add(f'(){r}')
        return r_set


if __name__ == '__main__':
    s = Solution()
    r = s.generateParenthesis(3)
    print(r)
