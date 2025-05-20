# Approach - Straight Forward Difference Array Technique
# T.C : O(Q + n)
# S.C : O(Q + n)

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diffArr = [0]*n
        for i,j in queries:
            diffArr[i]+=1
            if j+1<n:
                diffArr[j+1]-=1
        curSum = 0
        for i in range(n):
            curSum+=diffArr[i]
            if curSum<nums[i]:
                return False
        return True
        