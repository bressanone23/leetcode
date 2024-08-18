class Solution:
    def minPathSum(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(n):
            dp[1][i+1] = A[0][i] + dp[1][i]
        for i in range(m):
            dp[i+1][1] = A[i][0] + dp[i][1]

        for i in range(1,m):
            for j in range(1,n):
                dp[i+1][j+1] = min(dp[i][j+1],dp[i+1][j]) + A[i][j]

        return dp[-1][-1]
