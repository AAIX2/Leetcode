# Approach (Iterating and finding best at each point of time)
# T.C : O(n)
# S.C : O(n)

class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        n = len(s)
        maxCnt = 0
        nCnt = 0
        sCnt = 0
        wCnt = 0
        eCnt = 0
        for i in range(n):
            if s[i] == "W":
                wCnt+=1
            elif s[i] == "E":
                eCnt+=1
            elif s[i] == "N":
                nCnt+=1
            else:
                sCnt+=1
        
            maxi1 = max(sCnt,nCnt)
            mini1 = min(sCnt,nCnt)
            maxi2 = max(eCnt,wCnt)
            mini2 = min(eCnt,wCnt)
            maxCnt =  max(maxCnt,maxi1+maxi2-mini1-mini2+2*(min(k,mini1+mini2)))
        return maxCnt
                
