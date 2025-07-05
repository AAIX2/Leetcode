# Approach-1 (Using fixed size array to store frequency)
# T.C : O(n)
# S.C : O(n)

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        mp = defaultdict(int)
        for num in arr:
            mp[num]+=1
        res = -1
        for num in mp:
            if mp[num] == num:
                res = max(res,num)
        return res
    

# Approach-2 (Using fixed size array to store frequency)
# T.C : O(n)
# S.C : O(501) ~ O(1)

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        mp = [0]*501
        for num in arr:
            mp[num]+=1
        res = -1
        for i in range(501):
            if mp[i] and mp[i] == i:
                res = max(res,i)
        return res
    

# Approach-3 (Using bits to store frequency)
# T.C : O(n)
# S.C : O(1) in place

class Solution:
    def findLucky(self, arr):
        n = len(arr)

        for i in range(n):
            val = arr[i] & 65535
            if val <= n and val >= 1:
                arr[val - 1] += (1 << 16)  # Equivalent to 65536

        for val in range(n, 0, -1):
            if (arr[val - 1] >> 16) == val:
                return val

        return -1
