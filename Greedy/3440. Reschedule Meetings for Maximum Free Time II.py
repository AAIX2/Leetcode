# Approach (Greedily trying moving each event)
# T.C : O(n)
# S.C : O(n)

class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)

        suffixMax = [0]*n
        curMax = eventTime-endTime[-1] if endTime[-1]!=eventTime else 0
        for i in range(n-2,-1,-1):
            suffixMax[i] = max(curMax,suffixMax[i+1])
            curMax = max(curMax,startTime[i+1]-endTime[i])
        
        res = 0
        prefix = 0
        for i in range(n):
            st,end = startTime[i],endTime[i]
            prevEnd = endTime[i-1] if i-1>=0 else 0
            nextSt = startTime[i+1] if i+1<n else eventTime
            leftGap = st-prevEnd
            rightGap = nextSt-end
            
            res = max(res,leftGap+rightGap)
            if max(prefix,suffixMax[i])>=(end-st):
                res = max(res,(end-st)+leftGap+rightGap)
            
            prefix = max(prefix,leftGap)
        return res

        