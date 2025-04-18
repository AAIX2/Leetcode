# Approach-1 (Using Hashmap)
# T.C : O(n)
# S.C : O(26)

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        n = len(s)
        if k>n:
            return False
        if k == n:
            return True
        freq = Counter(s)
        
        oddCnt = 0
        for i in freq:
            if freq[i]%2:
                oddCnt+=1
        if oddCnt>k:
            return False
        else:
            return True