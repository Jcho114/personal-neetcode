from typing import List
from collections import defaultdict, deque
from math import inf

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        TC: O(V + E*K)
        SC: O(V + E*K)
        """
        graph = defaultdict(list)
        for frm, to, price in flights:
            graph[frm].append((to, price))

        cheapest = [inf]*n
        queue = deque([(src, 0)])
        res = inf

        for _ in range(k+1):
            for _ in range(len(queue)):
                node, price = queue.popleft()
                for neighbor, next_price in graph[node]:
                    if neighbor == dst:
                        res = min(res, price+next_price)
                        continue
                    
                    if price+next_price <= cheapest[neighbor]:
                        cheapest[neighbor] = price+next_price
                        queue.append((neighbor, price+next_price))
        
        return res if res != inf else -1