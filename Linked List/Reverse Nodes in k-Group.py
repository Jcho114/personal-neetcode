from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        TC: O(n)
        SC: O(1)
        """
        def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
            if not head:
                return None

            curr, prev = head, None
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            return prev

        dummy = ListNode()
        prev_group_tail = dummy
        curr = head

        while curr:
            next_group_tail = curr
            for _ in range(k-1):
                if not curr.next:
                    prev_group_tail.next = next_group_tail
                    return dummy.next # if too short return head
                curr = curr.next

            temp = curr.next
            curr.next = None
            group_head = reverse(next_group_tail)
            prev_group_tail.next = group_head
            prev_group_tail = next_group_tail
            curr = temp

        return dummy.next