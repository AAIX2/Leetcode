# Using DFS
class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dir_x = [0,0,-1,1]
        dir_y = [-1,1,0,0]
        
        dp = [[-1 for i in range(m)]for i in range(n)]
        mod = 10**9+7
        def solve(i,j):
            #  dp[i][j] represents number of increasing paths starting at cell (i,j)
            if dp[i][j]!=-1:
                return dp[i][j]
            # Every cell in itself is an increasing path
            ans = 1
            for d in range(4):
                new_x,new_y = i+dir_x[d],j+dir_y[d]
                if new_x>=0 and new_x<n and new_y>=0 and new_y<m and grid[new_x][new_y]>grid[i][j]:
                    ans+=solve(new_x,new_y)
            
            dp[i][j] = ans
            return dp[i][j]
        cnt = 0
        for i in range(n):
            for j in range(m):
                cnt+=solve(i,j)
        return cnt%mod
    # Time Complexity- O(n*m)
    # Space Complexity- O(n*m)