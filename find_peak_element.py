"""
https://leetcode.com/explore/interview/card/facebook/54/sorting-and-searching-3/3032/
https://leetcode.com/submissions/detail/636582169/?from=explore&item_id=3032
"""
import logging

from utils import MyAssert


class Solution(object):
    @staticmethod
    def is_left_lower(i, nums):
        if i - 1 == -1:
            return True
        return nums[i - 1] < nums[i]

    @staticmethod
    def is_right_lower(i, nums):
        n = len(nums)
        if i + 1 == n:
            return True
        return nums[i + 1] < nums[i]

    @staticmethod
    def is_peak(i, nums):
        is_left_lower_val = Solution.is_left_lower(i, nums)
        is_right_lower_val = Solution.is_right_lower(i, nums)
        return is_left_lower_val and is_right_lower_val

    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None:
            return -1
        n = len(nums)
        if n == 0:
            return -1
        if n == 1:
            return 0
        i = 0
        j = n - 1
        while i <= j:
            mid = int((i + j) / 2)
            if Solution.is_peak(mid, nums):
                return mid
            elif Solution.is_left_lower(mid, nums):
                i = mid + 1
            else:
                j = mid - 1


if __name__ == '__main__':
    myassert = MyAssert()
    s = Solution()
    logging.basicConfig(level=logging.INFO)

    nums = [1, 2, 3, 1]
    r = s.findPeakElement(nums)
    myassert.asser_in_list(r, [2])

    nums = [1, 2, 1, 3, 5, 6, 4]
    r = s.findPeakElement(nums)
    myassert.asser_in_list(r, [1, 5])

    nums = [6, 5, 4, 3, 2, 1]
    r = s.findPeakElement(nums)
    myassert.asser_in_list(r, [0])

    nums = [1, 2, 3, 4, 5, 6]
    r = s.findPeakElement(nums)
    myassert.asser_in_list(r, [5])

    nums = [5, 6, 7, 1, 8, 9]
    r = s.findPeakElement(nums)
    myassert.asser_in_list(r, [2, 5])

    nums = [5]
    r = s.findPeakElement(nums)
    myassert.asser_in_list(r, [0])

    nums = [5,6]
    r = s.findPeakElement(nums)
    myassert.asser_in_list(r, [1])

