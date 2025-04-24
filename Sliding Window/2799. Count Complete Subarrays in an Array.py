# Approach (Sliding Window Khandani Template)
# T.C : O(2*n) ~ O(n)
# S.C : O(1)

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        c = len(set(nums))
        f = defaultdict(int)
        res = 0
        i = j = 0
        while j<n:
            f[nums[j]]+=1
            while i<=j and len(f) == c:
                res+=n-j
                f[nums[i]]-=1
                if not f[nums[i]]:
                    del f[nums[i]]
                i+=1
            j+=1
        return res
        