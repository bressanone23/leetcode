class Solution:
        def longestIdealString(self, s: str, k: int) -> int:
                #dp[i] = longest subsequence ending at index i that satisfy the requirement
                # n = len(s)
                # dp = [1]*n
                # pre = [-1]*26
        
                # for i in range(n):
                #     for index in range(max(0, ord(s[i]) - ord('a')-k), min(26,ord(s[i]) - ord('a') + k + 1)):
                #         j = pre[index]
                #         if j != -1:
                #             dp[i] = max(dp[i],dp[j] + 1)
                #     pre[ord(s[i]) - ord('a')] = i
        
                # return max(dp)
        
                dp = [0] * 26
                for c in s:
                    i = ord(c) - ord('a')
                    dp[i] = max(dp[max(0, i - k) : min(25, i + k) + 1]) + 1
                return max(dp)
