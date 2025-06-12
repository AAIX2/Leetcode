# Approach - simple iteration
# T.C : O(n) 
# S.C : O(1)


class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)
        maxi = 0
        for i in range(n):
            maxi = max(maxi,abs(nums[i]-nums[(i+1)%n]))
        return maxi