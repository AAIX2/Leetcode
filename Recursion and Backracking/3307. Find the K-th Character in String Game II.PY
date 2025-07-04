# Approach - Recursion
# T.C : O(log(k))
# S.C : O(log(k))) of system stack

class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        n = len(operations)
        def solve(ind,k):
            if ind == 0:
                if k == 1:
                    return 0
                else:
                    if operations[ind] == 1:
                        return 1
                    return 0
            total = 2**(ind+1)
            mid = total//2
            if k<=mid:
                return solve(ind-1,k)
            else:
                if operations[ind] == 1:
                    return (1+solve(ind-1,k-mid))%26
                return solve(ind-1,k-mid)
        ans = chr(ord('a')+solve(n-1,k))
        return ans