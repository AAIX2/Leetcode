# Approach-1 (Using simple recursion to find subsets)
# T.C : O(2^n)
# S.C : O(1)

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        maxOr = 0
        for num in nums:
            maxOr|=num

        def solve(ind,curOr):
            if ind == n:
                if curOr == maxOr:
                    return 1
                return 0
            res = 0
            take = solve(ind+1,curOr|(nums[ind]))
            not_take = solve(ind+1,curOr)
            return take+not_take
        return solve(0,0)
        
# Approach-2 (Memoizing to store subproblems result)
# T.C : O(n*maxOr)
# S.C : O(1)

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        maxOr = 0
        for num in nums:
            maxOr|=num
        @cache
        def solve(ind,curOr):
            if ind == n:
                if curOr == maxOr:
                    return 1
                return 0
            res = 0
            take = solve(ind+1,curOr|(nums[ind]))
            not_take = solve(ind+1,curOr)
            return take+not_take
        return solve(0,0)
        
