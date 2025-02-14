# Approach-1 (Brute Force)
# T.C : O(n^2 * m), m = number of digits
# S.C : O(1)

def get_digit_sum(num: int) -> int:
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total

def maximum_sum(nums: List[int]) -> int:
    n = len(nums)
    result = -1
    
    for i in range(n):
        digit_sumi = get_digit_sum(nums[i])
        
        for j in range(i + 1, n):
            digit_sumj = get_digit_sum(nums[j])
            
            if digit_sumi == digit_sumj:
                result = max(result, nums[i] + nums[j])
    
    return result


# Approach-2 (Optimal using Map)
# T.C : O(n*m), m = number of digits
# S.C : O(n)

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        n = len(nums)
        mp = defaultdict(int)
        def getDigitSum(num):
            s = 0
            while num:
                s+=(num%10)
                num//=10
            return s
        maxi = -1
        for i in range(n):
            num = nums[i]
            s = getDigitSum(num)
            if s in mp:
                maxi = max(maxi,num+mp[s])
            mp[s] = max(mp[s],num)
        return maxi
    
# Approach-3 (Optimal using Map of heaps)
# T.C : O(n*m), m = number of digits
# S.C : O(n)


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        n = len(nums)
        mp = [[]for i in range(82)]
        def getDigitSum(num):
            s = 0
            while num:
                s+=(num%10)
                num//=10
            return s
        
        for i in range(n):
            num = nums[i]
            s = getDigitSum(num)
            heapq.heappush(mp[s],num)
            if len(mp[s])>2:
                heapq.heappop(mp[s])
        maxi = -1
        for i in mp:
            if len(i) == 2:
                first = heapq.heappop(i)
                second = heapq.heappop(i)
                maxi = max(maxi,first+second)
        return maxi