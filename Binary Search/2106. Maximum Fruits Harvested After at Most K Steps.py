# Approach (Binary Search and prefix sum)
# T.C : O(n+klogn)
# S.C : O(n)

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        arr = [fruits[0][1]]
        positions = [fruits[0][0]]
        for i in range(1,len(fruits)):
            pos,f = fruits[i]
            arr.append(arr[-1]+f)
            positions.append(pos)
        
        res = 0
        for d in range(0,(k//2)+1):
            leftPos1 = startPos-d
            rightPos1 = startPos+(k-2*d)
            l = bisect_left(positions,leftPos1)
            r = bisect_right(positions,rightPos1)-1
            if l<=r:
                res = max(res,arr[r]-(arr[l-1] if l-1>=0 else 0))
        
            rightPos2 = startPos+d
            leftPos2 = max(startPos-(k-2*d),0)
            l = bisect_left(positions,leftPos2)
            r = bisect_right(positions,rightPos2)-1
            if l<=r:
                res = max(res,arr[r]-(arr[l-1] if l-1>=0 else 0))
        return res

        