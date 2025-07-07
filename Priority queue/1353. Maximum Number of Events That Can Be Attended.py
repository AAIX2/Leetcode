# Approach (Using Sorting and heap and hreedily picking the ones ending earliest)
# T.C : O(nlogn)
# S.C : O(n)

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        events.sort()
        minHeap = []
        maxDay = max(events[i][1] for i in range(n))
        day = 1
        res = 0
        i = 0
        while day<=maxDay:
            if i<n and not minHeap:
                day = events[i][0]
            
            while i<n and events[i][0]<=day:
                heapq.heappush(minHeap,events[i][1])
                i+=1

            while minHeap and minHeap[0]<day:
                heapq.heappop(minHeap)
            
            if minHeap:
                heapq.heappop(minHeap)
                res+=1
            elif i>=n:
                break
            day+=1
        return res

        

            
        