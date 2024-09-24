class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:

        pool = defaultdict(int)

        for x in arr1:
            temp = str(x)
            prefix = ""
            for ch in temp:
                prefix += ch
                pool[prefix] += 1

        res = 0
        for y in arr2:
            temp = str(y)
            prefix = ""
            for ch in temp:
                prefix += ch
                if prefix not in pool:
                    break
                else:
                    res = max(res, len(prefix))
        return res
