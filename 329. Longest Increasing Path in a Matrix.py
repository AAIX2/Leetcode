# Using DFS
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        dir_x,dir_y = [0,0,-1,1],[-1,1,0,0]
        dp = [[-1 for i in range(m)]for i in range(n)]
        # dp[i][j] represents the longest increasing path starting at this cell (i,j)
        def solve(i,j):
            if dp[i][j]!=-1:
                return dp[i][j]
            # Every cell in itself is an increasing path so the length will be 1
            ans = 1
            for d in range(4):
                new_x,new_y = i+dir_x[d],j+dir_y[d]
                if new_x>=0 and new_x<n and new_y>=0 and new_y<m and matrix[new_x][new_y]>matrix[i][j]:
                    ans = max(ans,1+solve(new_x,new_y))
            
            dp[i][j] = ans
            return dp[i][j]
        maxi = 1
        for i in range(n):
            for j in range(m):
                maxi = max(maxi,solve(i,j))
        return maxi
    # Time Complexity- O(n*m)
    # Space Complexity- O(n*m)