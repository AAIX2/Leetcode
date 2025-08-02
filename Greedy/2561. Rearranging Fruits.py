# Approach (Greedily swapping directly element or swapping via minimum element)
# T.C : O(n), Average time complexity of nth_element is O(n)
# S.C : O(n)

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        mp = defaultdict(int)
        mini = float('inf')
        for f in basket1:
            mp[f]+=1
            mini = min(mini,f)
        for f in basket2:
            mp[f]-=1
            mini = min(mini,f)
        extra = []
        for f in mp:
            freq = abs(mp[f])
            if freq%2:
                return -1
            extra+=[f]*(freq//2)
        if not extra:
            return 0
        
        extra.sort()
        
        ans = 0
        for i in range(len(extra)//2):
            ans += min(mini*2,extra[i])
        return ans