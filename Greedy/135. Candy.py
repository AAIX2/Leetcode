# Approach-1
# T.C : O(n)
# S.C : O(2*n) ~ O(n) But using 2 Extra Arrays

from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        
        L2R = [1] * n
        R2L = [1] * n
        
        # First pass: compare with left neighbor
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                L2R[i] = L2R[i - 1] + 1
        
        # Second pass: compare with right neighbor
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                R2L[i] = R2L[i + 1] + 1
        
        # Calculate the total candies required
        result = sum(max(L2R[i], R2L[i]) for i in range(n))
        
        return result


# Approach-2 
# T.C : O(n)
# S.C : O(n) - Using only 1 Extra Array

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        r = [0]*n
        # We check only for the left neighbors for now
        for i in range(n):
            if i == 0 or ratings[i]<=ratings[i-1]:
                r[i] = 1
            else:
                r[i] = r[i-1]+1
        
        # Check for right neighbor
        res = max(1,r[-1])
        prev = 1
        for i in range(n-2,-1,-1):
            if ratings[i]<=ratings[i+1]:
                prev = 1
                res += max(r[i],prev)
            else:
                prev = prev+1
                res += max(r[i],prev)
        return res
    
# Approach-3
# T.C : O(n)
# S.C : O(1)

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        # Using Concept of slope
        peak,down = 0,0
        res = 1
        i = 1
        while i<n:
            # For flat surface
            if ratings[i] == ratings[i-1]:
                res+=1
                i+=1
                continue
            # we add peak since its increasing and we assign the value +1 than the prev guy
            peak = 1
            while i<n and ratings[i]>ratings[i-1]:
                peak+=1
                res+=peak
                i+=1
            # This is for the dec slope where the current guy is smaller but we assign like 1,2,3,4,5,... since we dont care abt the assignment of candies but the sum so even we do it like the above order answer wont change
            down = 0
            while i<n and ratings[i]<ratings[i-1]:
                down+=1
                res+=down
                i+=1
            
            # Check if the peak was correct or not since there might be a case the peak is smaller than the down since peak is dependent upon the max of either sides the number of smaller eleemnts 
            if peak<down+1:
                res+=(down+1-peak)
        return res
            
            


            
