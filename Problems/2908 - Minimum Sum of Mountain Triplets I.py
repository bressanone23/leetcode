class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        left, right = [nums[0]], [nums[-1]]

        for x in nums[1:]:
            left.append(min(x,left[-1]))

        for x in nums[::-1][1:]:
            right.append(min(x,right[-1]))

        right = right[::-1]

        #print(left, right)
        res = float('inf')

        for i in range(1, len(nums)-1):
            if left[i] < nums[i] and nums[i] > right[i]:
                res = min(res, left[i] + nums[i] + right[i])

        return res if res != float('inf') else -1
