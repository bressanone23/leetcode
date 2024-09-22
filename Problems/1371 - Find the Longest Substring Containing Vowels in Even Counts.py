class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        n = len(s)
        dic = {'00000':-1}
        count = [0]*5
        res = 0
        for j in range(n):
            if s[j] == 'a':
                count[0] += 1
                count[0] %= 2
            elif s[j] == 'e':
                count[1] += 1
                count[1] %= 2
            elif s[j] == 'i':
                count[2] += 1
                count[2] %= 2
            elif s[j] == 'o':
                count[3] += 1
                count[3] %= 2
            elif s[j] == 'u':
                count[4] += 1
                count[4] %= 2

            key = "".join([str(x) for x in count])

            if key in dic:
                res = max(res, j - dic[key])
            else:
                dic[key] = j
        #print(dic)
        return res
