# Approach-1 (Using Recursion)
# T.C : O(2^n), take and skip
# S.C : O(1) auxiliary space, and O(n) of recursion stack

class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)

        def solve(i: int, k: int) -> int:
            if i < 0:
                return 0

            take = 0
            bit = int(s[i])
            value = (1 << (n - i - 1)) if bit == 1 else 0

            if value <= k:
                take = 1 + solve(i - 1, k - value)

            skip = solve(i - 1, k)
            return max(take, skip)

        return solve(n - 1, k)
    
# Approach-2 (Using Greedy)
# T.C : O(n)
# S.C : O(1)

class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        s = s[::-1]
        num = 0
        cnt = 0
        for i in range(n):
            if s[i] == "0":
                cnt+=1
            else:
                if num|(1<<cnt)<=k:
                    num|=(1<<cnt)
                    cnt+=1
        return cnt
        
