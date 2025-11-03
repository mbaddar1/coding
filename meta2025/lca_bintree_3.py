# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Done : Accepted
#       https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/submissions/1819602258
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


################ Tree Building Code #########################################
# COde copied from utils.py
def dfs(rootNode: Node):
    print(rootNode.val)
    if rootNode.left is not None:
        # print(rootNode.left.val)
        dfs(rootNode.left)
    if rootNode.right is not None:
        # print(rootNode.right.val)
        dfs(rootNode.right)


def __build_tree_aux(a: list[int], i: int, rootNode: Node, tree_dict: dict):
    # fill wih value at i
    tree_dict[rootNode.val] = rootNode
    rootNode.val = a[i]  # this step is redundant
    left_child_idx = 2 * i + 1
    if left_child_idx < len(a) and a[left_child_idx] is not None:
        left_child_node = Node(val=a[left_child_idx])  # this is the main step where value is written
        left_child_node.parent = rootNode
        rootNode.left = left_child_node
        __build_tree_aux(a, left_child_idx, left_child_node, tree_dict)

    right_child_idx = 2 * i + 2
    if right_child_idx < len(a) and a[right_child_idx] is not None:
        right_child_node = Node(val=a[right_child_idx])
        right_child_node.parent = rootNode
        rootNode.right = right_child_node
        __build_tree_aux(a, right_child_idx, right_child_node, tree_dict)


def build_tree(a: List[int], tree_dict: dict):
    rootNode = Node(val=a[0])
    __build_tree_aux(a, 0, rootNode, tree_dict)
    return rootNode


############################################################################################
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        finished = False
        assert p!=q
        assert p.val!=q.val
        p_path_set = {p.val}  # assume set is a hashmap without k,v just k
        q_path_set = {q.val}
        while not finished:
            # get p parent
            if p.parent == q.parent:
                if p.parent is not None:
                    return p.parent
                else:
                    raise ValueError("p and q must have same parent")

            if p.parent is not None and p.parent.val in q_path_set:
                return p.parent
            if p.parent is not None:
                p_path_set.add(p.parent.val)
            if p.parent is not None:
                p = p.parent
            if q.parent is not None and q.parent.val in p_path_set:
                return q.parent
            if q.parent is not None:
                q_path_set.add(q.parent.val)
            if q.parent is not None:
                q = q.parent
        raise ValueError("Something went wrong")



if __name__ == "__main__":

    a = [1,2,3,None,4]
    tree_dict = dict()
    tree = build_tree(a, tree_dict)
    p = tree_dict[4]
    q = tree_dict[1]
    s = Solution()
    s.lowestCommonAncestor(p,q)
    #
    #
    # a = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    #
    # p = tree_dict[6]
    # q = tree_dict[4]
    # s = Solution()
    # r = s.lowestCommonAncestor(p=p, q=q)
    # assert r.val == 5
    # p = tree_dict[4]
    # q = tree_dict[8]
    # r = s.lowestCommonAncestor(p=p, q=q)
    # assert r.val == 3
