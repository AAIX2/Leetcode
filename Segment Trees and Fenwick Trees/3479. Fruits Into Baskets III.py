# Approach (Using Segment Tree Range Maximum Query + Binary Search)
# T.C : O(nlogn)
# S.C : O(n)

class SegmentTree:
    def __init__(self,n,arr):
        self.t = [0]*4*n
        self.arr = arr
    def build(self,v,tl,tr):
        if tl == tr:
            self.t[v] = self.arr[tl]
            return 
        mid = (tl+tr)//2
        self.build(2*v,tl,mid)
        self.build(2*v+1,mid+1,tr)
        self.t[v] = max(self.t[2*v],self.t[2*v+1])
    def search(self,v,tl,tr,val):
        if self.t[v]<val:
            return -1
        if tl == tr:
            self.t[v] = -1
            return 
        mid = (tl+tr)//2
        if self.t[2*v]>=val:
            self.search(2*v,tl,mid,val)
        else:
            self.search(2*v+1,mid+1,tr,val)
        self.t[v] = max(self.t[2*v],self.t[2*v+1])
        

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        tree = SegmentTree(n,baskets)
        tree.build(1,0,n-1)
        
        cnt = 0
        for f in fruits:
            if tree.search(1,0,n-1,f) == -1:
                cnt+=1
        return cnt
        