# Approach (simple traverse and check)
# T.C : O(n)
# S.C : O(1)

class Solution:
    def isValid(self, word: str) -> bool:
        if len(word)<3:
            return False
        vowel = 0
        conso = 0
        
        for ch in word:
            if ch.isalpha():
                if ch in {"a","e","i","o","u","A","E","I","O","U"}:
                    vowel+=1
                else:
                    conso+=1
            elif ch.isdigit():
                continue
            else:
                return False
        if vowel and conso:
            return True
        return False
        