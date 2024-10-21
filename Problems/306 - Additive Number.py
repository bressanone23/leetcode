class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if int(num) == 0 and len(num) > 2:
            return True

        def dfs(start, prev):
            if start == len(num):
                return True
            if start != len(num) - 1 and num[start] == '0':
                return False

            for end in range(start+1, len(num)+1):
                if int(num[start:end]) == int(prev[-1]) + int(prev[-2]):
                    prev.append(num[start:end])
                    return dfs(end, prev)
                    prev.pop()

        for i in range(1,len(num)-1):
            for j in range(1,len(num)-i):
                #print([num[:i], num[i:i+j]])
                if (i > 1 and num[0] == '0') or (j > 1 and num[i] == '0'):
                    break
                if dfs(i+j, [num[:i], num[i:i+j]]):
                    return True


        return False
