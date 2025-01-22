# Approach - Using Multi-Source BFS
# T.C : O(m * n) , We will visit all cells once
# S.C : O(m * n), in worst case queue will contain all the cells

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        n = len(isWater)
        m = len(isWater[0])
        q = deque()
        for i in range(n):
            for j in range(m):
                if isWater[i][j] == 1:
                    q.append([i,j,0])
        dir_x,dir_y = [0,0,-1,1],[-1,1,0,0]
        dist = [[0 for i in range(m)]for i in range(n)]
        ans = 0
        while q:
            x,y,h = q.popleft()
            for d in range(4):
                new_x,new_y = x+dir_x[d],y+dir_y[d]
                if new_x>=0 and new_x<n and new_y>=0 and new_y<m and isWater[new_x][new_y] == 0 and dist[new_x][new_y] == 0:
                    dist[new_x][new_y] = h+1
                    q.append([new_x,new_y,h+1])
        return dist