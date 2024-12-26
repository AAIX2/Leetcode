# Approach-1 (Normal Recursion & Memoization using unordered_map)
# T.C : O(n*totalSum)
# S.C : O(n*totalSum)

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = defaultdict(int)
        def solve(ind,s):
            if ind == n:
                if s == target:
                    return 1
                return 0
            if (ind,s) in dp:
                return dp[(ind,s)]
            add = solve(ind+1,s+nums[ind])
            sub = solve(ind+1,s-nums[ind])
            dp[(ind,s)] = add+sub
            return dp[(ind,s)]
        return solve(0,0)
    

# Approach-2 (Normal Recursion & Memoization using vector)
# T.C : O(n*totalSum)
# S.C : O(n*totalSum)

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        s1 = sum(nums)
        dp = [[float('inf') for i in range(2*s1+1)]for i in range(n)]
        def solve(ind,s):
            if ind == n:
                if s == target:
                    return 1
                return 0
            if dp[ind][s+s1]!= float('inf'):
                return dp[ind][s+s1]
            add = solve(ind+1,s+nums[ind])
            sub = solve(ind+1,s-nums[ind])
            dp[ind][s+s1] = add+sub
            return dp[ind][s+s1]
        return solve(0,0)
    
# Approach-3 (Recursion + Memoization) - Using concept of SubsetSum and Partition Equal Subset Sum
# T.C : O(n*target)
# S.C : O(n*target)

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        s = sum(nums)
        if s-target<0 or (s-target)%2:
            return 0
        tar = (s-target)//2
        dp = [[-1 for i in range(tar+1)]for i in range(n)]
        def solve(ind,t):
            if ind == 0:
                if t == 0 and nums[0] == 0:
                    return 2
                elif t == 0 and nums[0]>0:
                    return 1
                elif t-nums[0] == 0:
                    return 1
                return 0
            if dp[ind][t]!=-1:
                return dp[ind][t]
            pick = 0
            if nums[ind]<=t:
                pick = solve(ind-1,t-nums[ind])
            not_pick = solve(ind-1,t)
            dp[ind][t] = pick+not_pick
            return dp[ind][t]
        return solve(n-1,tar)
    
# Approach-4 (Bottom Up DP) - Using concept of SubsetSum and Partition Equal Subset Sum
# T.C : O(n*target)
# S.C : O(n*target)


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        s = sum(nums)
        if s-target<0 or (s-target)%2:
            return 0
        tar = (s-target)//2
        dp = [[0 for i in range(tar+1)]for i in range(n)]
        if nums[0] == 0:
            dp[0][0] = 2
        else:
            dp[0][0] = 1
        if nums[0]!=0 and nums[0]<=tar:
            dp[0][nums[0]] = 1
        for ind in range(1,n):
            for t in range(tar+1):
                pick = 0
                if nums[ind]<=t:
                    pick = dp[ind-1][t-nums[ind]]
                not_pick = dp[ind-1][t]
                dp[ind][t] = pick+not_pick
        return dp[n-1][tar]
        

# Approach-5 (Bottom Up Space Optimised DP) - Using concept of SubsetSum and Partition Equal Subset Sum
# T.C : O(n*target)
# S.C : O(target)

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        s = sum(nums)
        if s-target<0 or (s-target)%2:
            return 0
        tar = (s-target)//2
        prev = [0 for i in range(tar+1)]
        if nums[0] == 0:
            prev[0] = 2
        else:
            prev[0] = 1
        if nums[0]!=0 and nums[0]<=tar:
            prev[nums[0]] = 1
        for ind in range(1,n):
            cur = [0]*(tar+1)
            for t in range(tar+1):
                pick = 0
                if nums[ind]<=t:
                    pick = prev[t-nums[ind]]
                not_pick = prev[t]
                cur[t] = pick+not_pick
            prev = cur
        return prev[tar]
        

