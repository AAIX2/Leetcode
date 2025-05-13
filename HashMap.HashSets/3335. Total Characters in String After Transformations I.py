# Approach - Using frequency count in map
# T.C : O(n+t)
# S.C : O(26) ~= O(1)


class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        n = len(s)
        mod = 10**9+7
        freq = [0 for i in range(26)]
        for ch in s:
            idx = ord(ch)-ord('a')
            freq[idx]+=1
        
        for i in range(t):
            j = 0
            freq1 = [0]*26
            while j<26:
                
                if j == 25:
                    freq1[0] += freq[j]
                    freq1[1] += freq[j]
                else:
                    freq1[j+1] += freq[j]
                j+=1
            freq = freq1
        
        cnt = 0
        for i in range(26):
            cnt+=freq[i]
        return cnt%mod
        

# Approach - Using one arr
# T.C : O(n+t)
# S.C : O(26) ~= O(1)


class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10**9+7
        freq = [0]*26
        for ch in s:
            freq[ord(ch)-ord('a')]+=1
        
        for i in range(t):
            curLen = 0
            zFreq = freq[25]
            for j in range(25,0,-1):
                freq[j] = freq[j-1]
            freq[0] = zFreq
            freq[1] += zFreq
            
        return sum(freq)%mod
            
            


                    