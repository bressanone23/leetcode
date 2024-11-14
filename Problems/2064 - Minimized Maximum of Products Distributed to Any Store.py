class Solution:
    def minimizedMaximum(self, n: int, A: List[int]) -> int:
        left, right = 1, max(A)
        while left < right:
            x = (left + right) // 2
            if sum(math.ceil(a/x) for a in A) > n:
                left = x + 1
            else:
                right = x
        return left
