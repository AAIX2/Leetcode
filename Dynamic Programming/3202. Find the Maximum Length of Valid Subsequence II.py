# Approach - Using LIS Pattern (Bottom Up)
# T.C : O(n^2)
# S.C : O(n*k)

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[1 for i in range(k)]for i in range(n)]
        maxi = 1
        for i in range(1,n):
            curMax = 0
            for j in range(i):
                mod = (nums[i]+nums[j])%k
                dp[i][mod] = max(dp[i][mod],1+dp[j][mod])
                curMax = max(curMax,dp[i][mod])
            maxi = max(maxi,curMax)
        return maxi

