"""
https://leetcode.com/problems/longest-palindromic-substring/description/
done
https://leetcode.com/problems/longest-palindromic-substring/submissions/1863287099
"""
class Solution:
    def __init__(self):
        self.palindromes = []
        self.debug=False
    def __print(self,s):
        k = [s[e[0]:e[1]+1] for e in self.palindromes]
        print(k)
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_len = 1
        max_palindrome = s[0]
        if self.debug:
            print("adding palindromes of size 1")
        for i in range(n):
            self.palindromes.append((i,i))
        if self.debug:
            self.__print(s)
            print("adding palindromes of size 2")
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                max_len = 2
                max_palindrome = s[i:i+2]
                self.palindromes.append((i, i + 1))
        if self.debug:
            self.__print(s)
            print("Searching for larger palindromes")
        while len(self.palindromes) > 0:
            e = self.palindromes.pop(0)
            l = e[0]-1
            h = e[1]+1
            if l>=0 and h<=n-1 and s[l] == s[h]:
                max_len = h-l+1
                max_palindrome= s[l:(h+1)]
                self.palindromes.append((l, h))
                if self.debug:
                    print(f"adding palindrome = {s[l:h+1]}, max_len = {max_len}")
            if self.debug:
                self.__print(s)
        return max_palindrome


if __name__=="__main__":
    s = "cbbd"
    sol = Solution()
    r = sol.longestPalindrome(s)
    print(r)