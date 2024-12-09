class Solution:
    def isArraySpecial(self, A: List[int], Q: List[List[int]]) -> List[bool]:
        P = [0] * len(A)
        for i in range(len(A)):
            P[i] = P[i-1] + (A[i] % 2 != A[i-1] % 2)
        #print(P)
        ans = []
        for q in Q:
            Count = P[q[1]] - P[q[0]]
            Total = q[1] - q[0]
            if Total == Count:
                ans.append(True)
            else:
                ans.append(False)

        return ans
