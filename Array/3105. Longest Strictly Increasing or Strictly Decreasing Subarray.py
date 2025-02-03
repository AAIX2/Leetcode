# Approach-1 : Brute Force
# T.C : O(n^2)
# S.C : O(1)    


class Solution:
    def longestMonotonicSubarray(self, nums):
        n = len(nums)
        result = 0
        
        for i in range(n):
            increasing = 1
            j = i + 1
            while j < n and nums[j] > nums[j - 1]:
                increasing += 1
                j += 1
                
            decreasing = 1
            j = i + 1
            while j < n and nums[j] < nums[j - 1]:
                decreasing += 1
                j += 1
                
            result = max(result, increasing, decreasing)
        
        return result
    

# Approach-2 : Optimal
# T.C : O(n)
# S.C : O(1)

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        incLen = 1
        decLen = 1
        maxInc = 1
        maxDec = 1
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                incLen+=1
            else:
                incLen = 1
            if nums[i]<nums[i-1]:
                decLen+=1
            else:
                decLen = 1
            maxDec= max(maxDec,incLen)
            maxInc = max(maxInc,decLen)
        return max(maxDec,maxInc)