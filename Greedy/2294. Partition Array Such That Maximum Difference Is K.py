# T.C : O(nlogn)
# S.C : O(n)

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        cnt = 1
        st = nums[0]
        for i in range(1,n):
            if nums[i]-st<=k:
                continue
            else:
                st = nums[i]
                cnt+=1
        return cnt