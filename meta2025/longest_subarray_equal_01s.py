"""
Longest Subarray with Equal Number of 0s and 1s
Given an array nums consisting only of 0s and 1s, return the length of the longest contiguous subarray that contains an equal number of 0s and 1s.
Example 1:
Input: nums = [0,1,0,1,1,0]
Output: 6
Example 2:
Input: nums = [0,1,1,1,0,0,1]
Output: 6

Status
quick soln, GBL - Get Back Later
"""
from typing import List

def find_longest_subarray(nums:List[int]) -> int:
    n = len(nums)
    cum_sum_arr = [0]*n
    cum_sum_arr[0] = nums[0]
    for i in range(1,n):
        cum_sum_arr[i] = cum_sum_arr[i-1] + nums[i]
    i = 0
    j = n-1
    while j >= i:
        sub_n = j-i+1
        sum_ij = cum_sum_arr[j]-cum_sum_arr[i]+nums[i]
        if sum_ij == sub_n/2:
            break
        elif sum_ij > sub_n/2:
            if nums[i]==1:
                i = i+1
            else:
                j = j-1
        else:
            i = i+1
    if i>j:
        return -1
    else:
        return (j-i)+1
if __name__=="__main__":
    # a = [0,1,0,1,1,0]
    # r = find_longest_subarray(a)
    # print(r)

    nums = [0, 1, 1, 1, 0, 0, 1]
    r = find_longest_subarray(nums)
    print(r)
