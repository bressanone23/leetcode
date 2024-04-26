class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # n = len(matrix)

        # dp = [[float('inf')]*(n+1) for _ in range(n+1)]
        # for i in range(n+1):
        #     dp[0][i] = 0

        # for i in range(n):
        #     matrix[i].insert(0,0)
        # matrix.insert(0,[0]*(n+1))

        # for i in range(1,n+1):
        #     for j in range(1,n+1):
        #         if j < n:
        #             dp[i][j] = matrix[i][j] + min(dp[i-1][j],dp[i-1][j-1],dp[i-1][j+1])
        #         else:
        #             dp[i][j] = matrix[i][j] + min(dp[i-1][j],dp[i-1][j-1])

        # #print(dp)
        # return min([x for x in dp[n]])


        n = len(matrix)
        dp = [[float('inf')]*n for _ in range(n)]
        for i in range(n):
            dp[0][i] = matrix[0][i]

        for i in range(1,n):
            for j in range(n):
                dp[i][j] = dp[i-1][j]
                if j >= 1:
                    dp[i][j] = min(dp[i][j],dp[i-1][j-1])
                if j < n-1:
                    dp[i][j] = min(dp[i][j],dp[i-1][j+1])
                dp[i][j] += matrix[i][j]

        print(dp)
        return min([x for x in dp[-1]])
