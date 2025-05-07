# Approach (Using Dijkstra's Algorithm)
# T.C : O(mn log(mn))
# S.C : O(mn)

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n,m = len(moveTime),len(moveTime[0])
        heap = [[0,0,0]]
        dir_x,dir_y = [-1,1,0,0],[0,0,-1,1]
        time = [[float('inf') for i in range(m)]for i in range(n)]
        time[0][0] = 0
        while heap:
            t,x,y = heapq.heappop(heap)
            if x == n-1 and y == m-1:
                return t
            for d in range(4):
                new_x,new_y = x+dir_x[d],y+dir_y[d]
                if new_x>=0 and new_x<n and new_y>=0 and new_y<m:
                    extraTime = moveTime[new_x][new_y]+1 if t<moveTime[new_x][new_y] else t+1
                    if time[new_x][new_y]>extraTime:
                        time[new_x][new_y] = extraTime
                        heapq.heappush(heap,[extraTime,new_x,new_y])
            
        

