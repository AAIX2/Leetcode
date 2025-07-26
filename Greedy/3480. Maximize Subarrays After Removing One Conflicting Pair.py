# Approach (Greedily maximizing the extra gains)
# T.C : O(n+p), p = total number of conflicting points, n = total points
# S.C : O(n)

class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        valid = 0
        conflictingPoints = [[] for i in range(n+1)]

        for x,y in conflictingPairs:
            mini = min(x,y)
            maxi = max(x,y)
            conflictingPoints[maxi].append(mini)
        # Extra subarr that we will get on removing this conflicting point i
        extra = [0]*(n+1)
        maxConflictingPoint = 0
        secondMaxConflictingPoint = 0

        for i in range(1,n+1):

            for p in conflictingPoints[i]:
                if p>=maxConflictingPoint:
                    secondMaxConflictingPoint = maxConflictingPoint
                    maxConflictingPoint = p
                elif p>secondMaxConflictingPoint:
                    secondMaxConflictingPoint = p

            valid += i-maxConflictingPoint
            extra[maxConflictingPoint] += maxConflictingPoint-secondMaxConflictingPoint
            
        
        return valid+max(extra)