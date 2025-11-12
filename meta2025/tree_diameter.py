"""
https://leetcode.com/problems/diameter-of-binary-tree/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.diameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.getMaxPathFromRootRecursive(root)

    def getMaxPathFromRootRecursive(self, root: Optional[TreeNode]) -> int:
        left_max_path = 0
        if root.left is not None:
            left_max_path = 1 + self.getMaxPathFromRootRecursive(root.left)
        right_max_path = 0
        if root.right is not None:
            right_max_path = 1 + self.getMaxPathFromRootRecursive(root.right)
        self.diameter = max(self.diameter, left_max_path + right_max_path)
        return max(left_max_path,right_max_path)


if __name__ == '__main__':
    root_list = [1, 2, 3, 4, 5]
    aux_list = [None]*len(root_list)
    for i in range(len(root_list)):
        if aux_list[i] is None:
            node = TreeNode(val=root_list[i])
            aux_list[i] = node
        else:
            node = aux_list[i]
        left_idx = 2*i+1
        if left_idx < len(root_list):
            node.left = TreeNode(val=root_list[left_idx])
            aux_list[left_idx] = node.left
        right_idx = 2*i+2
        if right_idx < len(root_list):
            node.right = TreeNode(val=root_list[right_idx])
            aux_list[right_idx] = node.right
    root_node = aux_list[0]
    sol = Solution()
    sol.diameterOfBinaryTree(root_node)
    print(sol.diameter)

