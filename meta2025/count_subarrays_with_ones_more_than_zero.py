# https://leetcode.com/problems/count-subarrays-with-more-ones-than-zeros/description/
from typing import List
class Solution:
    def subarraysWithMoreOnesThanZeroes(self, nums: List[int]) -> int:
        # init
        n = len(nums)
        total_count = 0
        # memory = dict()
        queue = list()
        for i in range(n):
            queue.append((i,i,nums[i]))
            # memory[(i,i)] = nums[i]
            if nums[i] ==1:
                total_count += 1
                # print(f"{(i,i)} - OK")
        while len(queue) >0:
            e = queue.pop(0)
            # assert e in memory.keys(),"each entry in queue must be in memory(dict)"
            # c = memory[e]
            # del memory[e] # no longer needed
            # only right extension
            right_idx_ext = e[1]+1
            if right_idx_ext <=n-1:
                new_ones_count = e[2] + nums[right_idx_ext]
                # memory[e[0],right_idx_ext] = new_ones_count
                new_zeros_count = (right_idx_ext-e[0])+1-new_ones_count
                if new_ones_count > new_zeros_count:
                    total_count+=1
                    # print(f"{(e[0],right_idx_ext)} - OK")
                # else:
                    # print(f"{(e[0],right_idx_ext)} - NO")
                queue.append((e[0], right_idx_ext, new_ones_count))

        mod_num = 10**9+7
        return total_count % mod_num

        #
        #     e = entries.pop(0)
        #     # check left extension
        #     left_ext_idx = e[0]-1
        #     if left_ext_idx >=0:
        #         new_ones_count = e[2]+nums[left_ext_idx]
        #         new_zeros_count = (e[1]-left_ext_idx+1)-new_ones_count
        #         if new_ones_count > new_zeros_count:
        #             total_count+=1
        #             entries.append((e[0]-1,e[1],new_ones_count))
        #     # check right extension
        #     right_ext_idx = e[1]+1
        #     if right_ext_idx <=(n-1):
        #         new_ones_count = e[2] + nums[right_ext_idx]
        #         new_zeros_count = (right_ext_idx - e[0] + 1) - new_ones_count
        #         if new_ones_count >new_zeros_count:
        #             total_count+=1
        #             entries.append((e[0],right_ext_idx,new_ones_count))
        # return total_count


if __name__ == '__main__':
    # arr = [0,1,1,0,1]
    arr = [1,1,1,0,1,1,1]
    sol = Solution()
    r = sol.subarraysWithMoreOnesThanZeroes(arr)
    print(r)