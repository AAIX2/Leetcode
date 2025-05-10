# Approach (Using simple greedy)
# T.C : O(m+n), m = nums1.size() , n = nums2.size()
# S.C : O(1)

class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        s1 = 0
        z1 = 0
        for num in nums1:
            s1+=num
            if num == 0:
                s1+=1
                z1+=1
        s2,z2 = 0,0
        for num in nums2:
            s2+=num
            if num == 0:
                s2+=1
                z2+=1
        if (s2>s1 and not z1) or (s1>s2 and not z2):
            return -1
        return max(s1,s2)