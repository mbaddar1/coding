"""
https://leetcode.com/problems/kth-smallest-element-in-a-bst/
success
https://leetcode.com/problems/kth-smallest-element-in-a-bst/submissions/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

# Definition for a binary tree node.
from tree_utils import construct_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.counter = 0
        self.finished = False
        self.ret = None
        self.k = None

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.inOrder(root)
        return self.ret

    def inOrder(self, root: TreeNode):
        if root.left is not None and not self.finished:
            self.inOrder(root.left)
        self.counter = self.counter + 1
        if self.counter == self.k:
            self.finished = True
            self.ret = root.val
        if root.right is not None and not self.finished:
            self.inOrder(root.right)


if __name__ == '__main__':
    s = Solution()
    root = [3, 1, 4, None, 2]
    tree_root_ = construct_tree(root)
    assert s.kthSmallest(tree_root_, 1) == 1
    ###
    s = Solution()
    root = [5, 3, 6, 2, 4, None, None, 1]
    tree_root_ = construct_tree(root)
    assert s.kthSmallest(tree_root_, 3) == 3
