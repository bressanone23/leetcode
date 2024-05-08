class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        dic = defaultdict(int)
        n = len(score)
        for i, x in enumerate(score):
            dic[x] = i
        #print(dic)

        res = [0]*n

        heapify(score)
        while score:
            res[dic[heapq.heappop(score)]] = str(len(score))
            #print(res)

        for i in range(n):
            if res[i] == '1':
                res[i] = "Gold Medal"
            if res[i] == '2':
                res[i] = "Silver Medal"
            if res[i] == '3':
                res[i] = "Bronze Medal"

        return res
