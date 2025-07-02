# Approach-1 (Recursion + Memoization) - TLE
# T.C : O(n*k*maxFreq), n = total unique characters, maxFreq = maximumFrequency of a character
# S.C : O(n*k)

class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        n = len(word)
        mod = 10**9 + 7
        if k>n:
            return 0
        freq = []
        cnt = 1
        prod = 1
        for i in range(1,n):
            if word[i] != word[i-1]:
                prod = (prod*cnt)%mod
                freq.append(cnt)
                cnt = 1
            else:
                cnt+=1
            
            
        freq.append(cnt)
        prod = (prod*cnt)%mod

        if len(freq)>=k:
            return prod
        
        dp = [[-1 for i in range(n)]for i in range(n)]
        def solve(ind,curLen):
            if ind == len(freq):
                if curLen<k:
                    return 1
                return 0
            if dp[ind][curLen]!=-1:
                return dp[ind][curLen]
            res = 0
            for i in range(1,freq[ind]+1):
                if i+curLen<k:
                    res = (res+solve(ind+1,curLen+i))%mod
                else:
                    break
            dp[ind][curLen] = res
            return dp[ind][curLen]
        
        return (prod-solve(0,0))%mod
    
# Approach-2 (Bottom Up) - TLE
# T.C : O(n*k*maxFreq), n = total unique characters, maxFreq = maximumFrequency of a character
# S.C : O(n*k)

class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        n = len(word)
        mod = 10**9 + 7
        if k>n:
            return 0
        freq = []
        cnt = 1
        prod = 1
        for i in range(1,n):
            if word[i] != word[i-1]:
                prod = (prod*cnt)%mod
                freq.append(cnt)
                cnt = 1
            else:
                cnt+=1
            
            
        freq.append(cnt)
        prod = (prod*cnt)%mod

        if len(freq)>=k:
            return prod
        
        dp = [[0 for i in range(k)]for i in range(len(freq)+1)]
        for i in range(k):
            dp[len(freq)][i] = 1
        for ind in range(len(freq)-1,-1,-1):
            for curLen in range(k-1,-1,-1):
                res = 0
                for i in range(1,freq[ind]+1):
                    if i+curLen<k:
                        res = (res+dp[ind+1][curLen+i])%mod
                    else:
                        break
                dp[ind][curLen] = res
        return (prod-dp[0][0])%mod
       

# Approach-3 (Bottom Up) - Optimized
# T.C : O(n*k)
# S.C : O(n*k)

class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        n = len(word)
        mod = 10**9 + 7
        if k>n:
            return 0
        freq = []
        cnt = 1
        prod = 1
        for i in range(1,n):
            if word[i] != word[i-1]:
                prod = (prod*cnt)%mod
                freq.append(cnt)
                cnt = 1
            else:
                cnt+=1
            
            
        freq.append(cnt)
        prod = (prod*cnt)%mod

        if len(freq)>=k:
            return prod
        
        next = [1 for i in range(k)]
        prefix = [0]*(k+1) #1-based ind
        
        for ind in range(len(freq)-1,-1,-1):
            for i in range(1,k+1):
                prefix[i] = (prefix[i-1]+next[i-1])%mod
            cur = [0]*k
            for curLen in range(k-1,-1,-1):
                res = 0
                l = curLen+1
                r = curLen+freq[ind]
                if r+1>k:
                    r = k-1
                if l<=r:
                    res = (res+prefix[r+1]-prefix[l])%mod
                cur[curLen] = res
            next = cur
        return (prod-next[0])%mod
       