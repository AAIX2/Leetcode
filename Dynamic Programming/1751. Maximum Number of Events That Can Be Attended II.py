# Approach-1 (Top Down Dp)
# T.C : O(nlogn*k)
# S.C : O(n*k)


class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
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

        dp = [[-1 for i in range(k+1)]for i in range(n)]
        def solve(ind,cnt):
            if ind == n or cnt == 0:
                return 0
            if dp[ind][cnt]!=-1:
                return dp[ind][cnt]
            take = 0
            st,end,val = events[ind]
            if cnt:
                take = val+solve(binarySearch(end),cnt-1)
            not_take = solve(ind+1,cnt)
            dp[ind][cnt] = max(take,not_take)
            return dp[ind][cnt]
        return solve(0,k)
    
# Approach-2 (bottom Up Dp)
# T.C : O(nlogn*k)
# S.C : O(n*k)

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
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

        dp = [[0 for i in range(k+1)]for i in range(n+1)]
        for ind in range(n-1,-1,-1):
            for cnt in range(1,k+1):
                take = 0
                st,end,val = events[ind]
                if cnt:
                    take = val+dp[binarySearch(end)][cnt-1]
                not_take = dp[ind+1][cnt]
                dp[ind][cnt] = max(take,not_take)
        return dp[0][k]
        
# Approach-2 (bottom Up Dp)
# T.C : O(nlogn)
# S.C : O(n)

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        n = len(events)
        events.sort()
        next = [0]*n
        for i in range(n):
            end = events[i][1]
            low = i+1
            high = n-1
            ans = n
            while low<=high:
                mid = (low+high)//2
                if events[mid][0]>end:
                    high = mid-1
                else:
                    low = mid+1
            next[i] = low

        next1 = [0 for i in range(n+1)] 
        for cnt in range(1,k+1):
            cur = [0]*(n+1)
            for ind in range(n-1,-1,-1):
                take = 0
                st,end,val = events[ind]
                if cnt:
                    take = val+next1[next[ind]]
                not_take = cur[ind+1]
                cur[ind] = max(take,not_take)
            next1 = cur
        return next1[0]
        