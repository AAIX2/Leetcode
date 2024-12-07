# Using Sorted List
from sortedcontainers import SortedList
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        

        arr = SortedList(range(1, n))
        ans = []
        
        for n1, n2 in queries:
            l = bisect_right(arr, n1)
            r = bisect_left(arr, n2)
            # Efficiently remove elements within the range [l, r)
            for i in range(l, r):
                arr.discard(arr[l])  # O(log n) for each deletion
            ans.append(len(arr))

        return ans
# Time Complexity- O(Q*log(n))
# Space- O(n)

# Using normal arr
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        arr = [i for i in range(1,n)]
        ans =[]
        # print(arr)

        for n1,n2 in queries:
            l = bisect_right(arr,n1)
            r = bisect_left(arr,n2)
            for i in range(l,r):
                arr.pop(l)
            ans.append(len(arr))
        return ans
# Time Complexity- O(Q*(log(n)+n))
# Space- O(n)




                