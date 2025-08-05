# Approach (Using brute force)
# Time O(n**2)
# Space O(n)

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        vis = set()
        cnt = 0
        for f in fruits:
            flag = False
            for i,b in enumerate(baskets):
                if b>=f and i not in vis:
                    vis.add(i)
                    flag = True
                    break
            if not flag:
                cnt+=1
        return cnt
        