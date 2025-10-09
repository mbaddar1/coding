# https://leetcode.com/problems/dot-product-of-two-sparse-vectors/submissions/1796422961/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
from typing import List
class SparseVector:

    def __init__(self, nums: List[int]):
        self.data = dict()
        for i in range(len(nums)):
            if nums[i] != 0:
                self.data[i] = nums[i]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        sum_ = 0
        for k1 in self.data.keys():
            if k1 in vec.data.keys():
                sum_ += self.data[k1] * vec.data[k1]
        return sum_


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)

if __name__ == '__main__':
    v1 = SparseVector([1,0,0,2,3])
    v2 = SparseVector([0,3,0,4,0])
    r = v1.dotProduct(v2)
    print(r)
    v1 = SparseVector([0, 1, 0, 0, 0])
    v2= SparseVector([0, 0, 0, 0, 2])
    r = v1.dotProduct(v2)
    print(r)
    v1 = SparseVector([0, 1, 0, 0, 2, 0, 0])
    v2 = SparseVector([1, 0, 0, 0, 3, 0, 4])
    r = v1.dotProduct(v2)
    print(r)

