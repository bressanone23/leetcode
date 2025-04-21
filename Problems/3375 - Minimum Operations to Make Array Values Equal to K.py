class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        pool = list(set(nums))
        if k > min(pool):
            return -1
        return len(pool) - 1 if k in pool else len(pool)
