# Approach-1 (Top Down Dp)
# T.C : O(n**2*l)
# S.C : O(n**2)

class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        
        n = len(words)

        def hammingDist(w1,w2):
            i = j = 0
            cnt = 0
            while i<len(w1) and j<len(w2):
                cnt+=1 if w1[i]!=w2[j] else 0
                i+=1
                j+=1
            
            return cnt

        dp = [[-1 for i in range(n+1)]for i in range(n)]
        def solve(ind,prev):
            if ind == n:
                return []
            if dp[ind][prev+1]!=-1:
                return dp[ind][prev+1]
            take = []
            if (prev == -1) or (len(words[ind]) == len(words[prev]) and hammingDist(words[ind],words[prev]) == 1 and groups[ind]!=groups[prev]):
                take = [words[ind]]+solve(ind+1,ind)
            not_take = solve(ind+1,prev)
            if len(take)>len(not_take):
                dp[ind][prev+1] = take
                return dp[ind][prev+1]
            dp[ind][prev+1] = not_take
            return dp[ind][prev+1]
        return solve(0,-1)
        
        


# Approach -  Using LIS Pattern
# T.C : (n^2 * L), where L = max length of a string in the words
# S.C : O(n)


class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        parent = [-1]*n
        def hammingDist(w1,w2):
            i = j = 0
            cnt = 0
            while i<len(w1) and j<len(w2):
                cnt+=(1 if w1[i]!=w2[j] else 0)
                i+=1
                j+=1
            return cnt

        maxi = 1
        res = [words[0]]
        dp = [1 for i in range(n)]
        
        for i in range(1,n):
            for j in range(i):
                if groups[i]!=groups[j] and len(words[i]) == len(words[j]) and hammingDist(words[i],words[j]) == 1:
                    if dp[j]+1>dp[i]:
                        dp[i] = dp[j]+1
                        parent[i] = j
                        
            
            if dp[i]>maxi:
                maxi = dp[i]
        res = []
        for i in range(n):
            if maxi == dp[i]:
                while i!=-1:
                    res = [words[i]]+res
                    i = parent[i]
                break
        return res

        

