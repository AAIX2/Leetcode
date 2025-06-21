# Approach-1 (Straight forward)
# T.C : O(n)
# S.C : O(1)

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        n = len(word)
        freq = [0]*26
        for i in range(n):
            freq[ord(word[i])-ord('a')]+=1
        res = n
        for i in range(26):
            if freq[i]!=0:
                deletions = 0
                for j in range(26):
                    if freq[j]!=0 and j!=i:
                        if freq[j]<freq[i]:
                            deletions+=freq[j]
                        elif freq[j]>freq[i]+k:
                            deletions+=freq[j]-freq[i]-k
                res = min(res,deletions)
        return res
    

# Approach-2 (slight optimisation of above approach)
# T.C : O(n) because other iterations are on a constant sized array
# S.C : O(1) - 26 sized array

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        n = len(word)
        freq = [0]*26
        for i in range(n):
            freq[ord(word[i])-ord('a')]+=1
        freq.sort()
        res = n
        curSum = 0
        for i in range(26):
            if freq[i]!=0:
                deletions = 0
                for j in range(25,i,-1):
                    if freq[j]!=0:
                        if freq[j]>freq[i]+k:
                            deletions+=freq[j]-freq[i]-k
                        else:
                            break
                res = min(res,deletions+curSum)
                curSum+=freq[i]
        return res