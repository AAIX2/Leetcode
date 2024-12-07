# Approach (Using Binary Search in Answer - See the problem statement : It asks to Minimize the Maximum which hints towards Binary Search On Answer)
# T.C : O(nlog(MAX)), where n = length of nums, MAX = max value in nums
# S.C : O(1)

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def isPossible(mid):
            op = 0
            for i in range(len(nums)):
                op1 = ceil(nums[i]/mid)-1 
                if op+op1>maxOperations:
                    return False
                op+=op1
            return True
        low = 1
        high = max(nums)
        while low<=high:
            mid = (low+high)//2
            if isPossible(mid):
                high = mid-1
            else:
                low = mid+1
        return low