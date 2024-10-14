class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        pool = []
        heapq.heapify(pool)

        for x in nums:
            heapq.heappush(pool,-x)

        res = 0
        for i in range(k):
            res += -pool[0]
            heapq.heapreplace(pool, math.floor(pool[0]/3))
            #print(pool)

        return res
