# Approach-1 (Using prefix sum)
# T.C : O(n + m)
# S.C : O(n)

# THe intuition is to store for every index what is the cnt of violating indices uptil that ind. Also the first ind can never be a violating index
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        m = len(queries)
        prefixCnt = [0]*n
        for i in range(1,n):
            if (nums[i]%2 and nums[i-1]%2) or (nums[i]%2 == 0 and nums[i-1]%2 == 0):
                prefixCnt[i] = 1+prefixCnt[i-1]
            else:
                prefixCnt[i] = prefixCnt[i-1]
        ans = []
        for i,j in queries:
            if prefixCnt[j]-prefixCnt[i] == 0:
                ans.append(True)
            else:
                ans.append(False)
        return ans
    
# Approach-2 (Using 2 pointers/Sliding Window)
# T.C : O(n + m)
# S.C : O(n)
# The intuition here is to simply store the max end index possible for every index such that uptil that ind the subarray is special or valid 
class Solution:
    def isArraySpecial(
        self, nums: List[int], queries: List[List[int]]
    ) -> List[bool]:
        n = len(nums)
        max_reach = [0] * n
        end = 0

        # Step 1: Compute the maximum reachable index for each starting index
        for start in range(n):
            # Ensure 'end' always starts from the current index or beyond
            end = max(end, start)
            # Expand 'end' as long as adjacent elements have different parity
            while end < n - 1 and nums[end] % 2 != nums[end + 1] % 2:
                end += 1
            # Store the farthest index reachable from 'start'
            max_reach[start] = end

        ans = []

        # Step 2: Answer each query based on precomputed 'max_reach'
        for start, end_query in queries:
            # Check if the query range [start, end] lies within the max reachable range
            ans.append(end_query <= max_reach[start])
        return ans
    
# Approach-3 (Using binary search)
# T.C : O(n + m*logn)
# S.C : O(n)


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        violatingIndices = []
        for i in range(1,n):
            if nums[i]%2!=nums[i-1]%2:
                continue
            violatingIndices.append(i)
        
        
        def binarySearch(st,end):
            low = 0
            high = len(violatingIndices)-1
            while low<=high:
                mid = (low+high)//2
                if st<=violatingIndices[mid]<=end:
                    return True
                elif violatingIndices[mid]>end:
                    high = mid-1
                else:
                    low = mid+1
            return False
        
        
        ans = []
        for i,j in queries:
            if binarySearch(i+1,j):
                ans.append(False)
            else:
                ans.append(True)
        return ans
