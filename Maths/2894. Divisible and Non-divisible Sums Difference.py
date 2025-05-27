# Approach - Constant time using maths
# T.C : O(1)
# S.C : O(1)

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total = (n*(n+1))//2
        numbersDivBym = n//m
        num2 = m*(numbersDivBym*(numbersDivBym+1))//2
        num1 = total-num2
        return num1-num2