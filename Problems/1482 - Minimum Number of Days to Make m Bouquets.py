class Solution:
    def minDays(self, A: List[int], m: int, k: int) -> int:
        # TLE
        # if k*m > len(bloom):
        #     return -1
        # pool = [0]*len(bloom)
        # for d in sorted(set(bloom)):
        #     flow = bouq = 0
        #     for a in bloom:
        #         flow = 0 if a > d else flow + 1
        #         if flow >= k:
        #             flow = 0
        #             bouq += 1
        #             if bouq == m:
        #                 return d

        # return -1
            
        if m * k > len(A): return -1
        left, right = 1, max(A)
        while left < right:
            mid = (left + right) // 2
            flow = bouq = 0
            for a in A:
                flow = 0 if a > mid else flow + 1
                if flow >= k:
                    flow = 0
                    bouq += 1
                    if bouq == m: break
            if bouq == m:
                right = mid
            else:
                left = mid + 1
        return left
