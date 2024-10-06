class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        pool = defaultdict(int)
        n = len(skill)
        if sum(skill)*2 % n != 0:
            return -1
        tar = sum(skill)*2//n

        res = 0
        for x in skill:
            if x >= tar:
                return -1

            if (tar-x) in pool and pool[tar - x] > 0 :
                res += x*(tar - x)
                pool[tar - x] -= 1
            else:
                pool[x] += 1
            #print(res)

        #print(pool)

        return res if all(x == 0 for x in pool.values()) else -1
