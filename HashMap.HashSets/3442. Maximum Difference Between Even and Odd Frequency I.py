# Approach (Straught forward maxOdd - minEven)
# T.C : O(n)
# S.C : O(1)

class Solution:
    def maxDifference(self, s: str) -> int:
        freq = [0]*26
        for ch in s:
            freq[ord(ch)-ord('a')]+=1
        maxEven,maxOdd = 0,0
        minEven,minOdd = len(s),len(s)
        for i in range(26):
            if freq[i] == 0:
                continue
            if freq[i]%2 == 1:
                maxOdd = max(maxOdd,freq[i])
                minOdd = min(minOdd,freq[i])
            else:
                maxEven = max(maxEven,freq[i])
                minEven = min(minEven,freq[i])
        return maxOdd-minEven