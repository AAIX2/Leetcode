# Approach (observing the condition and checking, oddCount, evenCount and alternatingCount
# T.C : O(n)
# S.C : O(1)
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        even,odd = 0,0
        oddSt = -1
        oddStLen = 0
        evenSt = -1
        evenStLen = 0
        for i,num in enumerate(nums):
            if num%2 == 0:
                even+=1
                if evenSt == -1 or evenSt%2 == 1:
                    evenSt = nums[i]
                    evenStLen+=1
                if oddSt!=-1 and oddSt%2 == 1:
                    oddSt = nums[i]
                    oddStLen += 1

            else:
                odd+=1
                if oddSt == -1 or oddSt%2 == 0:
                    oddSt = nums[i]
                    oddStLen += 1
                if evenSt!=-1 and evenSt%2 == 0:
                    evenSt = nums[i]
                    evenStLen+=1
                
                
        return max(even,odd,evenStLen,oddStLen)            
        