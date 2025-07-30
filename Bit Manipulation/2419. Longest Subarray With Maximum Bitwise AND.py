# Approach-(Simple Observation of AND property)
# T.C : O(n)
# S.C : O(1)

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        maxi = max(nums)
        cnt = 0
        maxLen = 1
        for i in range(n):
            if nums[i] == maxi:
                cnt+=1
                maxLen = max(maxLen,cnt)
            else:
                cnt = 0
        return maxLen