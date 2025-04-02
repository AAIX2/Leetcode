# Approach-1 (Brute Force - Trying All Possibilities)
# T.C : O(n^3)
# S.C : O(1)

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        maxi = 0
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    maxi = max(maxi,(nums[i] - nums[j]) * nums[k])
        return maxi
    

# Approach-2 (Using suffix Max)
# T.C : O(n^2)
# S.C : O(n)

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        suffixMax = [0]*n
        suffixMax[-1] = nums[-1]
        for i in range(n-2,-1,-1):
            suffixMax[i] = max(suffixMax[i+1],nums[i])
        
        maxi = 0
        for i in range(n-3+1):
            for j in range(i+1,n-2+1):
                maxi = max(maxi,(nums[i] - nums[j]) * suffixMax[j+1])
                    
        return maxi
    

# Approach-3 (Using prefix and suffix storage)
# T.C : O(n)
# S.C : O(n)
class Solution:
    def maximumTripletValue(nums: List[int]) -> int:
        n = len(nums)
        left_max = [0] * n
        right_max = [0] * n

        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], nums[i - 1])
        
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], nums[i + 1])

        result = 0
        for j in range(1, n - 1):
            result = max(result, (left_max[j] - nums[j]) * right_max[j])
        
        return result



# Approach-4 (Keeping track of maxDif and maxi)
# T.C : O(n)
# S.C : O(1)

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        multiMax = 0
        maxi = 0
        diffMax = 0
        maxNum = 0
        for j in range(n):
            maxi = max(maxi,diffMax*nums[j])
            diffMax = max(diffMax,maxNum-nums[j])
            maxNum = max(maxNum,nums[j])
        return maxi
            
        

        
        
        