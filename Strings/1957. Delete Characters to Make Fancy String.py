# Approach (Simple straight forward traversal)
# T.C : O(n)
# S.C : O(1)

class Solution:
    def makeFancyString(self, s: str) -> str:
        res = []
        for ch in s:
            if len(res)>1:
                last = res[-1]
                secondLast = res[-2]
                if ch!=last or ch!=secondLast:
                    res.append(ch)
            else:
                res.append(ch)
        return "".join(res)
                