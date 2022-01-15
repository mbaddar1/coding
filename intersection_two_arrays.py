"""
https://leetcode.com/explore/interview/card/facebook/54/sorting-and-searching-3/3033/
"""


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n1 = len(nums1)
        n2 = len(nums2)
        if nums1 is None or nums2 is None or n1 == 0 or n2 == 0:
            return []
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        i1 = i2 = 0
        intersect_set = set()
        while i1 < n1 and i2 < n2:
            if nums1[i1] == nums2[i2]:
                intersect_set.add(nums1[i1])
                i1 += 1
                i2 += 1
            elif nums1[i1] < nums2[i2]:
                i1 += 1
            else:
                i2 += 1
        return list(intersect_set)


if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    r = s.intersection(nums1=nums1, nums2=nums2)
    assert set(r) == {2}

    s = Solution()
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    r = s.intersection(nums1=nums1, nums2=nums2)
    assert set(r) == {4, 9}

    s = Solution()
    nums1 = [9, 8, 7]
    nums2 = [1, 2]
    r = s.intersection(nums1=nums1, nums2=nums2)
    assert set(r) == set([])

    s = Solution()
    nums1 = [4, 5, 6]
    nums2 = [6, 5, 4]
    r = s.intersection(nums1=nums1, nums2=nums2)
    assert set(r) == {4, 5, 6}

    s = Solution()
    nums1 = [2, 2, 1]
    nums2 = [1, 2]
    r = s.intersection(nums1=nums1, nums2=nums2)
    assert set(r) == {1, 2}

    s = Solution()
    nums1 = [2, 2, 2]
    nums2 = [2, 2]
    r = s.intersection(nums1=nums1, nums2=nums2)
    assert set(r) == {2}
