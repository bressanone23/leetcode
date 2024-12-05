class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = float('Inf')
        for i in range(len(nums)-1):
            res = min(res,max(nums[-1] - k,nums[i] + k) - min(nums[0] + k,nums[i+1] - k))
        return min(res, nums[-1]-nums[0])
