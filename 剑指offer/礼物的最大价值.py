class Solution:
    def maxValue(self, grid):
        m = len(grid)
        n = len(grid[0])
        if m == n == 1:
            return grid[0][0]
        dp = [0]*m
        for i in range(m):
            dp[i] = n*[0]
        dp[0][0] = grid[0][0]
        for i in range(m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for i in range(n):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = max(dp[i-1][j],dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]
a = Solution()
a.maxValue([
  [1,3,1],
  [1,5,1],
  [4,2,1]
])