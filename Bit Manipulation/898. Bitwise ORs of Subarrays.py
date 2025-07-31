# Approach (using hashset to store previous or values)
# T.C : O(n*32) ~ O(n)
# S.C : O(n*32) ~ O(n)

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        n = len(arr)
        res = set()
        prevOrs = set()
        for i in range(n):
            curOrs = set()
            curOrs.add(arr[i])
            for j in prevOrs:
                curOrs.add(arr[i]|j)
            res|=curOrs
            prevOrs = curOrs
            
        return len(res)