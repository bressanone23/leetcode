class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        #dp[i][j] = length of the side of the largest square with (i,j) as it bottom right corner.

        m,n = len(matrix), len(matrix[0])
        dp = [[0]*(n+1) for _ in range(m+1)]

        # [["1","0","1","0","0"],
        # ["1","0","1","1","1"],
        # ["1","1","1","1","1"],
        # ["1","0","0","1","0"]]
        for x in matrix:
            x.insert(0,"0")
        matrix.insert(0,["0"]*(n+1))

        res = 0
        for i in range(1,m+1):
            for j in range(1,n+1):
                if matrix[i][j] == "1":
                    dp[i][j] = min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1]) + 1
                    res = max(res,dp[i][j])
        return res**2
