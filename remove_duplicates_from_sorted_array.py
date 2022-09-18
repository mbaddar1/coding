# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
from typing import List


class Solution:
    MAX_NUMBER = int(1e4)
    MIN_NUMBER = int(-1e4)
    DUMMY_NUM = MIN_NUMBER - 1

    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        # pass 1 , put displacements
        block_counter = 1
        cum_block_diff = 0
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                block_counter += 1
            else:
                if block_counter > 2:
                    cum_block_diff += block_counter - 2
                    coded_displacement = Solution.MAX_NUMBER + cum_block_diff
                    nums[i - 1] = coded_displacement
                block_counter = 1
        # pass 2 - displacement
        for j in range(n):
            if nums[j] > Solution.MAX_NUMBER:
                displacement = nums[j] - Solution.MAX_NUMBER
                counter = 0
                for k in range(j + 1, n):
                    if nums[k] > Solution.MAX_NUMBER:
                        break
                    # if counter == 2:
                    #     break

                    new_idx = k - displacement
                    nums[new_idx] = nums[k]
                    counter += 1
        n_bar = n - cum_block_diff
        return n_bar


if __name__ == '__main__':
    sol = Solution()

    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    r = sol.removeDuplicates(nums)
    print(nums[:r])

    nums = [1, 1, 1, 2, 2, 3]
    r = sol.removeDuplicates(nums)
    print(nums[:r])

    nums = [1, 1, 1, 2, 2, 3, 3, 3, 4]
    r = sol.removeDuplicates(nums)
    print(nums[:r])
