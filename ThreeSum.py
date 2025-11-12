# https://www.linkedin.com/pulse/understanding-threesum-problem-solution-steps-jean-claude-adjanohoun-gqhmc/
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        # O(n2)
        res = set()
        for i in range(n):
            for j in range(i + 1, n):
                k = nums[i] + nums[j]
                found = self.__find(-k, nums[j+1:])
                for u in found:
                    res.add((nums[i], nums[j], nums[j+1+u]))
        return list(res)

    def __find(self, item, items_list):
        found = []
        for u in range(len(items_list)):
            if item == items_list[u]:
                found.append(u)
        return found


if __name__ == '__main__':
    sol = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    r = sol.threeSum(nums)
    print(r)
