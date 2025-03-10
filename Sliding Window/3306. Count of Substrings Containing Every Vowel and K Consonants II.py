# Approach (Sliding Window Khandani Template)
# T.C : O(2*n) ~ O(n)
# S.C : O(n)


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        v = {"a","e","i","o","u"}
        nextInd = [n]*n
        last = n
        for i in range(n-1,-1,-1):
            nextInd[i] = last
            if word[i] not in v:
                last = i
            
        cnt = 0
        i = j = 0
        vowels = defaultdict(int)
        consonants = 0
        while j<n:
            if word[j] in v:
                vowels[word[j]]+=1
            else:
                consonants+=1
            while i<j and consonants>k:
                if word[i] in v:
                    vowels[word[i]]-=1
                    if not vowels[word[i]]:
                        del vowels[word[i]]
                else:
                    consonants-=1
                i+=1
            while len(vowels) == 5 and consonants == k:
                cnt+=(nextInd[j]-j)
                if word[i] in v:
                    vowels[word[i]]-=1
                    if not vowels[word[i]]:
                        del vowels[word[i]]
                else:
                    consonants-=1
                
                i+=1
            j+=1
       
                
        return cnt


# Approach (Sliding Window Khandani Template)
# T.C : O(2*n) ~ O(n)
# S.C : O(1)


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        v = {"a","e","i","o","u"}
            
        cnt = 0
        i = j = 0
        right = 0
        vowels = defaultdict(int)
        consonants = 0
        while j<n:
            if word[j] in v:
                vowels[word[j]]+=1
            else:
                consonants+=1
            while right<j and consonants>k:
                if word[right] in v:
                    vowels[word[right]]-=1
                    if not vowels[word[right]]:
                        del vowels[word[right]]
                else:
                    consonants-=1
                right+=1
                i = right
            while len(vowels) == 5 and consonants == k:
                if word[right] in v:
                    if vowels[word[right]] - 1 >0:
                        vowels[word[right]]-=1
                        right+=1
                    else:
                        break
                else:
                    break
                
            if len(vowels) == 5 and consonants == k:
                cnt+=(right-i+1)
            j+=1
       
                
        return cnt
    
# Approach (Sliding Window Khandani Template)
# T.C : O(2*n) ~ O(n)
# S.C : O(1)

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        v = {"a","e","i","o","u"}
        def cntOfAtLeastK(k):
            cnt = 0
            i = j = 0
            vowels = defaultdict(int)
            consonants = 0
            while j<n:
                if word[j] in v:
                    vowels[word[j]]+=1
                else:
                    consonants+=1
                while len(vowels) == 5 and consonants >= k:
                    cnt+=(n-j)
                    if word[i] in v:
                        vowels[word[i]]-=1
                        if not vowels[word[i]]:
                            del vowels[word[i]]
                    else:
                        consonants-=1
                    i+=1
                        
                j+=1
            return cnt
       
                
        return cntOfAtLeastK(k)-cntOfAtLeastK(k+1)

