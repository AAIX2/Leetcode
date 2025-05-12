# Approach-1 (Trying all possibilities using 3 for loops for 3 digits)
# T.C : O(n^3 + SlogS), S = total 3 digits even numbers
# S.C : O(S)

from typing import List

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        st = set()
        n = len(digits)
        
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i == j or j == k or i == k:
                        continue
                    num = digits[i] * 100 + digits[j] * 10 + digits[k]
                    if num >= 100 and num % 2 == 0:
                        st.add(num)
        
        return sorted(st)
    

# Approach-2 (Smartly finding valid digits for each position)
# T.C : O(1)
# S.C : O(1)


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        n = len(digits)
        res = []
        freq = [0]*10
        for d in digits:
            freq[d]+=1
        for i in range(1,10):
            if not freq[i]:
                continue
            freq[i]-=1
            for j in range(10):
                if not freq[j]:
                    continue
                freq[j]-=1
                for k in range(0,9,2):
                    if not freq[k]:
                        continue
                    freq[k]-=1
                    res.append(i*100+j*10+k)
                    freq[k]+=1
                freq[j]+=1
            freq[i]+=1
        return res
        

                    
                    