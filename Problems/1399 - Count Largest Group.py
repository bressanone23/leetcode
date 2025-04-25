class Solution:
    def countLargestGroup(self, n: int) -> int:
        dic = defaultdict(int)
        for i in range(1,n+1):
            dic[sum([int(x) for x in str(i)])] += 1

        #print(dic)
        res = 0
        new = sorted(dic.values())[-1]
        for value in dic.values():
            if value == new:
                res+=1

        return res
