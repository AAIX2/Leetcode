# Approach (using observation by changing the brackets)
# T.C : O(n+m)
# S.C : O(1)


class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        n = len(arr1)
        m = len(arr2)
        xor1 = 0
        for num in arr1:
            xor1^=num
        xor2 = 0
        for num in arr2:
            xor2^=num
        return xor1&xor2