class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def countLess(val: int) -> int:
            res, j = 0, len(nums) - 1
            for i in range(len(nums)):
                #O(n) time complexity because of the i < j condition
                while i < j and nums[i] + nums[j] > val:
                    j -= 1
                res += max(0, j - i)
            return res

        nums.sort()
        return countLess(upper) - countLess(lower - 1)
