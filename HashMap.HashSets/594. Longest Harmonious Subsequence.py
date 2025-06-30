# Approach-1 (Using sorting and sliding Window)
# T.C : O(nlogn)
# S.C : O(n)

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        i = j = 0
        maxLen = 0
        while j<n:
            while i<=j and nums[j]-nums[i]>1:
                i+=1
            if nums[j]-nums[i] == 1:
                maxLen = max(maxLen,j-i+1)
            j+=1
        return maxLen
    

# Approach-2 (Using map and counting)
# T.C : O(n)
# S.C : O(n)

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        n = len(nums)
        freq = Counter(nums)
        maxLen = 0
        for i in range(n):
            if nums[i]+1 in freq:
                maxLen = max(maxLen,freq[nums[i]]+freq[nums[i]+1])
        return maxLen