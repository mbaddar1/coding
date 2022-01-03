"""
https://leetcode.com/explore/interview/card/facebook/52/trees-and-graphs/3022/
submission
https://leetcode.com/submissions/detail/612056630/?from=explore&item_id=3022
"""


# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inOrder(root, list_):
    if root.left is not None:
        inOrder(root.left, list_)
    list_.append(root.val)
    if root.right is not None:
        inOrder(root.right, list_)


"""
failed cases , to learn from
[1,-2,-3,1,3,-2,null,-1]
Output:
4
Expected:
3
"""


class Solution(object):
    def isLeaf(self, root):
        return root.left is None and root.right is None

    def maxPathSum(self, root):
        self.global_max = -2000
        if root is None:
            return 0
        if self.isLeaf(root):
            return root.val

        self.maxPathSumWrapper(root)
        return self.global_max

    def maxPathSumWrapper(self, root):

        max_left_path = None if root.left is None else self.maxPathSumWrapper(root.left)
        max_right_path = None if root.right is None else self.maxPathSumWrapper(root.right)
        self.global_max = max(self.global_max, root.val)
        self.global_max = max(self.global_max,
                              root.val + max_left_path) if max_left_path is not None else self.global_max
        self.global_max = max(self.global_max,
                              root.val + max_right_path) if max_right_path is not None else self.global_max
        self.global_max = max(self.global_max,
                              root.val + max_left_path + max_right_path) \
            if max_left_path is not None and max_right_path is not None else self.global_max
        to_return = max(root.val, root.val + max_left_path) if max_left_path is not None else root.val
        to_return = max(to_return, root.val + max_right_path) if max_right_path is not None else to_return

        return to_return

    def maxPathSum_false(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        list_ = []
        inOrder(root, list_)
        # print(list_)
        max_ = self.maxContig(list_)
        return max_

    def maxContig(self, list_):
        n = len(list_)
        if n == 0:
            return 0
        if n == 1:
            return list_[0]
        max_ = list_[0]
        running_max = max_
        running_max_last_index = 0
        for i in range(1, n):
            if list_[i] >= 0:
                if i == running_max_last_index + 1 and running_max > 0:
                    running_max = running_max + list_[i]
                    running_max_last_index = i
                else:
                    running_max = list_[i]
                    running_max_last_index = i
            else:
                if list_[i] > max_:
                    max_ = list_[i]
            max_ = max(running_max, max_)
        return max_


if __name__ == '__main__':
    # # case 1
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    sol = Solution()
    s = sol.maxPathSum(root)
    print(s)

    # case 2
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    sol = Solution()
    s = sol.maxPathSum(root)
    print(s)

    # case 3
    root = TreeNode(1)
    root.left = TreeNode(-2)
    root.right = TreeNode(-3)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.left.left.left = TreeNode(-1)
    root.right.left = TreeNode(-2)
    l = []
    inOrder(root,l)
    print(l)
    sol = Solution()
    s = sol.maxPathSum(root)
    print(s)

    # case 3
    root = TreeNode(1)
    root.right = TreeNode(2)
    l = []
    inOrder(root,l)
    print(l)
    sol = Solution()
    s = sol.maxPathSum(root)
    print(s)

    # case 4
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(4)
    root.left.left.left.left = TreeNode(5)
    l = []
    inOrder(root,l)
    print(l)
    sol = Solution()
    s = sol.maxPathSum(root)
    print(s)


