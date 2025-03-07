class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        pool = [None, False] + [True]*right

        for i in range(2,int(sqrt(right))+1):
            if pool[i]:
                for j in range(i+i,right+1,i):
                    pool[j] = False

        prime = [i for i in range(left,right+1) if pool[i]]
        res = [-1,-1]
        temp = float('inf')

        for i in range(1,len(prime)):
            if prime[i] - prime[i-1] < temp:
                temp = prime[i] - prime[i-1]
                if temp == 2 and left > 2:
                    return [prime[i-1],prime[i]]
                res = [prime[i-1],prime[i]]

        return res
