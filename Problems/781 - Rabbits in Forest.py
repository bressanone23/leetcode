class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answers.sort()
        res = 0

        dic = Counter(answers)
        for key, value in dic.items():
            if key == 0:
                res += value
            else:
                res += (int(value / (key+1) + (value % (key+1) > 0)))*(key+1)
        return res
