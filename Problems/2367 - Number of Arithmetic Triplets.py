class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        seen = set()
        res = 0
        for x in nums:
            if x- diff in seen and x - 2*diff in seen:
                res += 1
            seen.add(x)

        return res
