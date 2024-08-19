class Solution:
    def smallestNumber(self, p: str) -> str:
        # p = 'I' + p
        # res = []
        # count = 'I'
        # for x in p[1:]:
        #     if x != 'I':
        #         count += x
        #     else:
        #         res.append(count)
        #         count = 'I'
        # res.append(count)
        # #print(res)

        # fi = ''
        # candidates = [1,2,3,4,5,6,7,8,9]
        # for s in res:
        #     if len(s) == 1:
        #         fi += str(candidates.pop(0))
        #     else:
        #         for i in range(len(s)):
        #             fi += str(candidates.pop(len(s)-i-1))
        # return fi

        res = []
        for i,c in enumerate(p + 'I', 1):
            if c == 'I':
                res += range(i, len(res), -1)
            #print(res)
        return ''.join(map(str,res))
