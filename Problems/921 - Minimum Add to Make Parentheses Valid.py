class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        res = 0
        for x in s:
            if x == ')':
                if stack != []:
                    stack.pop()
                else:
                    res += 1
            if x == '(':
                stack.append(x)

            #print(stack)
        return len(stack) + res
