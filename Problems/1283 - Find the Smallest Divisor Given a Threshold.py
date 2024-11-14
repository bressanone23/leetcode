class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        lo, up = 1, max(nums)

        while lo < up:
            mid = (lo + up)//2
            if sum(math.ceil(a/mid) for a in nums) > threshold:
                lo = mid + 1
            else:
                up = mid
        return lo
