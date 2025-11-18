"""
https://chatgpt.com/share/691a0e33-50d0-8010-aea5-889ad046027d

Problem:
Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0, 1] because 2 + 7 = 9.

Constraints:

Exactly one valid answer

You may not use the same element twice

Return in any order
"""
from typing import List


def two_sum(a:List[int],target:int):
    n= len(a)
    val_pos=dict()
    val_pos[a[0]]=0
    for i in range(1,n):
        key_ = target-a[i]
        if key_ in val_pos.keys():
            first_idx = min(i,val_pos[key_])
            max_idx = max(i,val_pos[key_])
            return first_idx, max_idx
        val_pos[a[i]] = i
    return -1, -1


if __name__=="__main__":
    r = two_sum([2,7,11,15], 9)
    print(r)

    nums = [3, 1, 9, 14, 7, 22, 5, 11, 8, 17, 4, 6]
    target = 19
    r = two_sum(nums, target)
    print(r)

    nums = [10, 2, 4, 23, 7, 18, 9, 30, 11, 21, 13, 1, 6, 8, 12]
    target = 25
    r = two_sum(nums, target)
    print(r)

    nums = [5, 3, 8, 12, 7]
    target = 50
    r = two_sum(nums, target)
    print(r)