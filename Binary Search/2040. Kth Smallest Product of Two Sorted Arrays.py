# Approach (Binary Search on Answer)
# T.C : O(log(maxP-minP) * n * log(m)
# S.C : O(1)

class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)
        m = len(nums2)
        

        def isPossible(mid):
            cnt = 0
            for i in range(n):
                val = nums1[i]
                
                if val == 0 and mid>=0:
                    cnt+=m
                elif val<0:
                    cnt+=(m-bisect_left(nums2,-(-mid//val)))
                elif val>0:
                    cnt+=bisect_right(nums2,mid//val)
                
                if cnt>=k:
                    return True
                
            return cnt>=k

        low = min(nums1[0]*nums2[0], nums1[0]*nums2[-1], nums1[-1]*nums2[0], nums1[-1]*nums2[-1])
        high = max(nums1[0]*nums2[0], nums1[0]*nums2[-1], nums1[-1]*nums2[0], nums1[-1]*nums2[-1])
        while low<=high:
            mid = (low+high)//2
            
            if isPossible(mid):
                high = mid-1
            else:
                low = mid+1
        return low

        