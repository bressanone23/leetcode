class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        pool = defaultdict(int)
        for i, x in enumerate(nums[::-1]):
            pool[x] += 1
            #print(pool,i)
            if pool[x] > 1:
                return ceil((len(nums) - i)/3)
        return 0
