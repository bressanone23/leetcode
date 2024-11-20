class Solution:
# Instead of taking k of each character from left and right, we take at most count(c) - k of each character from middle.

# For Example 1, s = "aabaaaacaabc" with k = 2:
# we have freq = {'a': 8, 'b': 2, 'c': 2}
# this converts to limits = freq - k = {'a': 6, 'b': 0, 'c': 0}
# now the problem becomes "finding the longest substring where the occurrence of each character is within limits"
# we can easily solve this new problem using sliding window

    def takeCharacters(self, s: str, k: int) -> int:
        limits = {c: s.count(c) - k for c in 'abc'}

        if any(x < 0 for x in limits.values()):
            return -1

        ct = {'a':0, 'b':0, 'c':0}

        l, ans = 0, 0

        for i, ch in enumerate(s):
            ct[ch]+= 1

            while ct[ch] > limits[ch]:
                ct[s[l]]-= 1
                l+= 1

            ans = max(ans, i - l + 1)

        return len(s) - ans
