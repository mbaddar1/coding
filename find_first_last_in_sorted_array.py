"""
https://leetcode.com/explore/interview/card/facebook/54/sorting-and-searching-3/3030/
https://leetcode.com/submissions/detail/637760959/?from=explore&item_id=3030
"""
import logging


def is_first(i, nums):
    if i == 0:
        return True
    if len(nums) == 1:
        return True
    return nums[i - 1] != nums[i]


def is_last(i, nums):
    if len(nums) == 1:
        return True
    if i == len(nums) - 1:
        return True
    return nums[i + 1] != nums[i]


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        first = Solution.search(nums, target, True)
        if first == -1:
            last = -1
        else:
            last = Solution.search(nums, target, False)
        return [first, last]

    @staticmethod
    def search(nums, target, first_flag):
        if nums is None:
            return -1
        n = len(nums)
        if n == 0:
            return -1
        i = 0
        j = n - 1
        while i <= j:
            mid = int((i + j) / 2)
            additional = is_first(mid, nums) if first_flag else is_last(mid, nums)
            nums_mid = nums[mid]
            if nums[mid] == target and additional:
                return mid
            elif target < nums[mid]:
                j = mid - 1
            elif target > nums[mid]:  # nums[mid] > target
                i = mid + 1
            else:
                if first_flag:
                    j = mid - 1
                else:
                    i = mid + 1
        return -1


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    s = Solution()

    # nums = [5, 7, 7, 8, 8, 10]
    # target = 8
    # r = s.searchRange(nums, target)
    # assert r == [3, 4]
    #
    # nums = [5, 7, 7, 8, 8, 10]
    # target = 8
    # r = s.searchRange(nums, target)

    test_cases = [([5, 7, 7, 8, 8, 10], 8, [3, 4]),
                  ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
                  ([], 0, [-1, -1])]
    for test_case in test_cases:
        nums = test_case[0]
        target = test_case[1]
        expected = test_case[2]
        actual = s.searchRange(nums, target)
        assert actual == expected
