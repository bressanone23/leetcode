class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        res = []

        for i in range(len(s1)):
            if len(res) > 2:
                return False
            if s1[i] != s2[i]:
                res.append(i)
        if res == []:
            return True
        if len(res) != 2:
            return False

        if s1[res[0]] == s2[res[1]] and s1[res[1]] == s2[res[0]]:
            return True
        return False
