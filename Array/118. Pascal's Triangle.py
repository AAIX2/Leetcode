# Approach-1 (Doing simply just like Pascal triangle is formed)
# Time Complexity O(n**2)
# Space Complexity O(1)
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1,numRows):
            cur = [1]
            prev = res[-1]
            for j in range(1,i):
                cur.append(prev[j]+prev[j-1])
            cur.append(1)
            res.append(cur)
        return res