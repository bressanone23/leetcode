class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        mask, res = 0, 0

        for i in range(32,-1,-1):
            mask = mask | 1 << i

            found  = set([n & mask for n in nums])

            temp = res | 1 << i

            for f in found:
                if f^temp in found:
                    res = temp
                    break

        return res
