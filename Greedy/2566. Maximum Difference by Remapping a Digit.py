# Approach-1 (Simple iterating on digits)
# T.C : O(log10(n))
# S.C : O(log10(n))

class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        maxi = ""
        mini = ""
        for ch in s:
            if ch!="9":
                maxi = ch
                break
        for ch in s:
            if ch != "0":
                mini = ch
                break
                
        maxNum = ""
        minNum = ""
        for ch in s:
            if ch == maxi:
                maxNum+="9"
            else:
                maxNum+=ch
            if ch == mini:
                minNum+="0"
            else:
                minNum+=ch
        
        return int(maxNum)-int(minNum)