# https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import List, Optional


class Solution:
    def merge_two_lists(self, l1: ListNode, l2: ListNode):
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        runner1 = l1
        runner2 = l2
        runner1_prev = ListNode(next=runner1)
        runner2_prev = ListNode(next=runner2)
        if runner1.val < runner2.val:
            root = runner1
        else:
            root = runner2
        while runner1 is not None and runner2 is not None:
            if runner1.val < runner2.val:
                if runner1.next is not None and runner2.val < runner1.next.val:
                    tmp = runner1.next
                    runner1.next = runner2
                    runner1 = tmp
                else:  # runner2.val >= runner1.next.val
                    runner1_prev = runner1
                    runner1 = runner1.next
            else:  # runner1.val >= runner2.val
                if runner2.next is not None and runner1.val < runner2.next.val:
                    tmp = runner2.next
                    runner2.next = runner1
                    runner2 = tmp
                else:  # runner1.val >= runner2.nex.val
                    runner2_prev = runner2
                    runner2 = runner2.next

        if runner1 is None:
            runner1_prev.next = runner2
        if runner2 is None:
            runner2_prev.next = runner1
        return root

    def printList(self, l: ListNode):
        s = []
        while l is not None:
            s.append(l.val)
            l = l.next
        print(','.join(list(map(str, s))))

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l = None
        for u in lists:
            l = self.merge_two_lists(u, l)
            self.printList(l)
        return l

    def makeList(self, l: List) -> [ListNode, None]:
        if not l:
            return None
        root = ListNode(val=l[0])
        runner = root
        n = len(l)
        for i in range(1, n):
            node = ListNode(l[i])
            runner.next = node
            runner = runner.next
        return root


if __name__ == '__main__':
    s = Solution()
    l = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    l_ = []
    for u in l:
        u_ = s.makeList(u)
        l_.append(u_)

    # l1 = s.makeList(l[0])
    # s.printList(l1)
    # l2 = s.makeList(l[1])
    # s.printList(l2)
    r = s.mergeKLists(l_)
    s.printList(r)
