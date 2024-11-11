class Solution:
    def compressedString(self, word: str) -> str:
        res = ""
        word += '$'
        last = word[0]
        count = 1

        for x in word[1:]:

            if count ==0:
                count += 1
                last = x
            else:
                if x == last:
                    count += 1
                else:
                    res += str(count) + last
                    count = 1
                    last = x

                if count == 9:
                    res += str(count) + last
                    count = 0

        return res


class Solution:
    def compressedString(self, word: str) -> str:
        res = ""
        word += '$'
        last = word[0]
        count = 1

        for x in word[1:]:
                if x == last and count < 9:
                    count += 1
                else:
                    res += str(count) + last
                    count = 1
                    last = x

        return res
