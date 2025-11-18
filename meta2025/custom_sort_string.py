"""
https://leetcode.com/problems/custom-sort-string/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
"""


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # create order indices
        n_order = len(order)
        n_s = len(s)
        order_index = {}
        for i in range(len(order)):
            order_index[order[i]] = i
        counts = [0] * n_order
        tmp_str = ""
        for i in range(n_s):
            if s[i] in order_index.keys():
                counts[order_index[s[i]]] += 1
            else:
                tmp_str += s[i]

        final_s = ""
        for j in range(n_order):
            if counts[j] > 0:
                c = order[j]
                for k in range(counts[j]):
                    final_s = final_s + c
        final_s = final_s + tmp_str
        assert len(final_s) == len(s) # sanity check
        return final_s


if __name__ == "__main__":
    order = "bcafg"
    s = "abcd"
    sol = Solution()
    r = sol.customSortString(order, s)
    assert r == "bcad"
    #
    order = "bcafg"
    s = "abcdb"
    sol = Solution()
    r = sol.customSortString(order, s)
    assert r == "bbcad"
    #
    order = "bcafg"
    s = "abcd"
    sol = Solution()
    r = sol.customSortString(order, s)
    assert r == "bcad"




