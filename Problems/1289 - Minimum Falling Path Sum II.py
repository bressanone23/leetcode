class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        dp = [[float('inf')]*n for _ in range(n)]

        for i in range(n):
            dp[0][i] = matrix[0][i]

        for i in range(1,n):
            for j in range(n):
                temp = sorted(dp[i-1])[:2]
                #print(temp)
                if dp[i-1][j] == temp[0]:
                    dp[i][j] = matrix[i][j] + temp[1]
                else:
                    dp[i][j] = matrix[i][j] + temp[0]

        return min([x for x in dp[-1]])
