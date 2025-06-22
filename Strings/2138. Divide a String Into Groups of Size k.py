# Approach (Simple iterating and generating)
# T.C : O(n)
# S.C : O(k)

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)
        res = []
        for i in range(0,n,k):
            cur = []
            for j in range(i,min(i+k,n)):
                cur.append(s[j])
            if len(cur)<k:
                cur+=[fill]*(k-len(cur))
            res.append("".join(cur))
        return res
        