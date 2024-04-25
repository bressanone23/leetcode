class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        presum = [0]*n
        temp1 = 0
        for i,x in enumerate(s):
            temp1 += (x == '*')
            presum[i] = temp1
        print(presum)


        last = [0]*n
        temp2 = -1
        for i in range(n):
            if s[i] == '|':
                temp2 = i
            last[i] = temp2
        print(last)

        nex = [n-1]*n
        temp3 = n
        for i in range(n-1,-1,-1):
            if s[i] == '|':
                temp3 = i
            nex[i] = temp3
        print(nex)

        res = []
        for q in queries:
            a,b = q[0], q[1]
            x,y = nex[a], last[b]
            print(x,y)
            if x >= a and y <= b and x <=y:
                res.append(presum[y] - presum[x])
            else:
                res.append(0)

        return res
