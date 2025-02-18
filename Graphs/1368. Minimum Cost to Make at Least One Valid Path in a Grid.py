# Approach-1 (Backtracking DFS to try all paths) - TLE
# T.C : O(4^(m*n))
# S.C : O(m*n)

class Solution:
    def __init__(self):
        self.dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        self.m = 0
        self.n = 0

    def dfs(self, i, j, grid, visited, cost):
        if i == self.m - 1 and j == self.n - 1:  # Reached destination
            return cost

        visited[i][j] = True

        # Explore all directions
        min_cost = float('inf')
        for dir_i in range(4):
            i_ = i + self.dir[dir_i][0]
            j_ = j + self.dir[dir_i][1]

            if 0 <= i_ < self.m and 0 <= j_ < self.n and not visited[i_][j_]:
                next_cost = cost + (1 if (grid[i][j] - 1 != dir_i) else 0)
                min_cost = min(min_cost, self.dfs(i_, j_, grid, visited, next_cost))

        visited[i][j] = False
        return min_cost

    def minCost(self, grid):
        self.m = len(grid)
        self.n = len(grid[0])

        visited = [[False] * self.n for _ in range(self.m)]

        return self.dfs(0, 0, grid, visited, 0)  # Explore all paths by backtracking


# Approach-2 (Dijkstra's Algorithm) - Accepted
# T.C : O((m*n) * log(m*n))
# S.C : O(m*n)


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        def getDir(i,j):
            if grid[i][j] == 1:
                return [i,j+1]
            elif grid[i][j] == 2:
                return [i,j-1]
            elif grid[i][j] == 3:
                return [i+1,j]
            else:
                return [i-1,j]

        heap = [[0,0,0]]
        dir_x = [0,0,-1,1]
        dir_y = [-1,1,0,0]
        minCost = [[float('inf') for i in range(m)]for i in range(n)]
        minCost[0][0] = 0
        while heap:
            cost,i,j = heapq.heappop(heap)
            if i == n-1 and j == m-1:
                return cost
            if minCost[i][j]<cost:
                continue
            intial_dir = getDir(i,j)
            for d in range(4):
                new_x,new_y = i+dir_x[d],j+dir_y[d]
                if new_x>=0 and new_x<n and new_y>=0 and new_y<m:
                    new_cost = cost+(1 if new_x!=intial_dir[0] or new_y!=intial_dir[1] else 0)
                    if minCost[new_x][new_y]>new_cost:
                        minCost[new_x][new_y] = new_cost
                        heapq.heappush(heap,[new_cost,new_x,new_y])


# Approach-3 (0-1 BFS)
# T.C : O((m*n))
# S.C : O(m*n)       
            
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        def getDir(i,j):
            if grid[i][j] == 1:
                return [i,j+1]
            elif grid[i][j] == 2:
                return [i,j-1]
            elif grid[i][j] == 3:
                return [i+1,j]
            else:
                return [i-1,j]

        q = deque([[0,0,0]])
        dir_x = [0,0,-1,1]
        dir_y = [-1,1,0,0]
        minCost = [[float('inf') for i in range(m)]for i in range(n)]
        minCost[0][0] = 0
        while q:
            i,j,cost = q.popleft()
            if i == n-1 and j == m-1:
                return cost
            intial_dir = getDir(i,j)
            for d in range(4):
                new_x,new_y = i+dir_x[d],j+dir_y[d]
                if new_x>=0 and new_x<n and new_y>=0 and new_y<m:
                    
                    if (new_x!=intial_dir[0] or new_y!=intial_dir[1]) and minCost[new_x][new_y]>1+cost:
                        minCost[new_x][new_y] = 1+cost
                        q.append([new_x,new_y,cost+1])
                    elif new_x == intial_dir[0] and new_y == intial_dir[1] and minCost[new_x][new_y]>cost:
                        minCost[new_x][new_y] = cost
                        q.appendleft([new_x,new_y,cost])
        
            
                    
                    
