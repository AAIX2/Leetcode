# Approach (Sliding Window Khandani Template)
# T.C : O(2*n) ~ O(n)
# S.C : O(1)

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        i = j = 0
        curSum = 0
        cnt = 0
        while j<n:
            curSum+=nums[j]
            while i<=j and curSum*(j-i+1)>=k:
                curSum-=nums[i]
                i+=1
            cnt+=(j-i+1)
            j+=1
        return cnt