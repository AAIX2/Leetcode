# Approach : (Recursion)
# T.C : T(n) = n^2 * T(n/2) -> Homework for you. Comment in the video your solution
# S.C : No extra space taken (ignoring the system recursion space)

class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        
        left = firstPlayer
        right = secondPlayer

        # Both players are gonna face now in this round
        if left == n-right+1:
            return [1,1]
        # if left player position>the right players figthing opponent
        if left>n-right+1:
            temp = n-left+1
            left = n-right+1
            right = temp
        
        earliestRound = float('inf')
        latestRound = float('-inf')
        nextPlayerCnt = (n+1)//2
        # if both are in the left half 
        if right<=nextPlayerCnt:
            cntLeft = left-1
            cntMid = right-left-1
            for survivorsLeft in range(cntLeft+1):
                for survivorsMid in range(cntMid+1):
                    leftPos = survivorsLeft+1
                    rightPos = leftPos+survivorsMid+1
                    ans = self.earliestAndLatest(nextPlayerCnt,leftPos,rightPos)
                    earliestRound = min(earliestRound,ans[0]+1)
                    latestRound = max(latestRound,ans[1]+1)
        # if both or right player is in the right half
        else:
            cntLeft = left-1
            fightsRight = n-right+1
            cntMid = fightsRight-left-1
            remMidCnt = right-fightsRight-1
            for survivorsLeft in range(cntLeft+1):
                for survivorsMid in range(cntMid+1):
                    leftPos = survivorsLeft+1
                    rightPos = leftPos+survivorsMid+(remMidCnt+1)//2+1
                    ans = self.earliestAndLatest(nextPlayerCnt,leftPos,rightPos)
                    earliestRound = min(earliestRound,ans[0]+1)
                    latestRound = max(latestRound,ans[1]+1)
        return [earliestRound,latestRound]
