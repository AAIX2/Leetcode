# Approach (Sliding Window using map)
# T.C : O(n)
# S.C : O(n)

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        mp = defaultdict(int)
        res = 0
        i = j = 0
        while j<n:
            mp[fruits[j]]+=1
            while i<j and len(mp)>2:
                mp[fruits[i]]-=1
                if not mp[fruits[i]]:
                    del mp[fruits[i]]
                i+=1
            res = max(res,j-i+1)
            j+=1
        return res