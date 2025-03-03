# Approach-1 (Using extra space of 3 vectors)
# T.C : O(n)
# S.C : O(n)

from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_pivot = []
        equal_pivot = []
        greater_pivot = []

        for num in nums:
            if num < pivot:
                less_pivot.append(num)
            elif num == pivot:
                equal_pivot.append(num)
            else:
                greater_pivot.append(num)

        return less_pivot + equal_pivot + greater_pivot


# Approach-2 (Using pointers only)
# T.C : O(n)
# S.C : O(n)


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        cntOfSmaller = 0
        cntOfEqual = 0
        for num in nums:
            cntOfSmaller+=(1 if num<pivot else 0)
            cntOfEqual+=(1 if num == pivot else 0)
        res = [0]*len(nums)
        i = 0
        j = cntOfSmaller
        k = cntOfSmaller+cntOfEqual
        for num in nums:
            if num<pivot:
                res[i] = num
                i+=1
            elif num == pivot:
                res[j] = num
                j+=1
            else:
                res[k] = num
                k+=1
        return res 
    

# Approach-3 (Using pointers only)
# T.C : O(n)
# S.C : O(n)

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        res = [float('inf')]*n
        i = 0
        j = n-1
        low = 0
        high = n-1
        while i<n and j>=0:
            if nums[i]<pivot:
                res[low] = nums[i]
                low+=1
            if nums[j]>pivot:
                res[high] = nums[j]
                high-=1
            i+=1
            j-=1
        while low<=high:
            res[low] = pivot
            low+=1
        return res