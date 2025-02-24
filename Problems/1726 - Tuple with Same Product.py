class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:

        res = 0
        nums = list(set(nums))
        pool = defaultdict(int)
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                pool[nums[i]*nums[j]] += 1

        for value in pool.values():
            res += value*(value-1)//2

        return res*8
