# Approach-1 (By converting to intervals and finding the max intervals we can get)
# T.C : O(nlogn)
# S.C : O(n)

from collections import deque

def maximumBeauty(nums, k):
    # Step 1: Create ranges based on nums and k
    ranges = [(num - k, num + k) for num in nums]

    # Step 2: Sort the ranges by their start points
    ranges.sort()

    max_beauty = 0
    deq = deque()

    # Step 3: Process ranges to find the maximum beauty
    for start, end in ranges:
        while deq and deq[0] < start:
            deq.popleft()

        deq.append(end)
        max_beauty = max(max_beauty, len(deq))

    return max_beauty


# Approach-2 (Sorting and Using Binary Search)
# T.C : O(nlogn)
# S.C : O(1)

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        def binarySearch(num):
            low = 0
            high = n-1
            while low<=high:
                mid = (low+high)//2
                if nums[mid]<=num:
                    low = mid+1
                else:
                    high = mid-1
            return high
        maxcnt = 0
        for i in range(n):
            idx = binarySearch(nums[i]+2*k)
            maxcnt = max(maxcnt,idx-i+1)
        return maxcnt

# Approach-3 (Using Sliding Window)
# T.C : O(nlogn)
# S.C : O(1)

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        i = j = 0
        maxlen = 0
        while j<n:
            if i<j and nums[j]-k>nums[i]+k:
                i+=1
            maxlen = max(maxlen,j-i+1)
            j+=1
        return maxlen
    

# Approach-4 (Using Prefix Sum/ Line Sweep algo)
# T.C : O(n+maxEle)
# S.C : O(maxEle)

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        n = len(nums)
        intervals = [0]*(max(nums)+k+2)
        for i in range(n):
            if nums[i]-k<0:
                intervals[0]+=1
                
            else:
                intervals[nums[i]-k] += 1
                
            intervals[nums[i]+k+1]-=1
        maxcnt = 0
        cnt = 0
        for i in range(len(intervals)):
            val = intervals[i]
            cnt+=val
            maxcnt = max(maxcnt,cnt)
        return maxcnt
