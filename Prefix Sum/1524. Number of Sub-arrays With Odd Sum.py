# Approach-1 (Brute Force)
# T.C : O(n^3)
# S.C : O(1)

class Solution:
    def numOfSubarrays(self, arr):
        M = int(1e9 + 7)
        n = len(arr)
        count = 0

        for i in range(n):
            for j in range(i, n):
                total = sum(arr[i:j+1])
                if total % 2 != 0:
                    count += 1

        return count % M
    

# Approach-2 (Better Brute Force)
# T.C : O(n^2)
# S.C : O(1)

class Solution:
    def numOfSubarrays(self, arr):
        M = int(1e9 + 7)
        n = len(arr)
        count = 0

        for i in range(n):
            total = 0
            for j in range(i, n):
                total += arr[j]
                if total % 2 != 0:
                    count = (count + 1) % M

        return count % M

# Approach-3 (Optimal using prefix-sum array)
# T.C : O(n)
# S.C : O(n)

class Solution:
    def numOfSubarrays(self, arr):
        M = int(1e9 + 7)
        n = len(arr)

        prefix = [0] * n
        prefix[0] = arr[0]

        for i in range(1, n):
            prefix[i] = prefix[i - 1] + arr[i]

        count = 0
        odd = 0
        even = 1  # To handle subarrays starting from index 0

        for i in range(n):
            if prefix[i] % 2 == 0:  # odd + even = odd
                count = (count + odd) % M
                even += 1
            else:  # even + odd = odd
                count = (count + even) % M
                odd += 1

        return count

# Approach-4 (Optimal using constant space)
# T.C : O(n)
# S.C : O(1)

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        even = 1
        odd = 0
        s = 0
        cnt = 0
        mod = 10**9+7
        for num in arr:
            s+=num
            if s%2:
                cnt+=even
                odd+=1
            else:
                cnt+=odd
                even+=1
        return cnt%mod
