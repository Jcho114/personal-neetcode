from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        TC: O(n)
        SC: O(1)
        """
        dummy = ListNode()
        build = dummy
        curr1, curr2 = list1, list2

        while curr1 and curr2:
            if curr1.val < curr2.val:
                build.next = curr1
                curr1 = curr1.next
            else:
                build.next = curr2
                curr2 = curr2.next
            build = build.next
        
        while curr1:
            build.next = curr1
            build = build.next
            curr1 = curr1.next

        while curr2:
            build.next = curr2
            build = build.next
            curr2 = curr2.next
        
        return dummy.next