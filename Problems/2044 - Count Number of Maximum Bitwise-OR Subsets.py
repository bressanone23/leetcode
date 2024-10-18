class Solution:
    def countMaxOrSubsets(self, A: List[int]) -> int:
        dp = collections.Counter([0])

        for a in A:
            for k, v in list(dp.items()):
                dp[k | a] += v
            #print(dp)

        return dp[max(dp)]
