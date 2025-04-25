class Solution:
    def mostPoints(self, A: List[List[int]]) -> int:
        dp = defaultdict(int)

        # dp[i] = the max_score we can get start from that index
        i = len(A) - 1
        maxscore = 0
        while i >= 0:
            dp[i] = max(dp[i + A[i][1] + 1] +  A[i][0], maxscore)
            maxscore = max(maxscore, dp[i])
            i -= 1
        #print(dp)
        return maxscore
