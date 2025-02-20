class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        nums.sort()
        new = [sum(int(digit) for digit in str(x)) for x in nums]

        po = defaultdict(list)

        for i,x in enumerate(new):
            po[x].append(i)

        res = -1

        for value in po.values():
            if len(value) > 1:
                res = max(res, nums[value[-1]] + nums[value[-2]])

        return res
