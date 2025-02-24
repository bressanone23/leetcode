class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        increase, decrease = 1,1
        c1,c2 = 1,1

        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                increase += 1
            else:
                c1 = max(increase,c1)
                increase = 1

            if nums[i] < nums[i-1]:
                decrease += 1
            else:
                c2 = max(decrease,c2)
                decrease = 1

        return max(c1,c2,increase,decrease)
