# Approach-1 (Top Down Dp)
# T.C : O(N*sqrt(N)) in the worst case due to exploring all possible states
# S.C : Memoization arr to store all possible states. ~ O(N) states possible
# According to the question we have to play it according to Alice's POV only
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [-1 for i in range(n+1)]
        def solve(n):
            if n == 0:
                return False
            if dp[n]!=-1:
                return dp[n]
            ans = False
            for i in range(1,int(sqrt(n))+1):
                # This here means if we choose to reduce a perfect sq which is less than n meaning if Alice chose to reduce it with the current i*i then we have to make sure we win since we are playing optimally so we want to make Bob lose for that we have to choose such that n-i*i is not a perfect square meaning if its not a perfect square we can still get a chance after Bob has played his chance. Why? Because if we choose a perfect sq such that n-perfect sq is not a perfect sq then we are sure we have a chance to win since if it was a perfect sq Bob would have chosen it and won.
                if solve(n-i*i) == False:
                    ans = True
                    break
            dp[n] = ans
            return dp[n]
            
        return solve(n)



# Approach-2 (Bottom up Dp)
# T.C : O(N*sqrt(N)) in the worst case due to exploring all possible states
# S.C : Memoization arr to store all possible states. ~ O(N) states possible
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [-1 for i in range(n+1)]
        dp[0] = False
        for num in range(1,n+1):
            ans = False
            for i in range(1,int(sqrt(num))+1):
                if dp[num-i*i] == False:
                    ans = True
                    break
            dp[num] = ans
        return dp[n]
        
