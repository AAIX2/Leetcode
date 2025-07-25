# Approach-1 (Using set)
# T.C : O(n)
# S.C : O(n)

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        n = len(nums)
        seen = set()
        maxi = 0
        curSum = 0
        for i in range(n):
            if nums[i] in seen or nums[i]<=0:
                continue
            curSum+=nums[i]
            seen.add(nums[i])
        return curSum if curSum>0 else max(nums)