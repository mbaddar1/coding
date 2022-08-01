# https://leetcode.com/problems/reverse-nodes-in-k-group/
from typing import Optional

from list_utils import ListNode, makeList, printList


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        k_arr = [ListNode() for i in range(k)]
        runner1 = head
        block_leaf = None
        while runner1 is not None:
            runner2 = runner1
            k_idx = 0
            while k_idx < k and runner2 is not None:
                k_arr[k_idx] = runner2
                runner2 = runner2.next
                k_idx += 1

            if k_idx == k:  # complete block
                runner1 = k_arr[k - 1].next
                k_arr[0].next = runner1
                for j in range(k - 1, 0, -1):
                    k_arr[j].next = k_arr[j - 1]

                if block_leaf is None:
                    head = k_arr[k - 1]
                    block_leaf = k_arr[0]
                else:
                    block_leaf.next = k_arr[k - 1]
                    block_leaf = k_arr[0]

            else:
                runner1 = runner2

        return head


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5]
    l_ = makeList(l)
    printList(l_)
    s = Solution()
    lr = s.reverseKGroup(l_, 2)
    printList(lr)

    #############

    l = [1, 2, 3, 4, 5]
    l_ = makeList(l)
    lr = s.reverseKGroup(l_,3)
    printList(lr)
