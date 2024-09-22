class Solution:
    def findMinDifference(self, t: List[str]) -> int:
        if len(set(t)) < len(t): return 0

        t.sort()
        res = []

        end = 60*(int(t[-1].split(':')[0]) - int(t[0].split(':')[0])) + int(t[-1].split(':')[1]) - int(t[0].split(':')[1])
        if end > 60*12:
                end -= 24*60
        res.append(abs(end))
        for i in range(1,len(t)):
            temp = 60*(int(t[i].split(':')[0]) - int(t[i-1].split(':')[0])) + int(t[i].split(':')[1]) - int(t[i-1].split(':')[1])
            if temp > 60*12:
                temp -= 24*60
            res.append(abs(temp))
        return min(res)
