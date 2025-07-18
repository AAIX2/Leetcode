# Approach (Using 2 heaps and cumulative sum)
# T.C : O(NlogN)
# S.C : O(N)

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        N = len(nums)
        n = len(nums)//3
        maxHeap = []
        curSum = 0
        minSum = [0]*(N)
        for i in range(N-n):
            curSum+=nums[i]
            heapq.heappush(maxHeap,-nums[i])
            if len(maxHeap)>n:
                ele = heapq.heappop(maxHeap)
                curSum-=abs(ele)
            if len(maxHeap) == n:
                minSum[i] = curSum
            
        
        minHeap = []
        curSum = 0
        res = float('inf')
        for i in range(N-1,n-1,-1):
            curSum+=nums[i]
            heapq.heappush(minHeap,nums[i])
            if len(minHeap)>n:
                ele = heapq.heappop(minHeap)
                curSum-=ele
            if len(minHeap) == n:
                res = min(res,minSum[i-1]-curSum)
        return res
                
            
        