# Approach-1 (By converting to intervals and finding the max intervals we can get)
# T.C : O(nlogn)
# S.C : O(n)
# Mainly the intuition here is to see that we can convert each nums[i] into a range values which converts it into an interval based problem.

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

# Example:- 
# [4,6,1,2], k = 2

# Question says that we can "Replace nums[i] with any integer from the range [nums[i] - k, nums[i] + k]".

# This means we can replace the element of the array with any value within the shown range below.

#                 [ 4   6   1   2 ]
# min of range =    2   4  -1   0     i.e. nums[i] - k 
# max of range =    6   8   3   4     i.e. nums[i] + k 

# Now, to be a "Beautiful Subsequence" all elements of the subsequence should be equal.

# All elements can be equal if the "max of range of minimum element is greater than equal to min of range of maxium element".
# Didn't get it 🤯 no problem lets visulaize:- 

# for the above example ~
# Minimum Element = 1 and max of range of 1 = 3
# Maixium Element = 6 and min of range of 6 = 4

# this means if we replace 1 with max of it's range i.e. 3 and we replace 6 with min of it's range i.e. 4,
# still we can't make 1 and 6 equal.

# So what can we do is either increment minimum i.e. ignore 1 or decrement maximum i.e. ignore 6 both will work. I'll ignore the minimum i.e. 1.

# I think now this condition "max of range of minimum element is greater than equal to min of range of maxium element" makes sense 😉.

# Okay, now the next minimum is 2 as we have igonred 1. Lets check the condition.

# for the above example ~
# Minimum Element = 2 and max of range of 2 = 4
# Maixium Element = 6 and min of range of 6 = 4

# this means if we replace 2 with max of it's range i.e. 4 and we replace 6 with min of it's range i.e. 4,
# we can make 2 and 6 equal.

# So the number of elements in the "Beautiful Subsequence" is 3 as we have ignored element '1'.
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
