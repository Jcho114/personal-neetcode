from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = scout = head
        prev = None
        for _ in range(n):
            scout = scout.next
        
        while scout:
            scout = scout.next
            prev = curr
            curr = curr.next
        
        if not prev:
            return head.next

        prev.next = curr.next
        return head