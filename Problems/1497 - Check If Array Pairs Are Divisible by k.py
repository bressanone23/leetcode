class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        if sum(arr) % k != 0:
            return False

        pool = defaultdict(int)

        for x in arr:
            pool[x % k] += 1

        #print(pool)

        for key in pool.keys():
            if (k - key) in pool:
                if pool[k - key] != pool[key]:
                    return False
            else:
                if pool[key] % 2 == 1:
                    return False
                if key != 0 and key*2 != abs(k):
                    return False
        return True
