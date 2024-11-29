# Using Djisktra's Algo
# We can visualise the grid in terms of a graph where the cells are nodes and to reach a cell with an obstacle we will take a wt of 1 since its an obstacle which can be considered as an edge wt. So basically we are trying to find out the path with minimum obstacles from source to target which implies to djkistra's algo. 

# BFS will give TLE beacuse it will explore all the paths since all the wt will be processed sequentially rather than what we do in a heap. 
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dir_x = [0,0,-1,1]
        dir_y = [-1,1,0,0]
        obs = [[float('inf') for i in range(m)]for i in range(n)]
        heap = [[0,0,0]]
        obs[0][0] = 0
        while heap:
            obstacles,i,j = heapq.heappop(heap)
            if i == n-1 and j == m-1:
                return obstacles
            for d in range(4):
                new_x,new_y = i+dir_x[d],j+dir_y[d]
                if new_x>=0 and new_x<n and new_y>=0 and new_y<m:
                    if grid[new_x][new_y] == 1:
                        if obs[new_x][new_y]>1+obstacles:
                            obs[new_x][new_y] = 1+obstacles
                            heapq.heappush(heap,[1+obstacles,new_x,new_y])
                    else:
                        if obs[new_x][new_y]>obstacles:
                            obs[new_x][new_y] = obstacles
                            heapq.heappush(heap,[obstacles,new_x,new_y])
            
# Time Complexity- O(E log V) or O(n*mlog(n*m)) since at the worst case edges can be n*m and vertices are n*m
# Space Complexity- O(n*m)


# Using 0-1 BFS

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dir_x = [0,0,-1,1]
        dir_y = [-1,1,0,0]
        obs = [[float('inf') for i in range(m)]for i in range(n)]
        q = deque([[0,0,0]])
        obs[0][0] = 0
        while q:
            i,j,obstacles = q.popleft()
            for d in range(4):
                new_x,new_y = i+dir_x[d],j+dir_y[d]
                if new_x>=0 and new_x<n and new_y>=0 and new_y<m and obs[new_x][new_y] == float('inf'):
                    if grid[new_x][new_y] == 1:
                        obs[new_x][new_y] = 1+obstacles
                        q.append([new_x,new_y,1+obstacles])
                    else:
                        obs[new_x][new_y] = obstacles
                        q.appendleft([new_x,new_y,obstacles])
            
        return obs[n-1][m-1]

# Time Complexity- O(n*m)
# Space Complexity- O(n*m)
