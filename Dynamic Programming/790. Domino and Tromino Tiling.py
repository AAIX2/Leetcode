
# Approach-1 (Recur + Memo)(More Intutive)
# T.C : O(n)
# S.C : O(n)

class Solution:
    def numTilings(self, n: int) -> int:
        mod = 10**9+7
        dp = [[-1 for i in range(2)]for i in range(n)]
        def solve(ind,prevGap):
            if ind>n:
                return 0
            if ind == n:
                if prevGap == False:
                    return 1
                return 0
            if dp[ind][prevGap]!=-1:
                return dp[ind][prevGap]
            if prevGap == True:
                dp[ind][prevGap] = solve(ind+1,False)+solve(ind+1,True)
                return dp[ind][prevGap]
            dp[ind][prevGap] = solve(ind+1,False)+solve(ind+2,False)+2*solve(ind+2,True)
            return dp[ind][prevGap]
        return solve(0,False)%mod
        
            

# Approach-2 (Recur + Memo + pattern and maths)
# T.C : O(n)
# S.C : O(n)

class Solution:
    def __init__(self):
        self.M = 10**9 + 7
        self.t = [-1] * 1001

    def solve(self, n):
        if n == 1 or n == 2:
            return n
        if n == 3:
            return 5
        if self.t[n] != -1:
            return self.t[n]
        
        self.t[n] = (2 * self.solve(n - 1) % self.M + self.solve(n - 3) % self.M) % self.M
        return self.t[n]

    def numTilings(self, n):
        return self.solve(n)
    

# Approach-3 (Bottom Up)
# T.C : O(n)
# S.C : O(n)

class Solution:
    def numTilings(self, n: int) -> int:
        mod = 10**9+7
        dp = [0 for i in range(n+1)]
        dp[0] = 1
        dp[1] = 1
        if n>=2:
            dp[2] = 2
        for i in range(3,n+1):
            dp[i] = 2*dp[i-1]+dp[i-3]
        return dp[n]%mod