"""
https://leetcode.com/problems/word-pattern-ii/description/
"""


class Solution:
    mapping:dict = {}
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        return self.match_aux(pattern,s)
    def match_aux(self,pattern:str,s:str)->bool:
        if len(pattern)==0 and len(s)==0:
            return True
        elif len(pattern)>0 and len(s)==0:
            return False
        elif len(pattern)==0 and len(s)>0:
            return False
        # map pattern[0]
        c = pattern[0]
        if c in self.mapping:
            mapped_str = self.mapping[c]
            next_pattern = pattern[1:]
            next_s = s[len(mapped_str):]
            return self.match_aux(next_pattern,next_s)
        #elif len(pattern)>=2 and pattern[1] in self.mapping:
        #    mapped_str_1 = self.mapping[pattern[1]]
        #    i = 0
        #    while i<len(s):
        #        if s[i]==mapped_str_1[0]:
        #            break
        #        i = i+1
        #    mapped_str = s[:i]
        #    self.mapping[c] = mapped_str

        else:
            r = False
            for i in range(1,len(s)):
                mapped_str = s[:i]
                next_pattern = pattern[1:]
                next_s = s[len(mapped_str):]
                self.mapping[c] = mapped_str
                r = self.match_aux(next_pattern,next_s)
                if r:
                    break
            return r


if __name__=="__main__":
    pattern = "abab"
    s = "redblueredblue"
    sol = Solution()
    res = sol.wordPatternMatch(pattern, s)
    print(res)
    print(sol.mapping)