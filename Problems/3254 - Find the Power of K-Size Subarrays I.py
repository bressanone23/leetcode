class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums

        indicator = [1] + [1 if nums[i] -1 == nums[i-1] else 0 for i in range(1,len(nums))]

        if all(indicator[i] == 1 for i in range(k)):
            res = [nums[k-1]]
        else:
            res = [-1]

        temp = sum(indicator[0:k])

        for j in range(k,len(nums)):
            temp += indicator[j] - indicator[j-k+1]
            if temp == k:
                res.append(nums[j])
            else:
                res.append(-1)
        return res
