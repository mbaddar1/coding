"""
https://leetcode.com/problems/3sum-closest/
"""
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums_sorted = sorted(nums)  # nlogn
        min_diff = 1000000000000
        min_idx = -1, -1, -1
        pair_sums_dict = self.twoSum(nums_sorted)  # n^2 on num_sorted not num for idx consistency
        for asum in pair_sums_dict.keys():
            for u, v in pair_sums_dict[asum]:
                m = target - asum
                x, y, _ = self.binSearch(nums_sorted, m)  # logn
                if x is None and u != y and v != y:
                    if abs(target - nums_sorted[y]) < min_diff:
                        min_diff = abs(target - nums_sorted[y] - nums_sorted[u] - nums_sorted[v])
                        min_idx = u, v, y
                elif y is None and u != x and v != x:
                    if abs(target - nums_sorted[x]) < min_diff:
                        min_diff = abs(target - nums_sorted[x] - nums_sorted[u] - nums_sorted[v])
                        min_idx = u, v, x
                elif x is not None and y is not None:
                    z = x if abs(target - nums_sorted[x]) < abs(target - nums_sorted[y]) else y
                    if u != z and v != z and abs(target - nums_sorted[z] - nums_sorted[u] - nums_sorted[v]) < min_diff:
                        min_diff = abs(target - nums_sorted[z] - nums_sorted[u] - nums_sorted[v])
                        min_idx = u, v, z
        return nums_sorted[min_idx[0]] + nums_sorted[min_idx[1]] + nums_sorted[min_idx[2]]

    def twoSum(self, nums):
        sum_dict = {}
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] in sum_dict.keys():
                    sum_dict[nums[i] + nums[j]].append((i, j))
                else:
                    sum_dict[nums[i] + nums[j]] = [(i, j)]
        return sum_dict

    def binSearch(self, arr, value):
        lower = 0
        upper = len(arr) - 1

        while lower <= upper:
            mid = int((lower + upper) / 2)
            if arr[mid] == value:
                return mid, mid, True

            if value > arr[mid]:
                if mid + 1 > upper:
                    to_return = mid, mid + 1 if mid < len(arr) - 1 else None, False
                    return to_return
                else:
                    lower = mid + 1
            else:
                if mid - 1 < lower:
                    to_return = mid - 1 if mid > 0 else None, mid, False
                    return to_return
                else:
                    upper = mid - 1


if __name__ == '__main__':
    a = [2, 4, 6, 8]
    s = Solution()
    # r = s.binSearch(a, 6)
    # print(r)
    r = s.threeSumClosest([-1, 2, 1, -4], 1)
    print(r)
    r = s.threeSumClosest([0, 0, 0], 1)
    print(r)
