class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if sentence1 == sentence2:
            return True

        s1,s2 = sentence1.split(" "), sentence2.split(" ")

        m,n = len(s1), len(s2)

        if m > n:
            s1,s2 = s2,s1
            m,n = n,m

        # ``````````````````````````````
        # # for i in range(n):
        # #     for j in range(1,n-m+1):
        # #         #print(s2[:i] + s2[i+j:])
        # #         if (s2[:i] + s2[i+j:]) == s1:
        # #             return True
        # # return False
        # ```````````````````````````````

        # Try to match the words from the start
        i = 0
        while i < m and s1[i] == s2[i]:
            i += 1

        # Try to match the words from the end
        j = 0
        while j < m and s1[-(j+1)] == s2[-(j+1)]:
            j += 1

        # If the matched prefix and suffix together cover all of words1, return true
        return i + j >= m
