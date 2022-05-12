# https://leetcode.com/problems/valid-palindrome-ii/
# success https://leetcode.com/problems/valid-palindrome-ii/submissions/
import numpy as np


class Solution:
    def validPalindromeHelper_attempt_1(self, s: str, i: int, j: int):
        n = j - i + 1
        if n <= 1:
            return True
        cond1 = s[i] == s[j] and self.validPalindromeHelper(s, i + 1, j - 1)
        cond2 = s[i + 1] == s[j] and self.validPalindromeHelper(s, i + 2, j - 1)
        cond3 = s[i] == s[j - 1] and self.validPalindromeHelper(s, i + 1, j - 2)
        return cond1 or cond2 or cond3

    def validPalindrome_attempt_1(self, s: str) -> bool:
        return self.validPalindromeHelper(s, 0, len(s) - 1)

    def validPalindrome(self, s: str) -> bool:
        n = len(s)

        if n <= 1:
            return True

        ret = np.zeros(shape=2, dtype=bool)
        ret[0] = ret[1] = True
        for direction in range(2):  # 0 skip a , 1 skip j
            tolerance = 1
            i = 0
            j = n - 1
            while j >= i:
                if s[i] != s[j] and tolerance == 0:
                    ret[direction] = False
                    break
                elif s[i] != s[j] and tolerance == 1:
                    tolerance = 0
                    if direction == 0:
                        i = i + 1
                    else:
                        j = j - 1
                else:
                    i = i + 1
                    j = j - 1

        return ret[0] or ret[1]


if __name__ == '__main__':
    s = Solution()
    assert s.validPalindrome("cbbcc") == True
    assert s.validPalindrome("abba") == True
    assert s.validPalindrome("aba") == True
    assert s.validPalindrome("abba") == True
    assert s.validPalindrome("a") == True
    assert s.validPalindrome("") == True
    assert s.validPalindrome("ab") == True
    assert s.validPalindrome("abc") == False
    assert s.validPalindrome("abca") == True
    assert s.validPalindrome("abdca") == False
