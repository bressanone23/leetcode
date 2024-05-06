class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        end = 0
        for i in range(len(word)-len(ch)+1):
            if word[i:i+len(ch)] == ch:
                end = i+len(ch)
                break
        return word[:end][::-1] + word[end:]
