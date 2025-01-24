# Approach - 1 (Brute Force)
# T.C : O((m*n) * s*(m+n)) , where s = arr.size() which is (m*n)
# S.C : O(m*n)

class Solution:

    def checkRowPainted(self, mat, row):
        for col in range(len(mat[0])):
            if mat[row][col] > 0:  # not painted
                return False
        return True

    def checkColPainted(self, mat, col):
        for row in range(len(mat)):
            if mat[row][col] > 0:  # not painted
                return False
        return True

    def firstCompleteIndex(self, arr, mat):
        m = len(mat)
        n = len(mat[0])

        # Create a dictionary to store value to cell-coordinate [i][j]
        mp = {}
        for i in range(m):
            for j in range(n):
                val = mat[i][j]
                mp[val] = (i, j)

        for i, val in enumerate(arr):
            row, col = mp[val]
            mat[row][col] *= -1  # painted

            if self.checkRowPainted(mat, row) or self.checkColPainted(mat, col):
                return i

        return -1
    
# Approach - 2 (Better Approach)
# T.C : O(m*n)
# S.C : O((m*n) + m + n)


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        row = [0]*n
        col = [0]*m
        coor = [0]*((n*m)+1)
        for i in range(n):
            for j in range(m):
                coor[mat[i][j]] = [i,j]
        
        for ind,num in enumerate(arr):
            i,j = coor[num]
            row[i]+=1
            col[j]+=1
            
            if row[i] == m or col[j] == n:
                return ind

        
# Approach - 3 (Best Approach)
# T.C : O(m*n)
# S.C : O(m*n)


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        numInd = defaultdict(int)
        for i in range(n*m):
            numInd[arr[i]] = i
        res = float('inf')
        for i in range(n):
            lastSeen = float('-inf')
            for j in range(m):
                lastSeen = max(lastSeen,numInd[mat[i][j]])
            res = min(res,lastSeen)
        for i in range(m):
            lastSeen = float('-inf')
            for j in range(n):
                lastSeen = max(lastSeen,numInd[mat[j][i]])
            res = min(res,lastSeen)
        return res

        
        
