class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp = [1]*(len(nums)+1)
        # for i in range(len(nums)):
        #     for j in range(i):
        #         if nums[j] < nums[i]:
        #             dp[i] = max(dp[i],dp[j] + 1)
        # return max(dp)



        # arr = [nums[0]]                  # <-- 1) initial step

        # for n in nums:                       # <-- 2) iterate through nums
        #     if n > arr[-1]:                  # <--    2a)
        #         arr.append(n)

        #     else:                            # <--    2b)
        #         arr[bisect_left(arr, n)] = n

        # return len(arr)                      # <-- 3) return the length of arr

        def bSearch(arr, target):
            # Lower bound Bsearch
            i = 0
            j = len(arr)
            while i < j:
                mid = (i+j) // 2
                if arr[mid] == target:
                    return mid
                elif arr[mid] < target:
                    i = mid+1
                else:
                    j = mid
            return i

        if not nums:
            return 0

        # Initialize
        dp = [nums[0]]
        for i in range(1, len(nums)):
            index = bSearch(dp, nums[i])
            if index == len(dp):
                # Add: nums[i] is bigger than the candidate
                dp.append(nums[i])
            else:
                # Update: nums[i] is smaller than other
                dp[index] = nums[i]
        return len(dp)
