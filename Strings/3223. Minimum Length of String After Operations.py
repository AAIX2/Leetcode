# Approach-1 - (Simple simulation)
# T.C : O(n)
# S.C : O(26) ~ O(1)

class Solution:
    def minimumLength(self, s: str) -> int:
        freq = [0]*26
        deleted = 0
        for ch in s:
            idx = ord(ch)-ord('a')
            freq[idx]+=1
            if freq[idx] == 3:
                deleted+=2
                freq[idx]-=2
        return len(s)-deleted


# Approach-2 - (Simple Observation)
# T.C : O(n)
# S.C : O(26) ~ O(1)

class Solution:
    def minimumLength(self, s: str) -> int:
        freq = [0]*26
        for ch in s:
            idx = ord(ch)-ord('a')
            freq[idx]+=1
        ans = 0
        for i in range(26):
            if not freq[i]:
                continue
            if freq[i]%2:
                ans+=1
            else:
                ans+=2
        return ans