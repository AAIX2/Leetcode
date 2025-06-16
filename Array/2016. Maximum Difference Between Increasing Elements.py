# Approach suffix max or prefix min
# T.C : O(n)
# S.C : O(1)
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        res = -1
        maxi = -1
        for i in range(n-1,-1,-1):
            if nums[i]>=maxi:
                maxi = nums[i]
            else:
                res = max(res,maxi-nums[i])
        return res
