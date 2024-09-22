class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        #Convert integers to strings
        array = list(map(str, nums))

        # Custom sorting with a lambda function
        array.sort(key=lambda x: x*10, reverse=True)

        #the maximum number that the input can be is 10**9, so if you multiply each string by 10
        #you guarantee matching the digits of the string to the highest possible candidate (e.g. 9 vs 90 becomes 9999999999 vs 909090...9090
        # which makes 9 the larger number)

        # Handle the case where the largest number is "0"
        if array[0] == "0":
            return "0"

        return ''.join(array)
