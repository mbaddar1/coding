from typing import Iterable

import numpy as np


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def construct_tree(arr: Iterable):
    n = len(arr)
    if n == 0:
        return None
    queue_ = []
    main_root = TreeNode(arr[0])
    queue_.append((main_root, 0))
    while len(queue_) > 0:
        node_, idx = queue_.pop(0)
        l_child_idx = 2 * idx + 1 if (2 * idx + 1 < n) else None
        r_child_idx = 2 * idx + 2 if (2 * idx + 2 < n) else None
        l_child_val = arr[l_child_idx] if l_child_idx is not None else None
        r_child_val = arr[r_child_idx] if r_child_idx is not None else None
        node_.left = TreeNode(l_child_val) if l_child_val is not None else None
        node_.right = TreeNode(r_child_val) if r_child_val is not None else None
        if node_.left is not None:
            queue_.append((node_.left, l_child_idx))
        if node_.right is not None:
            queue_.append((node_.right, r_child_idx))
    return main_root
