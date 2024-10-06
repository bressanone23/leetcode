class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        tar = sum(nums) % p

        if tar == 0:
            return 0

        dp = {0: -1}
        cur = 0
        res = n = len(nums)

        for i, x in enumerate(nums):
            cur = (cur + x) % p
            dp[cur] = i

            if (cur - tar) % p in dp:
                res = min(res, i - dp[(cur-tar) % p])

        return res if res < n else -1
