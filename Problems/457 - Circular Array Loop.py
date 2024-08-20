class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        seen = set()
        for i in range(len(nums)):
            if i in seen:
                next

            temp = set()
            while True:
                if i in temp:
                    return True
                if i in seen:
                    break

                temp.add(i)
                seen.add(i)
                if i  == (i+nums[i])%len(nums) or nums[i]*nums[(i+nums[i])%len(nums)]<0:
                    break
                i = (i+nums[i])%len(nums)

            #print(temp)
        return False
