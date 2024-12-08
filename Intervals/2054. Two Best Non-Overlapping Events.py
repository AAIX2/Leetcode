# Approach-1 (Brute Force) - TLE
# T.C : O(n^2)
# S.C : O(1)

class Solution:
    def maxTwoEvents(self, events: list[list[int]]) -> int:
        n = len(events)
        result = 0

        for i in range(n):
            result = max(result, events[i][2])  # Consider single event's value
            
            val = events[i][2]
            for j in range(n):
                if i == j:
                    continue
                
                # Check if events overlap
                if events[j][0] <= events[i][1] and events[j][1] >= events[i][0]:
                    continue
                
                result = max(result, val + events[j][2])
        
        return result

# Approach-2 Using Binary Search and suffix max
# T.C : O(nlogn)
# S.C : O(n)
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        events.sort()
        suffixMax = [0]*n
        suffixMax[-1] = events[-1][2]
        for i in range(n-2,-1,-1):
            suffixMax[i] = max(events[i][2],suffixMax[i+1])
        def binarySearch(end):
            low = 0
            high = n-1
            while low<=high:
                mid = (low+high)//2
                if events[mid][0]>end:
                    high = mid-1
                else:
                    low = mid+1
            return low
        maxi = 0
        
        for i,j,val in events:
            v = val
            idx = binarySearch(j)
            if idx!=n:
                maxi = max(maxi,v+suffixMax[idx])
            else:
                maxi = max(maxi,v)
        return maxi

# Approach-3 Using knapsack DP
# T.C : O(nlogn)
# S.C : O(n)

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        events.sort()
        def binarySearch(end):
            low = 0
            high = n-1
            while low<=high:
                mid = (low+high)//2
                if events[mid][0]>end:
                    high = mid-1
                else:
                    low = mid+1
            return low
        dp = [[-1 for i in range(2)]for i in range(n)]
        def solve(ind,cnt):
            if ind == n or cnt == 2:
                return 0
            if dp[ind][cnt]!=-1:
                return dp[ind][cnt]
            idx = binarySearch(events[ind][1])
            take = events[ind][2]
            if idx<n and events[idx][0]>events[ind][1]:
                take = events[ind][2]+solve(idx,cnt+1)
            not_take = solve(ind+1,cnt)
            dp[ind][cnt] = max(take,not_take)
            return dp[ind][cnt]
        return solve(0,0)

# Approach-4 Using Line Sweep and greedy
# T.C : O(nlogn)
# S.C : O(n)        

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        e = []
        for i,j,v in events:
            e.append([i,1,v])
            e.append([j+1,0,v])
        e.sort()
        maxVal = 0
        maxSum = 0
        for st,isStart,v in e:
            if isStart:
                maxSum = max(maxSum,maxVal+v)
            else:
                maxVal = max(maxVal,v)
        return maxSum

        
# Approach-5 Using heap
# T.C : O(nlogn)
# S.C : O(n)        

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        heap = []
        events.sort()
        max_val = 0
        max_sum = 0
        for i,j,val in events:
            while heap and heap[0][0]<i:
                max_val = max(max_val,heap[0][1])
                heapq.heappop(heap)
            max_sum = max(max_sum,max_val+val)
            heapq.heappush(heap,[j,val])
        return max_sum

        


        
        

                