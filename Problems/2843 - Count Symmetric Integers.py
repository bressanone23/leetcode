class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0
        while low <= high:
            if len(str(low)) % 2 != 0:
                low =  int('1' + '0' * len(str(low)))
            else:
                p = str(low)
                if sum([int(k) for k in p[:len(p)//2]]) == sum([int(k) for k in p[len(p)//2:]]):
                    res += 1
                low += 1
        return res
