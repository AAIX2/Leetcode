# Approach - 1 (Brute Force)
# T.C : O((m*n) * (m+n))
# S.C : O(1)


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0]) if num_rows > 0 else 0
        communicable_servers_count = 0

        # Traverse through the grid
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == 1:
                    can_communicate = False

                    # Check for communication in the same row
                    for other_col in range(num_cols):
                        if other_col != col and grid[row][other_col] == 1:
                            can_communicate = True
                            break

                    # If a server was found in the same row, increment
                    # communicable_servers_count
                    if can_communicate:
                        communicable_servers_count += 1
                    else:
                        # Check for communication in the same column
                        for other_row in range(num_rows):
                            if other_row != row and grid[other_row][col] == 1:
                                can_communicate = True
                                break

                        # If a server was found in the same column, increment
                        # communicable_servers_count
                        if can_communicate:
                            communicable_servers_count += 1

        return communicable_servers_count
    

# Approach - 2 (Better Approach)
# T.C : O(m*n)
# S.C : O(m+n)


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        rowCnt = [0]*n
        colCnt = [0]*m
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    rowCnt[i]+=1
                    colCnt[j]+=1
        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and (rowCnt[i]>1 or colCnt[j]>1):
                    cnt+=1
        return cnt
    

# Approach - 3 (Another better Approach)
# T.C : O(m*n)
# S.C : O(m+n)


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        aloneRowServers = [-1]*n
        colCnt = [0]*m
        res = 0
        for i in range(n):
            rowCnt = 0
            lastSeen = -1
            for j in range(m):
                if grid[i][j] == 1:
                    colCnt[j]+=1
                    lastSeen = j
                    rowCnt+=1
            if rowCnt>1:
                res+=rowCnt
            else:
                aloneRowServers[i] = lastSeen
        
        for i in range(n):
            if aloneRowServers[i]!=-1 and colCnt[aloneRowServers[i]]>1:
                res+=1

        return res

        
# Approach - 4 (Using DSU)
# T.C : O(m*n+(n+m))
# S.C : O(m+n)

class DisjointSet:
    def __init__(self,n):
        self.parent = [i for i in range(n+1)]
        self.size = [1]*(n+1)
    def getPar(self,node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.getPar(self.parent[node])
        return self.parent[node]
    def UnionBySize(self,u,v):
        ulti_u,ulti_v = self.getPar(u),self.getPar(v)
        if ulti_u == ulti_v:
            return
        if self.size[ulti_u]>= self.size[ulti_v]:
            self.parent[ulti_v] = ulti_u
            self.size[ulti_u]+=self.size[ulti_v]
        else:
            self.parent[ulti_u] = ulti_v
            self.size[ulti_v]+=self.size[ulti_u]
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dsu = DisjointSet(n+m)
        servers = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    if dsu.getPar(i)!=dsu.getPar(n+j):
                        dsu.UnionBySize(i,n+j)
                    else:
                        servers+=1
        cnt = 0
        for i in range(n+m):
            ultiPar = dsu.getPar(i)
            if dsu.size[ultiPar] >2 and i == ultiPar:
                cnt+=dsu.size[i]-1
        return cnt+servers


        

        