class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # mini = 0

        # for i,x in enumerate(customers):
        #     if grumpy[i] == 0:
        #         mini += x
        # res = mini

        # for i in range(len(customers)-minutes+1):
        #     temp = mini
        #     for j in range(i,i+minutes):
        #         if grumpy[j] == 1:
        #             temp += customers[j]
        #     res = max(res,temp)
        # return res

        mini = 0

        for i,x in enumerate(customers):
            if grumpy[i] == 0:
                mini += x
                customers[i] = 0

        res = 0
        current = 0
        for i,x in enumerate(customers):
            current += customers[i]
            if i >= minutes:
                current -= customers[i-minutes]
            res = max(res,current)

        return res + mini
