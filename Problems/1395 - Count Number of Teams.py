class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        res = 0

        for i in range(n):
            left_smaller, right_larger = 0,0
            for j in range(i):
                if rating[j] < rating[i]:
                    left_smaller += 1
            for k in range(i+1,n):
                if rating[i] < rating[k]:
                    right_larger += 1

            res += left_smaller*right_larger + (i-left_smaller)*(n-i-1-right_larger)
        return res
