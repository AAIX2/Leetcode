# Approach-1 (Using sorting with indices)
# T.C : O(nlogn)
# S.C : O(1)

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        maxHeap = []
        curSum = 0
        for i in range(n):
            heapq.heappush(maxHeap,[nums[i],i])
            if len(maxHeap)>k:
                heapq.heappop(maxHeap)
        ind = []
        while maxHeap:
            val,i = heapq.heappop(maxHeap)
            ind.append(i)
        ind.sort()
        res = []
        for i in ind:
            res.append(nums[i])
        return res


            
        