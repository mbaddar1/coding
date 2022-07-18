from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lower_ = Solution.binSearch(nums, target, True)
        if lower_ == -1:
            return [-1, -1]
        upper_ = Solution.binSearch(nums, target, False)
        return [lower_, upper_]

    @staticmethod
    def binSearch(nums, target, is_lower_bound):
        n = len(nums)
        low = 0
        high = n - 1
        while low <= high:
            mid = int((low + high) / 2)
            if is_lower_bound:
                if target == nums[mid]:

                    if mid == 0 or nums[mid] != nums[mid - 1]:
                        return mid
                    else:
                        high = mid - 1
                elif target > nums[mid]:
                    low = mid + 1
                else:  # target < nums[mid]
                    high = mid - 1
            else:  # find upper bound
                if target == nums[mid]:
                    if mid == n - 1 or nums[mid] != nums[mid + 1]:
                        return mid
                    else:
                        low = mid + 1

                elif target > nums[mid]:
                    low = mid + 1
                else:  # target < nums[mid]
                    high = mid - 1
        return -1


if __name__ == '__main__':
    s = Solution()
    assert s.searchRange([1, 2, 5, 5, 5, 5, 8], 5) == [2, 5]
    assert s.searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert s.searchRange([5, 7, 7, 8, 8, 10], 7) == [1, 2]
    assert s.searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1]