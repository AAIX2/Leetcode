# Approach (Using frequency count and Xor Property)
# T.C : O(n)
# S.C : O(1)

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        closestSetBit = [-1]*32
        res = [0]*n
        for i in range(n-1,-1,-1):
            maxInd = i
            
            for j in range(32):
                if closestSetBit[j]!=-1 and nums[i]&(1<<j) == 0:
                    maxInd = max(maxInd,closestSetBit[j])
                if nums[i]&(1<<j)!=0:
                    closestSetBit[j] = i

            res[i] = maxInd-i+1
        return res

# Approach (Sliding Window)
# T.C : O(n)
# S.C : O(1)

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        suffixOr = [0]*n
        suffixOr[-1] = nums[-1]
        for i in range(n-2,-1,-1):
            suffixOr[i]|=suffixOr[i+1]|(nums[i])

        bitArr = [0]*32
        def removeorAddContri(num,type):
            if type == 0:
                for i in range(32):
                    if num&(1<<i)!=0:
                        bitArr[i]-=1
            else:
                for i in range(32):
                    if num&(1<<i)!=0:
                        bitArr[i]+=1
        def newOr(arr):
            res = 0
            for i in range(32):
                if bitArr[i]>0:
                    res+=2**i
            return res
        
        i = j = 0
        curOr = 0
        ans = [0]*n
        while j<n:
            curOr|=nums[j]
            removeorAddContri(nums[j],1)
            while i<=j and curOr == suffixOr[i]:
                ans[i] = j-i+1
                removeorAddContri(nums[i],0)
                curOr = newOr(bitArr)
                i+=1
            
            j+=1
        return ans


        
        