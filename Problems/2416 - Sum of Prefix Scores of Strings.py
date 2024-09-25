class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        pool = defaultdict(int)

        for w in words:
            temp = ""
            for c in w:
                temp += c
                pool[temp] += 1


        res = []

        for w in words:
            temp = ""
            num = 0
            for c in w:
                temp += c
                num += pool[temp]
            res.append(num)
        return res
