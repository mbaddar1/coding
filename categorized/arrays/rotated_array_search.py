from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return Solution.search_aux(nums,target,0,len(nums)-1)
    @staticmethod
    def search_aux(nums: List[int], target: int,low:int,high:int) -> int:
        n = len(nums)
        if low > high:
            return -1
        mid= (low+high)//2
        if nums[mid] == target:
            return mid
        if nums[0] < nums[mid]:
            if mid > 0 and nums[0] <= target < nums[mid]:
                return Solution.search_aux(nums, target, low, mid-1)
            elif mid<n-1 and (target >nums[mid] or target <=nums[n-1]):
                return Solution.search_aux(nums, target, mid+1, high)
        else: #nums[0] > mid
            if mid < n-1 and nums[mid] < target <= nums[n-1]:
                return Solution.search_aux(nums,target,mid+1,high)
            elif mid > 0 and (target< nums[mid] or target >= nums[0]):
                return Solution.search_aux(nums,target,low,mid-1)
        return -1

if __name__ == "__main__":
    arr = [4,5,6,7,0,1,2]
    sol = Solution()
    target = 10
    r = sol.search(arr,target)
    print(r)
    pass