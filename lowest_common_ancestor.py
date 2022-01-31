"""
https://leetcode.com/explore/interview/card/facebook/52/trees-and-graphs/3024/
status : accepted
https://leetcode.com/submissions/detail/631710807/?from=explore&item_id=3024

"""
import numpy as np


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class CapsuleTreeNode(object):
    def __init__(self, node: TreeNode):
        self.node = node
        self.parent = None  # Capsule node


def lowestCommonAncestor(root, p, q):
    stack_ = []
    root_capsule = CapsuleTreeNode(root)
    stack_.append(root_capsule)
    first_hit_path_dict = dict()
    found_count = 0
    while len(stack_) > 0 and found_count < 2:
        root_capsule = stack_.pop()
        if root_capsule.node.val in [p, q] and found_count == 0:
            found_count += 1
            curr = root_capsule
            while curr is not None:
                first_hit_path_dict[curr.node.val] = None
                curr = curr.parent
        elif root_capsule.node.val in [p, q] and found_count == 1:
            found_count += 1
            curr = root_capsule
            while curr is not None:
                if curr.node.val in first_hit_path_dict.keys():
                    return curr.node.val
                curr = curr.parent
        if root_capsule.node.right is not None:
            capsule_child = CapsuleTreeNode(root_capsule.node.right)
            capsule_child.parent = root_capsule
            stack_.append(capsule_child)
        if root_capsule.node.left is not None:
            capsule_child = CapsuleTreeNode(root_capsule.node.left)
            capsule_child.parent = root_capsule
            stack_.append(capsule_child)


def inOrderTravers(root):
    if root.left is not None:
        inOrderTravers(root.left)
    print(root.val)
    if root.right is not None:
        inOrderTravers(root.right)


def buildTreeFromArr(arr):
    if arr is None:
        return None
    n = len(arr)
    if n == 0:
        return None
    tree_obj_arr = np.empty(shape=n, dtype=TreeNode)
    for i in range(n):
        if arr[i] is not None:
            tree_obj_arr[i] = TreeNode(arr[i]) if tree_obj_arr[i] is None else tree_obj_arr[i]
            left_idx = 2 * i + 1
            right_idx = 2 * i + 2
            if left_idx < n and arr[left_idx] is not None:
                tree_obj_arr[left_idx] = TreeNode(arr[left_idx]) if tree_obj_arr[left_idx] is None else TreeNode(
                    arr[left_idx])
                tree_obj_arr[i].left = tree_obj_arr[left_idx]

            if right_idx < n and arr[right_idx] is not None:
                tree_obj_arr[right_idx] = TreeNode(arr[right_idx]) if tree_obj_arr[right_idx] is None else tree_obj_arr[
                    right_idx]
                tree_obj_arr[i].right = tree_obj_arr[right_idx]
    return tree_obj_arr[0]


if __name__ == '__main__':
    # A
    arr = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    treeNodeRoot = buildTreeFromArr(arr)
    assert lowestCommonAncestor(treeNodeRoot, 5, 1) == 3 # 1
    assert lowestCommonAncestor(treeNodeRoot, 1, 3) == 3  # 2
    assert lowestCommonAncestor(treeNodeRoot, 1, 6) == 3  # 3
    assert lowestCommonAncestor(treeNodeRoot, 7, 8) == 3  # 4
    assert lowestCommonAncestor(treeNodeRoot, 7, 4) == 2  # 5
    assert lowestCommonAncestor(treeNodeRoot, 5, 8) == 3  # 6
    assert lowestCommonAncestor(treeNodeRoot, 7, 3) == 3  # 7
    assert lowestCommonAncestor(treeNodeRoot, 0, 8) == 1  # 8
    assert lowestCommonAncestor(treeNodeRoot, 6, 4) == 5  # 9
    assert lowestCommonAncestor(treeNodeRoot, 5, 4) == 5  # 10

    ##############################################

    # B
    arr = [1, 2]
    treeNodeRoot = buildTreeFromArr(arr)
    assert lowestCommonAncestor(treeNodeRoot, 1, 2) == 1  # 1


