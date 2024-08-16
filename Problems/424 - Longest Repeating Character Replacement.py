class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = [0]*26
        l = 0
        count = k
        for r in range(len(s)):
            dic[ord(s[r]) - ord('A')] += 1
            if r - l + 1 - max(dic) > k:
                dic[ord(s[l]) - ord('A')] -= 1
                l += 1

            count = max(count,r-l+1)
            #print(l,r,dic)
        return count
