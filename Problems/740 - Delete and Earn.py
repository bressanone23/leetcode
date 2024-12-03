class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = [0]*(max(nums)+1)

        for x in nums:
            points[x] += x

        dp = [0]*len(points)
        dp[1] = points[1]

        for i in range(1,len(points)):
            dp[i] = max(dp[i-1], dp[i-2]+points[i])

        print(points)
        print(dp)
        
        return max(dp)
