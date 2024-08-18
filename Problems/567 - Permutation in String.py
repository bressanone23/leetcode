class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m,n = len(s1), len(s2)
        if m > n:
            return False

        dic = Counter(s1)
        base = Counter(s2[:m])

        for i in range(m,n):
            if base == dic:
                return True
            base[s2[i-m]] -= 1
            base[s2[i]] += 1
        return base == dic
