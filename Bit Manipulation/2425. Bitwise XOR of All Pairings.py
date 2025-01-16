# Approach-1 (Using frequency count and Xor Property)
# T.C : O(n)
# S.C : O(n)


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        mp = defaultdict(int)

        for num in nums1:
            mp[num]+=m


        for num in nums2:
            mp[num]+=n
        
        
        res = 0
        for i in mp:
            if mp[i]%2:
                res^=i
        return res
    

# Approach-2 (Using Xor property)
# T.C : O(n)
# S.C : O(1)

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)

        def getXor(arr):
            xor = 0
            for num in arr:
                xor^=num
            return xor
        
        
        xor1 = 0
        xor2 = 0
        if m%2:
            xor1 = getXor(nums1)
        if n%2:
            xor2 = getXor(nums2)
        return xor1^xor2