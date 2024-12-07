# Using modified Djikstra's Algo
# Since we know we want the minimum time to visit the last cell so we can see we will always greedily choose the minimum time possible 
# THe main crux of this problem lies in the part that when we reach a step where we cannot advance further we will have to waste some time moving back and forth to the last visited cells until we reach the min time possible to go further
class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        # Edge Case - In case we cannot even move form our first cell so we will return -1
        if grid[0][1]>1 and grid[1][0]>1:
            return -1
        vis = set()
        dir_x,dir_y = [0,0,-1,1],[-1,1,0,0]
        heap = [[0,0,0]]
        while heap:
            t,i,j = heapq.heappop(heap)
            if i == n-1 and j == m-1:
                return t
            if (i,j) in vis:
                continue
            vis.add((i,j))
            for d in range(4):
                new_x,new_y = i+dir_x[d],j+dir_y[d]
                if new_x>=0 and new_x<n and new_y>=0 and new_y<m and (new_x,new_y) not in vis:
                    # We can move further since the condition satisfies
                    if t+1>=grid[new_x][new_y]:
                        heapq.heappush(heap,[t+1,new_x,new_y])
                    # We cannot move further so if the diff between the next cell and cur time 
                    # If the diff is odd then the time will be the next cell time else the time will be next cell time +1 (We can see this by take a cell and try to move back and forth to the prev cell so for every back and forth it will take 2 sec)
                    else:
                        tDiff = grid[new_x][new_y]-t
                        if tDiff%2:
                            heapq.heappush(heap,[grid[new_x][new_y],new_x,new_y])
                        else:
                            heapq.heappush(heap,[grid[new_x][new_y]+1,new_x,new_y])
                         
        return -1
# Time Complecity- O(n*mlog(n*m))
# Space Complexity- O(n*m)