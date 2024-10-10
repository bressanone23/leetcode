class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = set()
        pool = []
        for i,c in enumerate(s):
            if c == '(':
                pool.append((c,i))
            elif c == ')':
                if pool:
                    pool.pop()
                else:
                    #pool.append((c,i))
                    res.add(i)

        if pool:
            for pair in pool:
                res.add(pair[1])
        #print(res)
        return "".join([c for i,c in enumerate(s) if i not in res])
