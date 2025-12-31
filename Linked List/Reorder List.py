from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        TC: O(n)
        SC: O(1)
        """
        if not head or not head.next:
            return

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        head1, head2 = head, slow.next
        slow.next = None

        curr, prev = head2, None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        head2 = prev

        dummy = ListNode()
        build = dummy

        curr1, curr2 = head1, head2
        while curr1 and curr2:
            build.next = curr1
            curr1 = curr1.next
            build.next.next = curr2
            curr2 = curr2.next
            build = build.next.next
        
        while curr1:
            build.next = curr1
            curr1 = curr1.next
            build = build.next

        head = dummy.next