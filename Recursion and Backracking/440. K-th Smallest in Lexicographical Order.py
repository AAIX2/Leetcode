# Approach-1 (Simple Recursion - DFS) - MEMORY LIMIT EXCEEDE (MLE)
# T.C : O(n)
# S.C : O(d) of system stack and O(n) for storing numbers in result array

class Solution:
    def solve(self, curr, n, result):
        if curr > n:
            return
        
        result.append(curr)

        for next_digit in range(10):
            next_num = curr * 10 + next_digit
            if next_num > n:
                return
            self.solve(next_num, n, result)

    def findKthNumber(self, n, k):
        result = []
        for num in range(1, 10):
            self.solve(num, n, result)
        return result[k - 1]



# Approach-2 (Simple Recursion - DFS without storing in result) - TIME LIMIT EXCEEDE (TLE)
# T.C : O(n)
# S.C : O(d) of system stack

class Solution:
    def __init__(self):
        self.count = 0
        self.result = 0

    def solve(self, curr: int, n: int, k: int) -> bool:
        if curr > n:
            return False

        self.count += 1
        if self.count == k:
            self.result = curr
            return True

        for next_digit in range(10):
            next_num = curr * 10 + next_digit
            if next_num > n:
                break
            if self.solve(next_num, n, k):
                return True

        return False

    def findKthNumber(self, n: int, k: int) -> int:
        for num in range(1, 10):
            if self.solve(num, n, k):
                break
        return self.result


# Approach-3 (Optimal) - ACCEPTED
# T.C : O((logn)^2)
# S.C : O(log(n)) system resursion stack

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        num = 1
        cnt = 1
        def count(cur):
            res = 0
            nei = cur+1
            while cur<=n:
                res+=min(nei,n+1)-cur
                cur*=10
                nei*=10
            return res
        while cnt<k:
            steps = count(num)
            if cnt+steps<=k:
                num+=1
                cnt+=steps
            else:
                num*=10
                cnt+=1
        return num