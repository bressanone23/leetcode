class Solution:
    def largestRectangleArea(self, h: List[int]) -> int:
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


        # n = len(h)
        # next_smaller, prev_smaller = [n]*n,[-1]*n
        # stack = []

        # for i,x in enumerate(h):
        #     while stack and h[stack[-1]] > x:
        #         next_smaller[stack[-1]] = i
        #         stack.pop()
        #     stack.append(i)

        # stack = []
        # for i,x in enumerate(h):
        #     while stack and h[stack[-1]] > x:
        #         stack.pop()
        #     if stack:
        #         prev_smaller[i] = stack[-1]
        #     stack.append(i)

        # res = 0
        # for i,x in enumerate(h):
        #     res = max(res, h[i]*(next_smaller[i] - prev_smaller[i] - 1))


        # return res
