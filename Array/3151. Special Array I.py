# Approach-1 (Simple iteration)
# T.C : O(n) 
# S.C : O(1)

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        n = len(nums)
        
        for i in range(n-1):
            if nums[i]%2 == nums[i+1]%2:
                return False
        return True
    

# Approach-2 (Using Bit magic)
# T.C : O(n) 
# S.C : O(1)

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        n = len(nums)
        
        for i in range(n-1):
            if nums[i]&1 == nums[i+1]&1:
                return False
        return True