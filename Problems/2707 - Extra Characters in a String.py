class Solution:
    def minExtraChar(self, s: str, d: List[str]) -> int:
        dp = [0] * (len(s)+1)  # Initialize an array to store the minimum extra characters.
        n = len(s)

        for i in range(n - 1, -1, -1):
            dp[i] = 1 + dp[i + 1]  # Initialize with one extra character.

            for w in d:
                if i + len(w) <= n and s[i:i + len(w)] == w:
                    dp[i] = min(dp[i], dp[i + len(w)])  # Update if a word in the dictionary is found.
                #print(i,w,dp)
        return dp[0] 
