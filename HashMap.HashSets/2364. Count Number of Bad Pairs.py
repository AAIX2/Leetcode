# Approach-1 (Brute Force)
# T.C : O(n^2)
# S.C : O(1)

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0
        for i in range(n):
            for j in range(i+1,n):
                if j-i!=nums[j]-nums[i]:
                    cnt+=1
        return cnt
    



# Approach-2 (Using hashmap)
# T.C : O(n)
# S.C : O(n)

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0
        mp = defaultdict(int)
        total = 0
        for i in range(n):
            if i-nums[i] in mp:
                cnt+=(total-mp[i-nums[i]])
            else:
                cnt+=total
            
            mp[i-nums[i]]+=1
            total+=1
        return cnt
    


