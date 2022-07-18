# https://leetcode.com/problems/search-in-rotated-sorted-array/
# https://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/
from typing import List


class Solution:

    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        pivot = Solution.findPivot(nums)

        if target == nums[pivot]:
            r= pivot
        elif nums[0] <= target < nums[pivot]:
            r = Solution.binSearch(nums, 0, pivot - 1, target)
        elif nums[pivot] < target <= nums[n-1]:
            r = Solution.binSearch(nums, pivot + 1, n-1, target)
        else:
            r = -1
        return r

    @staticmethod
    def binSearch(nums, low, high, target):
        low_ = low
        high_ = high
        while low <= high:
            mid = int((low_ + high_) / 2)
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                low_ = mid + 1
            else:
                high_ = mid - 1
        return -1

    @staticmethod
    def findPivot(nums):
        n = len(nums)
        low = 0
        high = n - 1
        while low <= high:
            mid = int((low + high) / 2)

            if mid < n - 1 and nums[mid] > nums[mid + 1]:
                return mid
            if nums[mid] > nums[low]:
                low = mid
            else:
                high = mid


if __name__ == '__main__':
    a = [5, 6, 1, 2, 3, 4]
    a1 = [5, 6, 7, 8, 1, 2]
    a2 = [5, 6, 7, 1, 2, 3]
    s = Solution()
    r = s.search(a, 7)
    print(r)
