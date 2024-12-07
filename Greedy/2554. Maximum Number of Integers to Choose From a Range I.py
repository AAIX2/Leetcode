# Approach - Simple Greedily select smallest numbers
# T.C : O(n)
# S.C : O(m)

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        s = 0
        cnt = 0
        for i in range(1,n+1):
            if i not in banned:
                if s+i<=maxSum:
                    s+=i
                    cnt+=1
                else:
                    break
            # print(i,s,cnt)
        return cnt
    

# Approach - Using Binary Search
# T.C : O(nlogm + mlogm)
# S.C : O(m)

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned.sort()
        def binarySearch(num):
            low = 0
            high = len(banned)-1
            while low<=high:
                mid = (low+high)//2
                if banned[mid] == num:
                    return True
                elif banned[mid]<num:
                    low = mid+1
                else:
                    high = mid-1
            return False
        s = 0
        cnt = 0
        for i in range(1,n+1):
           
            if binarySearch(i) == False:
                if s+i<=maxSum:
                    s+=i
                    cnt+=1
                else:
                    break
            
        return cnt
