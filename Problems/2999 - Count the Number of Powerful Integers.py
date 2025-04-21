class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:

        def calculate(x, s, limit):
            if len(x) < len(s):
                return 0
            if len(x) == len(s):
                return 1 if x >= s else 0

            suffix = x[len(x) - len(s) :]
            count = 0
            pre_len = len(x) - len(s)

            for i in range(pre_len):
                if limit < int(x[i]):
                    count += (limit + 1) ** (pre_len - i)
                    return count
                count += int(x[i]) * (limit + 1) ** (pre_len - 1 - i)


            return count + 1 if suffix >= s else count


        return calculate(str(finish), s, limit) - calculate(str(start-1), s, limit)
