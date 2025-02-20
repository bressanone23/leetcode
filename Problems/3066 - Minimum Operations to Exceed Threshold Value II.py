class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        res = 0

        while True:
            t1 = heapq.heappop(nums)
            if t1 < k:
                res += 1
                t2 = heapq.heappop(nums)
                print(t1,t2)
                heapq.heappush(nums,(min(t1, t2) * 2 + max(t1, t2)))
            else:
                return res
