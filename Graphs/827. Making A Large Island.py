# Approach - 1 - Brute Force DFS (you can do BFS as well)
# T.C : O(n^4)
# S.C : O(n^2)


class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    def DFS(self, grid, i, j, visited):
        if i < 0 or i >= self.m or j < 0 or j >= self.n or grid[i][j] == 0 or visited[i][j]:
            return 0
        
        visited[i][j] = True
        count = 1
        
        for dir_x, dir_y in self.directions:
            count += self.DFS(grid, i + dir_x, j + dir_y, visited)
        
        return count
    
    def findLargestIsland(self, grid):
        self.m = len(grid)
        self.n = len(grid[0])
        max_area = 0
        
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 0:  # Try converting each 0 to 1
                    grid[i][j] = 1
                    
                    visited = [[False] * self.n for _ in range(self.m)]
                    largest = 0
                    
                    for x in range(self.m):
                        for y in range(self.n):
                            if grid[x][y] == 1 and not visited[x][y]:
                                largest = max(largest, self.DFS(grid, x, y, visited))
                    
                    max_area = max(max_area, largest)
                    grid[i][j] = 0  # Backtrack
        
        return self.m * self.n if max_area == 0 else max_area  # If the grid was full of 1s
    
    def largestIsland(self, grid):
        return self.findLargestIsland(grid)



# Approach - 2 - Brute Force DFS (you can do BFS as well)
# T.C : O(n^4)
# S.C : O(n^2)


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        dir_x,dir_y = [0,0,-1,1],[-1,1,0,0]
        def dfs(i,j,vis):
            vis.add((i,j))
            ans = 0
            for d in range(4):
                new_x,new_y = i+dir_x[d],j+dir_y[d]
                if new_x>=0 and new_x<n and new_y>=0 and new_y<m and grid[new_x][new_y] == 1 and (new_x,new_y) not in vis:
                    ans+=1+dfs(new_x,new_y,vis)
            return ans
        maxArea = 0
        cntOfOne = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    vis = set()
                    maxArea = max(maxArea,1+dfs(i,j,vis))
                else:
                    cntOfOne+=1
        return maxArea if maxArea else cntOfOne
    

# Approach - 3  - Optimal DFS (You can use BFS as well)
# T.C : O(m*n)
# S.C : O(m*n)

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        dir_x,dir_y = [0,0,-1,1],[-1,1,0,0]
        def dfs(i,j,color):
            grid[i][j] = color
            ans = 1
            for d in range(4):
                new_x,new_y = i+dir_x[d],j+dir_y[d]
                if new_x>=0 and new_x<n and new_y>=0 and new_y<m and grid[new_x][new_y] == 1:
                    ans+=dfs(new_x,new_y,color)
            return ans
        maxArea = 0
        islandToArea = defaultdict(int)
        color = 2
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    a = dfs(i,j,color)
                    islandToArea[color] = a
                    color+=1
                    maxArea = max(maxArea,a)       
                
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    v = set()
                    area = 0
                    for d in range(4):
                        new_x,new_y = i+dir_x[d],j+dir_y[d]
                        if new_x>=0 and new_x<n and new_y>=0 and new_y<m and grid[new_x][new_y] !=0:
                            if grid[new_x][new_y] not in v:
                                v.add(grid[new_x][new_y])
                                area+=islandToArea[grid[new_x][new_y]]
                    maxArea = max(maxArea,area+1)


        return maxArea 
    

# Approach - 4  - Optimal DSU 
# T.C : O(m*n)
# S.C : O(m*n)


class DisjointSet:
    def __init__(self,n):
        self.parent = [i for i in range(n+1)]
        self.size = [1]*(n+1)

    def findPar(self,node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findPar(self.parent[node])
        return self.parent[node]
    def UnionBySize(self,u,v):
        ulti_u = self.findPar(u)
        ulti_v = self.findPar(v)
        if ulti_u == ulti_v:
            return
        if self.size[ulti_u]<self.size[ulti_v]:
            self.parent[ulti_u] = ulti_v
            self.size[ulti_v]+=self.size[ulti_u]
        else:
            self.parent[ulti_v] = ulti_u
            self.size[ulti_u]+=self.size[ulti_v]
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dsu = DisjointSet(n*m)
        dir_x = [0,0,-1,1]
        dir_y = [-1,1,0,0]
        maxArea = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    ind = i*m+j
                    area = dsu.size[ind]
                    for d in range(4):
                        new_x,new_y = i+dir_x[d],j+dir_y[d]
                        if new_x>=0 and new_x<n and new_y>=0 and new_y<m and grid[new_x][new_y] == 1:
                            newInd = new_x*m+new_y
                            if dsu.findPar(ind)!=dsu.findPar(newInd):
                                dsu.UnionBySize(ind,newInd)
                            area = max(area,dsu.size[dsu.findPar(newInd)])
                    maxArea = max(maxArea,area)
        
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    ind = i*m+j
                    vis = set()
                    area = 0
                    for d in range(4):
                        new_x,new_y = i+dir_x[d],j+dir_y[d]
                        if new_x>=0 and new_x<n and new_y>=0 and new_y<m and grid[new_x][new_y] == 1:
                            newInd = new_x*m+new_y
                            par = dsu.findPar(newInd)
                            if par not in vis:
                                area+=dsu.size[par]
                                vis.add(par)
                    maxArea = max(maxArea,1+area)
        return maxArea    
                                
