from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        TC: O(n)
        SC: O(1)
        """
        counts = [0]*26
        for task in tasks:
            counts[ord(task) - ord('A')] += 1

        counts.sort()
        chunk = counts[25]-1
        idle = chunk*n

        for i in range(24, -1, -1):
            idle -= min(counts[i], chunk)

        return len(tasks)+idle if idle >= 0 else len(tasks)