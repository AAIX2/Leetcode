# Approach (Recursion + Memoization)
# T.C : O(n * S * S * m), where S = total states i.e. 3 * 2^m-1
# S.C : O((n * S) + (S * m)) where n * S is because of memoization array t, and S * m is for storing columnStates

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        col = []
        mod = 10**9+7
        def generateComb(ind,prev,pat):
            if ind == m:
                col.append(pat)
                return 
            for i in "RGB":
                if i != prev:
                    generateComb(ind+1,i,pat+i)
        generateComb(0,"","")


        def isPossible(c1,c2):
            for i in range(len(c1)):
                if c1[i] == c2[i]:
                    return False
            return True



        mp = defaultdict(list)
        for i in range(len(col)):
            for j in range(i+1,len(col)):
                if i == j:
                    continue
                if isPossible(col[i],col[j]):
                    mp[i].append(j)
                    mp[j].append(i)
        
        dp = [[-1 for i in range(n)]for i in range(len(col))]
        def solve(prevInd,rem):
            if rem == 0:
                return 1
            if dp[prevInd][rem]!=-1:
                return dp[prevInd][rem]
            prev = col[prevInd]
            res = 0
            for i in mp[prevInd]:
                res = (res+solve(i,rem-1))%mod
            dp[prevInd][rem] = res
            return dp[prevInd][rem]
        cnt = 0
        for i in range(len(col)):
            cnt = (cnt+solve(i,n-1))%mod
        return cnt%mod