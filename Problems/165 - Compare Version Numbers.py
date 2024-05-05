class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
        l1,l2 = list(map(int, v1.split('.'))),list(map(int, v2.split('.')))
        i = 0
        while i < len(l1) or i < len(l2):
            a = l1[i] if i < len(l1) else 0
            b = l2[i] if i < len(l2) else 0
            if a < b:
                return -1
            elif a > b:
                return 1
            i += 1
        return 0
