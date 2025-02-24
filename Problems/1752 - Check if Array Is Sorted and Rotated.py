class Solution:
    def check(self, nums: List[int]) -> bool:
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                #print(nums[i+1:] + nums[:i+1])
                if (nums[i+1:] + nums[:i+1]) == sorted(nums):
                    return True
                else:
                    return False

        return True
