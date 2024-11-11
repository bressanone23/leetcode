class Solution:
    def makeFancyString(self, s: str) -> str:
        res = set()
        for i,x in enumerate(s):
            if i == 0:
                last = x
                count = 1
            else:
                if x == last and count == 2:
                    res.add(i)
                elif x == last and count < 2:
                    count += 1
                elif x != last:
                    last = x
                    count = 1
        return "".join([s[i] for i in range(len(s)) if i not in res])
