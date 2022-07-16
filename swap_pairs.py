# https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        superhead = ListNode(0, next=head)
        root = None
        while superhead.next is not None and superhead.next.next is not None:
            n1 = superhead.next
            n2 = superhead.next.next
            n1.next = n2.next
            n2.next = n1
            superhead.next = n2
            # advance
            superhead = n1
            if root is None:
                root = n2
        if root is None and head is not None:
            root = head
        return root


def create_linked_list(l):
    root = None
    curr = root
    for e in l:
        if curr is None:
            curr = ListNode(e)
            root = curr
        else:
            curr.next = ListNode(e)
            curr = curr.next
    return root


def printLL(root):
    curr = root
    while curr is not None:
        print(curr.val)
        curr = curr.next


if __name__ == '__main__':
    l = [1, 2, 3, 4]
    ll = create_linked_list(l)
    printLL(ll)
    s = Solution()
    sll = s.swapPairs(ll)
    printLL(sll)
    print('------')
    l = [1]
    ll = create_linked_list(l)
    printLL(ll)
    s = Solution()
    sll = s.swapPairs(ll)
    printLL(sll)

