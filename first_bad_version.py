"""
First Bad Version
https://leetcode.com/explore/interview/card/facebook/54/sorting-and-searching-3/272/
"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
first_bad_version = None
n = None


def isBadVersion(version):
    if first_bad_version < 1 or first_bad_version > n:
        return False
    return version >= first_bad_version


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if isBadVersion(1):
            return 1
        if not isBadVersion(n):
            return 0
        lower = 2
        upper = n
        r = self.firstBadVersionWrapper(lower, upper)
        return r

    def firstBadVersionWrapper(self, lower, upper):
        if upper < lower:
            return 0
        mid = int((lower + upper) / 2)
        r = None
        if isBadVersion(mid):
            if mid == 1 or not isBadVersion(mid - 1):
                r = mid
            else:
                r = self.firstBadVersionWrapper(lower, mid - 1)
        else:
            r = self.firstBadVersionWrapper(mid + 1, upper)
        assert r is not None
        return r


if __name__ == '__main__':
    s = Solution()
    n = 5
    # 1
    first_bad_version = 3
    r = s.firstBadVersion(n)
    assert r == first_bad_version

    # 2
    first_bad_version = 4
    r = s.firstBadVersion(n)
    assert r == first_bad_version

    # 3
    first_bad_version = 1
    r = s.firstBadVersion(n)
    assert r == first_bad_version

    # 4
    first_bad_version = n
    r = s.firstBadVersion(n)
    assert r == first_bad_version

    # 5
    first_bad_version = 0  # no bad version
    r = s.firstBadVersion(n)
    assert r == first_bad_version

    # 6
    n = 1
    first_bad_version = n  # = 1
    r = s.firstBadVersion(n)
    assert r == first_bad_version

    # 7
    n = 1
    first_bad_version = 2
    r = s.firstBadVersion(n)
    print(r)
    assert r == 0 # 0 means no bas version
