class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # p = [i for i in range(1,n+1)]
        # index = 0
        # while len(p) > 1:
        #     temp = (index + k - 1) % len(p)
        #     p.pop(temp)
        #     index = temp
        #     #print(p)
        # return p[-1]

        res = 0
        for len_p in range(2, n + 1):
            res = (res + k) % len_p
        return res + 1
