# Approach (Using map and approach similar to Two Sum Problem)
# T.C : O(m+n) for FindSumPairs(), O(1) for add() and O(n) for count()
# S.C : O(m+n) for vec1 and vec2

class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.mp1 = defaultdict(int)
        self.mp2 = defaultdict(int)
        for num in nums1:
            self.mp1[num]+=1
        for num in nums2:
            self.mp2[num]+=1
        self.nums2 = nums2

    def add(self, index: int, val: int) -> None:
        v = self.nums2[index]
        self.mp2[v]-=1
        self.mp2[v+val]+=1
        self.nums2[index]+=val

    def count(self, tot: int) -> int:
        res = 0
        for num in self.mp1:
            tar = tot-num
            res+=(self.mp1[num]*self.mp2[tar])
        return res


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)