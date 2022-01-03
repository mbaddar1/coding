"""
https://leetcode.com/explore/interview/card/facebook/6/linked-list/319/
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.



Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print(self):
        pointer = self
        l = []
        while pointer is not None:
            l.append(str(pointer.val))
            pointer = pointer.next
        print(",".join(l))


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        r1 = l1
        r2 = l2
        carry = 0
        res_list = res_list_runner = None

        while r1 is not None or r2 is not None:
            r1_val = r1.val if r1 is not None else 0
            r2_val = r2.val if r2 is not None else 0
            res_val = carry + r1_val + r2_val
            if res_val >= 10:
                carry = 1
                res_val = res_val - 10
            else:
                carry = 0
            if res_list is None:
                res_list = ListNode(res_val)
                res_list_runner = res_list
            else:
                res_list_runner.next = ListNode(res_val)
                res_list_runner = res_list_runner.next
            r1 = r1.next if r1 is not None else r1
            r2 = r2.next if r2 is not None else r2
        if carry == 1:  # TODO very good edge case
            res_list_runner.next = ListNode(1)
        return res_list


if __name__ == '__main__':

    # case 1
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    sol = Solution()
    r = sol.addTwoNumbers(l1, l2)
    r.print()
    # case 2
    l1 = ListNode(0)
    l2 = ListNode(1)
    r = sol.addTwoNumbers(l1, l2)
    r.print()

    # case 3
    l1 = ListNode(1)
    l2 = ListNode(0)
    r = sol.addTwoNumbers(l1, l2)
    r.print()

    # case 3
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l2 = ListNode(0)
    r = sol.addTwoNumbers(l1, l2)
    r.print()

    # case 4
    l1 = ListNode(9)
    l1runner = l1
    for i in range(6):
        l1runner.next = ListNode(9)
        l1runner = l1runner.next
    l1.print()
    l2 = ListNode(9)
    l2runner = l2
    for i in range(3):
        l2runner.next = ListNode(9)
        l2runner = l2runner.next
    l2.print()

    r = sol.addTwoNumbers(l1, l2)
    r.print()
