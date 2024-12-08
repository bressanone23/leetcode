class Solution:
    def minimumSize(self, A: List[int], k: int) -> int:
        left, right = 1, max(A)
        while left < right:
            mid = (left + right) // 2
            if sum((a - 1) // mid for a in A) > k:
                left = mid + 1
            else:
                right = mid
        return left
