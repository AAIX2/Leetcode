# Approach-1 (Khandani Backtracking remplate - storing all possible strings)
# T.C : O(n * ((n/k)!))
# S.C : O(n/k)

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        n = len(s)
        lenOfSub = n//k
        freq = [0]*26
        for ch in s:
            freq[ord(ch)-ord('a')]+=1
        for i in range(26):
            freq[i]//=k

        def isSubsequence(s1,s2):
           
            m = len(s2)
            i = j = 0
            while i<n and j<k*m:
                if s1[i] == s2[j%m]:
                    i+=1
                    j+=1
                else:
                    i+=1
           
            return j == k*m
        
        res = []
        def solve(cur,maxLen):
            nonlocal res
            if len(cur)>maxLen:
                return 
            if (len(cur) > len(res)) or (len(cur) == len(res) and cur>res):
                if isSubsequence(s,cur):
                    res = cur[::] 
                    
            for i in range(26):
                if freq[i]:
                    freq[i]-=1
                    cur.append(chr(i+ord('a')))
                    solve(cur,maxLen)
                    freq[i]+=1
                    cur.pop()
        solve([],lenOfSub)
        return "".join(res)
    

# Approach-2 IMPROVED BACKTRACKING : (Khandani Backtracking remplate - storing all possible strings)
# T.C : O(n * ((n/k)!))
# S.C : O(n/k)

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        n = len(s)
        lenOfSub = n//k
        freq = [0]*26
        for ch in s:
            freq[ord(ch)-ord('a')]+=1
        for i in range(26):
            freq[i]//=k

        def isSubsequence(s1,s2):
           
            m = len(s2)
            i = j = 0
            while i<n and j<k*m:
                if s1[i] == s2[j%m]:
                    i+=1
                    j+=1
                else:
                    i+=1
           
            return j == k*m
        
        
        def solve(cur,maxLen):
            if len(cur) == maxLen:
                if isSubsequence(s,cur):
                    return True
                return False
                    
            for i in range(25,-1,-1):
                if freq[i]:
                    freq[i]-=1
                    cur.append(chr(i+ord('a')))
                    if solve(cur,maxLen):
                        return True
                    freq[i]+=1
                    cur.pop()
        for maxLen in range(lenOfSub,-1,-1):
            cur = []
            if solve(cur,maxLen):
                return "".join(cur)
        return ""