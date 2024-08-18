 class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        temp = 5001
        while l <= r:
            mid = (l+r)//2
            temp = min(nums[mid],temp)
            if nums[mid] < nums[r]:
                r = mid - 1
            else:
                l = mid+1

        return temp
