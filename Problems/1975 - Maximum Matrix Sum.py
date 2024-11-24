class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:

        # The big observation for solving this problem is to realise that there is always at most one negative number. So if there is an even number of negative numbers we can flip all of them and if there an odd number them we can always flip all of them except of one.

        # Approach
        # Count how many negative there are
        # If there is an evem number of negative numbers, we return sum of absolute values of all elements
        # If there is an odd number of negative numbers, wer return sum of absolute values of all elements and subtract the minimum absolute value twice (cause we want to make that number negative)

        abs_min = float('inf') # minimum absolulte value in matrix
        cnt = 0 # counter of negative number
        abs_sum = 0 # sum of absolute values

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] < 0:
                    cnt += 1

                abs_min = min(abs(matrix[i][j]), abs_min) #
                abs_sum += abs(matrix[i][j])

        return abs_sum if cnt % 2 == 0 else abs_sum - abs_min * 2
