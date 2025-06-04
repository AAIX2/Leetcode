# Approach-1 (trying at every index to find best substring)
# T.C : O(n^2)
# S.C : O(1)

class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        n = len(word)
        if numFriends == 1:
            return word
        rem = n-(numFriends-1)
        res = -1
        maxi = ""
        for i in range(n):
            if word[i:i+rem] > maxi:
                res = i
                maxi = word[i:i+rem]
        return word[res:res+rem]
        

# Approach-2 (2 Pointer)
# T.C : O(n)
# S.C : O(1)

class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        n = len(word)
        if numFriends == 1:
            return word
        rem = n-(numFriends-1)
        i = 0
        j = 1
        
        while j<n:
            k = 0
            while j+k<n and word[i+k] == word[j+k]:
                k+=1
            if j+k<n and word[j+k]>word[i+k]:
                i = max(i+k+1,j)
                j = i+1
            else:
                j = j+k+1
        return word[i:min(i+rem,n)]
                    
