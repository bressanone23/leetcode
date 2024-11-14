class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, up = 1, max(piles)

        while lo < up:
            mid = (lo + up)//2
            needed = sum(math.ceil(p/mid) for p in piles)
            if needed > h:
                lo = mid + 1
            else:
                up = mid
        return lo
