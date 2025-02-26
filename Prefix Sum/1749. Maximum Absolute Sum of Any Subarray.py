# Approach-1 (2 Pass - Kadane's Algorithm for maxsubarrysum and minsybarraysum)
# T.C : O(2*n) ~= O(n)
# S.C : O(1)

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        n = len(nums)
        maxSubSum = 0
        minSubSum = 0
        curSubMax = 0
        curSubMin = 0
        for num in nums:
            curSubMax = max(num,curSubMax+num)
            maxSubSum = max(maxSubSum,curSubMax)
            curSubMin = min(num,curSubMin+num)
            minSubSum = min(minSubSum,curSubMin)
        return max(maxSubSum,abs(minSubSum))
        
# Approach-2 (prefixSum)
# T.C : O(n)
# S.C : O(1)

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        n = len(nums)
        maxSum = 0
        sum = 0
        maxPos = 0
        minNeg = 0
        for num in nums:
            sum+=num
            if sum>0:
                maxSum = max(maxSum,abs(sum-minNeg))
                maxPos = max(maxPos,sum)
            elif sum<0:
                maxSum = max(maxSum,abs(sum-maxPos))
                minNeg = min(minNeg,sum)
            else:
                maxSum = max(maxSum,max(maxPos,abs(minNeg)))
        return maxSum
        
# Approach-3 (prefixSum)
# T.C : O(n)
# S.C : O(1)

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        n = len(nums)
        maxSum = 0
        minSum = 0
        sum = 0
        for num in nums:
            sum+=num
            maxSum = max(maxSum,sum)
            minSum = min(minSum,sum)
        return abs(maxSum-minSum)
        