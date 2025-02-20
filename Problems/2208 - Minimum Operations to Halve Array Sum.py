class Solution:
    def halveArray(self, nums: List[int]) -> int:
        new = [-x for x in nums]
        heapq.heapify(new)
        tar = sum(nums)
        total = sum(nums)
        res = 0

        while tar >  total/2:
            res += 1
            temp = -heapq.heappop(new)
            tar  -= temp/2
            heapq.heappush(new,-temp/2)

        return res
