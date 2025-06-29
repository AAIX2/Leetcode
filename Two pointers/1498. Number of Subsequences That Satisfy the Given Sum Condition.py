# Approach-1 (Produce all subsequences, find min and max and check)
# This will give TLE

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        mod = 10**9+7
        nums.sort()
        res = 0
        for i in range(n):
            mini = float('inf')
            maxi = float('-inf')
            for j in range(i,n):
                maxi = max(maxi,nums[j])
                mini = min(mini,nums[j])
                if maxi+mini<=target:
                    if j-i <= 1:
                        res+=1
                    else:
                        res+=2**(j-i-1)
                    
                else:
                    break
                
        return res%mod
    

# Approach-2 (Using Sorting + Two Pointer Approach)
# T.C : O(nlogn)
# S.C : O(n)


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        mod = 10**9+7
        powerOf2 = [1]*(n+1)
        mul = 1
        for i in range(1,n+1):
            mul*=2
            powerOf2[i] = mul%mod
        nums.sort()
        res = 0
        i = 0
        j = n-1
        while i<=j:
            if nums[i]+nums[j]>target:
                j-=1
            else:
                res+=powerOf2[j-i]
                i+=1
        return res%mod