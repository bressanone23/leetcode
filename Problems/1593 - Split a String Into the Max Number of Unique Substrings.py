class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def backtrack(start, seen):
            count = 0
            if start == len(s):
                return 0

            for end in range(start+1, len(s)+1):
                if s[start:end] not in seen:
                    seen.add(s[start:end])
                    count = max(count, 1 + backtrack(end, seen))
                    seen.remove(s[start:end])

            return count

        return backtrack(0, set())
