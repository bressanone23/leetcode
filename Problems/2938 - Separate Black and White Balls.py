class Solution:
    def minimumSteps(self, s: str) -> int:
        # black,res = [i for i,x in enumerate(s) if x == '1'], 0
        # n = len(black)
        # end = 0

        # for x in black[::-1]:
        #     res += len(s) - 1 - x - end
        #     end += 1

        # return res
        # 1 0 1 0 0
        # 1 0 0 1 0
        # 1 0 0 0 1
        # 0 1 0 0 1
        # 0 0 1 0 1
        # 0 0 0 1 1


        # Every 0 should be swapped with every 1 before it.
        # So we count numbers of 1 (swaps variable) and when meet next 0 add to result

        res, swaps = 0, 0
        for ch in s:
            if ch == '1':
                swaps += 1
            else:
                res += swaps
        return res
