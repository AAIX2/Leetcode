# Approach-1 (Using Segment Tree)
# T.C : O(n*log(n))
# S.C : O(n)


class SegmentTree:
    def __init__(self,n,arr):
        self.t = [0]*(4*n)
        self.a = arr 
    def query(self,v,tl,tr,l,r):
        if tl>r or tr<l:
            return 0
        if tl>=l and tr<=r:
            return self.t[v]
        tm = (tl+tr)//2
        left = self.query(2*v,tl,tm,l,r)
        right = self.query(2*v+1,tm+1,tr,l,r)
        return left+right
    def update(self,v,tl,tr,l,r):
        if tl>r or tr<l:
            return 
        if tl>=l and tr<=r:
            self.t[v] = 1
            return 
        tm = (tl+tr)//2
        self.update(2*v,tl,tm,l,r)
        self.update(2*v+1,tm+1,tr,l,r)
        self.t[v] = self.t[2*v]+self.t[2*v+1]
    def _query(self,l,r):
        return self.query(1,0,len(self.a)-1,l,r)
    def _update(self,l):
        return self.update(1,0,len(self.a)-1,l,l)
        
class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        ind = defaultdict(int)
        for i,num in enumerate(nums2):
            ind[num] = i
        tree = SegmentTree(n,nums1)
        res = 0
        for i,num in enumerate(nums1):
            idx = ind[num]
            leftCommonCount = tree._query(0,idx)
            leftUncommonCount = i-leftCommonCount
            rightCountNums2 = n-idx-1
            rightCommonCount = rightCountNums2-leftUncommonCount
            res+=leftCommonCount*rightCommonCount
            tree._update(idx)
        return res
