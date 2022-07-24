# https://leetcode.com/problems/group-anagrams/
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for s in strs:
            k = "".join(sorted(s))
            if k in group.keys():
                group[k].append(s)
            else:
                group[k] = [s]
        group2 = [l for l in group.values()]
        return group2


if __name__ == '__main__':
    s = Solution()
    r = s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(r)
    r = s.groupAnagrams([""])
    print(r)
    r = s.groupAnagrams(["a"])
    print(r)
