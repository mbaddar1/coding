# TODO add more test cases (edge and complex ones)
"""
https://www.facebookrecruiting.com/portal/coding_practice_question/?problem_id=495004218121393&c=282010630480533&ppid=454615229006519&practice_plan=0
Number of Visible Nodes
There is a binary tree with N nodes. You are viewing the tree from its left side and can see only the leftmost nodes at each level. Return the number of visible nodes.
Note: You can see only the leftmost nodes, but that doesn't mean they have to be left nodes. The leftmost node at a level could be a right node.
Signature
int visibleNodes(Node root) {
Input
The root node of a tree, where the number of nodes is between 1 and 1000, and the value of each node is between 0 and 1,000,000,000
Output
An int representing the number of visible nodes.
Example
            8  <------ root
           / \
         3    10
        / \     \
       1   6     14
          / \    /
         4   7  13
output = 4
"""


# Add any extra import statements you may need here


class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    # Add any helper functions you may need here


def max_child_depth(root, curr_depth):
    max_depth_left = curr_depth
    max_depth_right = curr_depth
    if root.left is not None:
        max_depth_left = max_child_depth(root.left, curr_depth + 1)
    if root.right is not None:
        max_depth_right = max_child_depth(root.right, curr_depth + 1)
    return max(max_depth_right, max_depth_left)


def visible_nodes(root):
    depth = 1
    max_depth = depth
    if root.left is not None:
        max_left_depth = max_child_depth(root.left, depth+1)
        max_depth = max(max_depth, max_left_depth)
    if root.right is not None:
        max_right_depth = max_child_depth(root.right, depth+1)
        max_depth = max(max_depth, max_right_depth)
    return max_depth

    pass


# Write your code here


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
    print('[', n, ']', sep='', end='')


test_case_number = 1


def check(expected, output):
    global test_case_number
    result = False
    if expected == output:
        result = True
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, 'Test #', test_case_number, sep='')
    else:
        print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
        printInteger(expected)
        print(' Your output: ', end='')
        printInteger(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    root_1 = TreeNode(8)
    root_1.left = TreeNode(3)
    root_1.right = TreeNode(10)
    root_1.left.left = TreeNode(1)
    root_1.left.right = TreeNode(6)
    root_1.left.right.left = TreeNode(4)
    root_1.left.right.right = TreeNode(7)
    root_1.right.right = TreeNode(14)
    root_1.right.right.left = TreeNode(13)
    expected_1 = 4
    output_1 = visible_nodes(root_1)
    check(expected_1, output_1)

    root_2 = TreeNode(10)
    root_2.left = TreeNode(8)
    root_2.right = TreeNode(15)
    root_2.left.left = TreeNode(4)
    root_2.left.left.right = TreeNode(5)
    root_2.left.left.right.right = TreeNode(6)
    root_2.right.left = TreeNode(14)
    root_2.right.right = TreeNode(16)

    expected_2 = 5
    output_2 = visible_nodes(root_2)
    check(expected_2, output_2)

    # Add your own test cases here
