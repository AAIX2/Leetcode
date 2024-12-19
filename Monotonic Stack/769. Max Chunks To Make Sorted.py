# Approach-1 (Using prefixMax and SuffixMin)
# T.C : O(n)
# S.C : O(n)

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        suffixMin = [i for i in arr]
        for i in range(n-2,-1,-1):
            suffixMin[i] = min(suffixMin[i],suffixMin[i+1])
        cnt = 0
        maxi = -1
        for i in range(n):
            if suffixMin[i]>maxi:
                cnt+=1
            maxi = max(maxi,arr[i])
        return cnt
    

# Approach-2 (Using prefix Sum)
# T.C : O(n)
# S.C : O(n)


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        cnt = 0
        sortedSum = 0
        s = 0
        for i in range(n):
            sortedSum+=i
            s+=arr[i]
            if s == sortedSum:
                cnt+=1
        return cnt
    

# Approach-3 (Using max check)
# T.C : O(n)
# S.C : O(1)

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        cnt = 0
        curMax = -1
        for i in range(n):
            curMax = max(curMax,arr[i])
            if curMax == i:
                cnt+=1
        return cnt
        

# Approach-4 (Using monotonic stack)
# T.C : O(n)
# S.C : O(n)

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        st = []
        for i in range(n):
            curMax = arr[i]
            while st and st[-1]>arr[i]:
                curMax = max(curMax,st.pop())
            st.append(curMax)
        return len(st)
        

