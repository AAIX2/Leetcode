# Approach  (Sliding Window)
# T.C : O(n)
# S.C : O(k)

class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        gaps = []
        if startTime[0]!=0:
            gaps.append(startTime[0])
        for i in range(1,n):
            gaps.append(startTime[i]-endTime[i-1])
        if endTime[-1]!=eventTime:
            gaps.append(eventTime-endTime[-1])
        
        i = j = 0
        ans = 0
        curSum = 0
        while j<len(gaps):
            curSum+=gaps[j]
            if j-i+1>k+1:
                curSum-=gaps[i]
                i+=1
            ans = max(ans,curSum)
            j+=1
        return ans