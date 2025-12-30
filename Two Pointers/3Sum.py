from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        TC: O(n^2)
        SC: O(n)
        """
        nums.sort()

        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                return res

            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i+1, len(nums)-1
            target = -nums[i]
            while l < r:
                sm = nums[l] + nums[r]
                if sm < target:
                    l += 1
                elif sm > target:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    r -= 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1

        return res