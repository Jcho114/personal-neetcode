from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        TC: O(n)
        SC: O(n)
        """
        c = s = 0
        dummy = ListNode()
        curr = dummy

        while l1 and l2:
            s = (l1.val + l2.val + c) % 10
            c = (l1.val + l2.val + c) // 10
            curr.next = ListNode(s)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            s = (l1.val + c) % 10
            c = (l1.val + c) // 10
            curr.next = ListNode(s)
            curr = curr.next
            l1 = l1.next
                    
        while l2:
            s = (l2.val + c) % 10
            c = (l2.val + c) // 10
            curr.next = ListNode(s)
            curr = curr.next
            l2 = l2.next
        
        if c > 0:
            curr.next = ListNode(c)
            curr = curr.next
        
        return dummy.next