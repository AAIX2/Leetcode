# Approach (Using Heap)
# T.C : O(m*n log(m*n))
# S.C : O(m*n)

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        n = len(heightMap)
        m = len(heightMap[0])
        heap = []
        vis = [[0 for i in range(m)]for i in range(n)]
        for i in range(n):
            for j in range(m):
                if i == 0 or i == n-1 or j == 0 or j == m-1:
                    heap.append([heightMap[i][j],i,j])
                    vis[i][j] = 1
        heapq.heapify(heap)
        dir_x,dir_y = [0,0,-1,1],[-1,1,0,0]
        totalVolume = 0
        
            
        while heap:
            hei,x,y = heapq.heappop(heap)
            for d in range(4):
                new_x,new_y = x+dir_x[d],y+dir_y[d]
                if new_x>=0 and new_x<n and new_y>=0 and new_y<m and not vis[new_x][new_y]:
                    vis[new_x][new_y] = 1
                    newHeight = max(hei,heightMap[new_x][new_y])
                    heapq.heappush(heap,[newHeight,new_x,new_y])
                    totalVolume+=max(hei-heightMap[new_x][new_y],0)
        return totalVolume

        