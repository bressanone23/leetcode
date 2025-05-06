class Solution:
    def numEquivDominoPairs(self, A: List[List[int]]) -> int:
        seen = defaultdict(int)
        res = 0
        for x in A:
            seen[(min(x[0],x[1]),max(x[0],x[1]))] += 1

        for v in seen.values():
            if v > 1:
                res += v*(v-1)//2

        return res
