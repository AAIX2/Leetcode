# Approach-1 (Top Down Dp)
# T.C : O(n*m+w*m)
# S.C : O(w*26+n*m)

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        n = len(target)
        m = len(words[0])
        mp = [[0]*26 for i in range(m)]
        for w in words:
            for i,ch in enumerate(w):
                mp[i][ord(ch)-ord('a')]+=1
        dp = [[-1 for i in range(m)]for i in range(n)]
        mod = 10**9+7
        def solve(ind,ind1):
            if ind == n:
                return 1
            if ind1 == m:
                return 0    
            if dp[ind][ind1]!=-1:
                return dp[ind][ind1]
            ch = ord(target[ind])-ord('a')
            pick = 0
            if mp[ind1][ch]>0:
                pick = mp[ind1][ch]*solve(ind+1,ind1+1)
            not_pick = solve(ind,ind1+1)
            dp[ind][ind1] = pick+not_pick
            return dp[ind][ind1]
        return solve(0,0)%mod
    

# Approach-2 (Bottom Up Dp)
# T.C : O(n*m+w*m)
# S.C : O(w*26+n*m)

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        n = len(target)
        m = len(words[0])
        mp = [[0]*26 for i in range(m)]
        for w in words:
            for i,ch in enumerate(w):
                mp[i][ord(ch)-ord('a')]+=1
        dp = [[0 for i in range(m+1)]for i in range(n+1)]
        mod = 10**9+7
        for i in range(m+1):
            dp[n][i] = 1
        for ind in range(n-1,-1,-1):
            for ind1 in range(m-1,-1,-1):
                ch = ord(target[ind])-ord('a')
                pick = 0
                if mp[ind1][ch]>0:
                    pick = mp[ind1][ch]*dp[ind+1][ind1+1]
                not_pick = dp[ind][ind1+1]
                dp[ind][ind1] = pick+not_pick
        return dp[0][0]%mod
        

# Approach-3 (Space Optimised Dp)
# T.C : O(n*m+w*m)
# S.C : O(w*26+m)

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        n = len(target)
        m = len(words[0])
        mp = [[0]*26 for i in range(m)]
        for w in words:
            for i,ch in enumerate(w):
                mp[i][ord(ch)-ord('a')]+=1
        next = [1 for i in range(m+1)]
        mod = 10**9+7
        for ind in range(n-1,-1,-1):
            cur = [0]*(m+1)
            for ind1 in range(m-1,-1,-1):
                ch = ord(target[ind])-ord('a')
                pick = 0
                if mp[ind1][ch]>0:
                    pick = mp[ind1][ch]*next[ind1+1]
                not_pick = cur[ind1+1]
                cur[ind1] = pick+not_pick
            next = cur
        return next[0]%mod


# Approach-4 (Using only one arr)
# T.C : O(n*m+w*m)
# S.C : O(w*26+m)

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        n = len(target)
        m = len(words[0])
        mp = [[0]*26 for i in range(m)]
        for w in words:
            for i,ch in enumerate(w):
                mp[i][ord(ch)-ord('a')]+=1
        dp = [1 for i in range(m+1)]
        mod = 10**9+7
        for ind in range(n-1,-1,-1):
            next1 = dp[m]
            dp[m] = 0
            for ind1 in range(m-1,-1,-1):
                ch = ord(target[ind])-ord('a')
                pick = 0
                next = dp[ind1]
                if mp[ind1][ch]>0:
                    pick = mp[ind1][ch]*next1
                not_pick = dp[ind1+1]
                dp[ind1] = pick+not_pick
                next1 = next         
        return dp[0]%mod
        