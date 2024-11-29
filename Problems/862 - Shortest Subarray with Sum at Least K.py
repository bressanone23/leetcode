class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        print(prefix_sum)
        result = n + 1  # Initialize with a value larger than possible answer
        d = deque()

        for i in range(n + 1):
            while d and prefix_sum[i] - prefix_sum[d[0]] >= k:
                result = min(result, i - d.popleft())

            while d and prefix_sum[i] <= prefix_sum[d[-1]]:
                d.pop()

            d.append(i)

        return result if result <= n else -1
