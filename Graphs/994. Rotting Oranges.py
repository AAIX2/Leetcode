# Approach - Using Multi-Source BFS
# T.C : O(m * n) , We will visit all cells once
# S.C : O(m * n), in worst case queue will contain all the cells


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        vis = [[0 for i in range(m)]for i in range(n)]
        q = deque()
        freshCnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    freshCnt+=1
                elif grid[i][j] == 2:
                    q.append([i,j,0])
                    vis[i][j] = 1
        dir_x = [0,0,-1,1]
        dir_y = [-1,1,0,0] 
        res = 0
        while q:
            i,j,time = q.popleft()
            res = time
            for d in range(4):
                new_x,new_y = i+dir_x[d],j+dir_y[d]
                if new_x>=0 and new_x<n and new_y>=0 and new_y<m and grid[new_x][new_y] == 1 and not vis[new_x][new_y]:
                    vis[new_x][new_y] = 1
                    freshCnt-=1
                    q.append([new_x,new_y,time+1])
        return res if freshCnt == 0 else -1
        
