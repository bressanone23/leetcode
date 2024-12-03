class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def maxRect(h):
            q = []
            res = 0
            h.insert(len(h),0) # make sure stack is empty after iteration if the stack is increasing
            h.insert(0,0) # make sure stack always has 0
            for i,x in enumerate(h):
                while q and x < h[q[-1]]:
                    base = h[q.pop()]
                    # i is the location of nextsmaller
                    # q[-1] is the location of the prevsmaller
                    #print(i,q[-1],base, i - q[-1] - 1)
                    res = max(res, base*(i - q[-1] - 1))

                q.append(i)
            return res

        tar = 0
        m = len(matrix)
        n = len(matrix[0])
        hist = [0]*n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    hist[j] += 1
                else:
                    hist[j] = 0
            #print(hist)
            tar = max(tar, maxRect(hist.copy()))
        return tar
                    
