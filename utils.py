import logging
from typing import List


class MyAssert:
    def __init__(self):
        self.assertion_count = 1
        self.logger = logging.getLogger(self.__class__.__name__)

    def assert_scalar(self, actual, expected):
        assert abs(actual - expected) < 1e-5, f"actual = {actual} != expected = {expected}"
        self.logger.info(f'Test # {self.assertion_count} passed!')
        self.assertion_count += 1

    def asser_in_list(self, actual, expected_list):
        assert actual in expected_list, f"actual = {actual} not in  {expected_list}"
        self.logger.info(f'Test # {self.assertion_count} passed!')
        self.assertion_count += 1


# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


def dfs(rootNode:Node):
    print(rootNode.val)
    if rootNode.left is not None:
        #print(rootNode.left.val)
        dfs(rootNode.left)
    if rootNode.right is not None:
        # print(rootNode.right.val)
        dfs(rootNode.right)

def __build_tree_aux(a:list[int],i:int,rootNode:Node):
    # fill wih value at i
    rootNode.val = a[i] # this step is redundant
    left_child_idx = 2*i+1
    if left_child_idx < len(a) and a[left_child_idx] is not None :
        left_child_node = Node(val=a[left_child_idx]) # this is the main step where value is written
        rootNode.left = left_child_node
        __build_tree_aux(a,left_child_idx,left_child_node)

    right_child_idx = 2*i+2
    if right_child_idx < len(a) and a[right_child_idx] is not None :
        right_child_node = Node(val=a[right_child_idx])
        rootNode.right = right_child_node
        __build_tree_aux(a,right_child_idx,right_child_node)

def build_tree(a:List[int]):
    rootNode = Node(val=a[0])
    __build_tree_aux(a,0,rootNode)
    return rootNode

if __name__=="__main__":
    arr = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    rootNode = build_tree(arr)
    dfs(rootNode)

