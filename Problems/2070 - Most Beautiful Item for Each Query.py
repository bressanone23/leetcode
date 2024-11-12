class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        import heapq
        tar = sorted((q, i) for i, q in enumerate(queries))

        heapq.heapify(items)
        res = [0]*len(queries)
        temp = 0
        for pair in tar:
            while items and items[0][0] <= pair[0]:
                temp = max(temp, heapq.heappop(items)[1])
            res[pair[1]] = temp

        return res
