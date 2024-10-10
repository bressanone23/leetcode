class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        # res = 0

        # stack = []
        # for i in range(len(A))[::-1]:
        #     #print([A[i], i])
        #     if not stack or A[i] > stack[-1][0]:
        #         stack.append([A[i], i])
        #     else:
        #         j = stack[bisect.bisect(stack, [A[i], i])][1]
        #         res = max(res, j - i)
        #     #print(stack, res)
        # return res


        s = []
        res = 0
        for i, a in enumerate(A):
            if not s or A[s[-1]] > a:
                s.append(i)

        #print(s)
        for j in range(len(A))[::-1]:
            while s and A[s[-1]] <= A[j]:
                res = max(res, j - s.pop())
        return res
