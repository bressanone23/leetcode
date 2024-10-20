class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        # If the length is 1, then it's S1
        if n == 1:
            return '0'

        # Calculate the length of the string Sn
        length = (2 ** n) - 1

        # If k is exactly the middle digit, it is 1
        if k == (length + 1) // 2:
            return '1'

        # If k is in the first half
        if k < (length + 1) // 2:
            return self.findKthBit(n - 1, k)

        # If k is in the second half, find the reverse position in the previous string
        # and return the inverted value
        return '0' if self.findKthBit(n - 1, length - k + 1) == '1' else '1'
