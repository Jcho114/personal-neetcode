from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        TC: O(nmlogm)
        SC: O(nm)
        """
        groups = defaultdict(list)
        for s in strs:
            key = str(sorted(s))
            groups[key].append(s)
        return list(groups.values())