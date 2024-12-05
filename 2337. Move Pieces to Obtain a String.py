# Approach-1 (Brute Force to check all possibilities)
# T.C : Exponential in the worst case due to exploring all possible swaps, though memoization reduces redundant computations.
# S.C : Memoization map to store all possible states. ~ O(n^2) states possible
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        dp = defaultdict()
        def solve(s):
            st = "".join(s)
            if st == target:
                return True
            
            if st in dp:
                return dp[st]
            for i in range(n):
                if i>0 and s[i] == "L" and s[i-1] == "_":
                    s[i],s[i-1] = s[i-1],s[i]
                    if solve(s) == True:
                        dp[st] = True
                        return dp[st]
                    s[i],s[i-1] = s[i-1],s[i]
                elif i<n-1 and s[i] == "R" and s[i+1] == "_":
                    s[i],s[i+1] = s[i+1],s[i]
                    if solve(s) == True:
                        dp[st] = True
                        return dp[st]
                    s[i],s[i+1] = s[i+1],s[i]
            dp[st] = False
            return dp[st]
        s = list(start)
        return solve(s)
    
# Approach-2 (Optimal using 2 pointers)
# T.C : O(n)
# S.C : O(1)
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        

        i = j = 0
        while i<n or j<n:
            while i<n and start[i] == "_":
                i+=1
            while j<n and target[j] == "_":
                j+=1
            if i == n or j == n :
                return i == n and j == n
            if start[i]!=target[j] or (start[i] == "L" and j>i) or (start[i] == "R" and j<i):
                return False
            j+=1
            i+=1
        return True    
            
        
                
                


                
        
                
                

