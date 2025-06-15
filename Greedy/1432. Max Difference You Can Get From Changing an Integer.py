# Approach-1 (Simple iterating on digits)
# T.C : O(log10(n))
# S.C : O(log10(n))

class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)
        n = len(s)
        
        maxNum = ""
        for ch in s:
            if ch!="9":
                maxNum = ch
                break
        if maxNum:
            maxi = s.replace(maxNum,"9")
        else:
            maxi = s
        mini = s
        if s[0] == "1":
            rep = ""
            for ch in s:
                if ch>"1":
                    rep = ch
                    break
            if rep:
                mini = s.replace(rep,"0")
        else:
            mini = s.replace(s[0],"1")

        
        return int(maxi)-int(mini)
