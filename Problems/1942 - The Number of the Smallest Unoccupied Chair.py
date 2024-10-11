class Solution:
    def smallestChair(self, times: List[List[int]], k: int) -> int:
        for i in range(len(times)):
            times[i].append(i)

        pool = sorted(times)

        seen = []
        available_index = [i for i in range(len(pool))]
        heapq.heapify(seen)
        heapq.heapify(available_index)


        for x in pool:
            if not seen:
                if x[2] == k:
                    return 0

                heapq.heappush(seen,[x[1],heapq.heappop(available_index)])
            else:
                if x[2] == k:
                    res = float('inf')
                    temp = 0
                    while temp < len(seen):
                        if seen[temp][0] <= x[0]:
                            res= min(res,seen[temp][1])
                        temp += 1

                    return min(res,heapq.heappop(available_index))

                if seen[0][0] > x[0]:
                    heapq.heappush(seen,[x[1],heapq.heappop(available_index)])

                else:
                    while seen and seen[0][0] <= x[0]:
                        heapq.heappush(available_index, heapq.heappop(seen)[1])
                    heapq.heappush(seen,[x[1],heapq.heappop(available_index)])
