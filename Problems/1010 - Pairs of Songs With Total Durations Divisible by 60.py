def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # n = len(time)
        # res = []
        # for i in range(n):
        #     if time[i] % 60 != 0:
        #         res.append(time[i] % 60)

        # dic = defaultdict(int)
        # final = 0
        # for i,x in enumerate(res):
        #     final += dic[60-x]
        #     dic[x] += 1

        # return final + int((n - len(res))*(n - len(res)-1)/2)



        # deal with number that % 60 == 0 during loop
        dic = defaultdict(int)
        final = 0
        for i,x in enumerate(time):
            final += dic[(60-x)%60]
            dic[x%60] += 1
            print(dic)
        return final 
