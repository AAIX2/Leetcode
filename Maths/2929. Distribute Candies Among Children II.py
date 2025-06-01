# Approach - Using maths distribution
# T.C : O(n)
# S.C : O(1)

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        
        mini = min(n,limit)
        ans = 0
        for ch1 in range(mini+1):
            rem = n-ch1
            mini1 = min(limit,rem)
            if rem-mini1>mini1:
                continue
            maxCh2Candies = mini1
            minCh2Candies = rem-mini1
            total = (maxCh2Candies-minCh2Candies+1)
            ans+=total
        return ans