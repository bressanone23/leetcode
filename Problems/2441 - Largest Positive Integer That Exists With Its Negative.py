class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        dic = set(nums)
        res = -1
        for x in dic:
            if -x in dic:
                res = max(res,abs(x))
        #print(dic)
        return res
