from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        TC: O(nlogn)
        SC: O(n)
        """
        res = []

        for num in nums:
            l, r = 0, len(res)-1
            while l <= r:
                c = (l+r)//2
                if res[c] < num:
                    l = c+1
                elif res[c] > num:
                    r = c-1
                else:
                    l = c
                    break
            if l >= len(res):
                res.append(num)
            else:
                res[l] = num

        return len(res)