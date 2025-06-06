# Approach (Greedily finding the minimum character to right)
# T.C : O(n)
# S.C : O(n)


class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        freq = [0]*26
        for ch in s:
            freq[ord(ch)-ord('a')]+=1
        res = []
        t = []
        ind = 0
        for i in range(26):
            while t and ord(t[-1])-ord('a')<=i:
                res.append(t.pop())
                
            while ind<n and freq[i]:
                idx = ord(s[ind])-ord('a')
                if idx == i:
                    res.append(s[ind])
                else:
                    t.append(s[ind])
                freq[idx]-=1
                ind+=1
            
        return "".join(res)