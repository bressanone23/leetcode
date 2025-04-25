class Solution:
    def countInterestingSubarrays(self, A: List[int], m: int, k: int) -> int:
        res = 0
        count = Counter({0: 1})
        dp = 0

        for x in A:
            dp = (dp + ((x % m) == k)) % m
            #print(count[(dp - k) % m])
            res += count[(dp - k) % m]
            count[dp] += 1

            #print(count)
        #print(dp)

        return res

        
