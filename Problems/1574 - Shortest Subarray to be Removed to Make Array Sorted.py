class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        left =len(arr) - 1
        right = 0
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                left = i
                break

        for j in range(len(arr)-1,0,-1):
            if arr[j] < arr[j-1]:
                right = j
                break

        #print(left, right)

        if left == len(arr) - 1:
            return 0
        # if left == 0 and right == (len(arr) - 1):
        #     return min(len(arr)-left-1, right)

        curr = min(len(arr)-left-1, right)

        res = len(arr)
        k = 0
        while k <= left:
            while right < len(arr):
                if arr[right] >= arr[k]:
                    #print(k, right)
                    res = min(res, right - k - 1)
                    break
                right += 1

            k += 1
        #print(res)
        return min(res, curr)
