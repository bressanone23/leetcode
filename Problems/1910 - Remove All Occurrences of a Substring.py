class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        for ch in s:
            stack.append(ch)
            if len(stack) >= len(part):
                if "".join(stack[-len(part):]) == part:
                    for _ in range(len(part)): stack.pop()
        return "".join(stack)
