from typing import List, Optional
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, head in enumerate(lists):
            if not head:
                continue
            heapq.heappush(heap, (head.val, i, head))
        
        dummy = ListNode()
        curr = dummy
        while heap:
            _, i, head = heapq.heappop(heap)
            curr.next = head
            curr = curr.next
            if head.next:
                heapq.heappush(heap, (head.next.val, i, head.next))

        return dummy.next