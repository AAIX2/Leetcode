# Approach (Simply iterate and find valid indices. Just be careful of corner cases and overlapping indices
# T.C : O(n), we visit every index only 2 times.
# S.C : O(1)

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        res = []
        for i in range(n):
            if nums[i] == key:
                left = max(0,i-k)
                right = min(n-1,i+k)+1
                if res and res[-1]>=left:
                    left = res[-1]+1
                for j in range(left,right):
                    res.append(j)
        return res