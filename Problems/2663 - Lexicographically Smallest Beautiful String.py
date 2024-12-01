class Solution:
    def smallestBeautifulString(self, s: str, k: int) -> str:
        pool = [chr(x+97) for x in range(k)]
        flag = 0

        s = list(s)

        def test(st,i,ch):
            if i >= 1 and st[i-1] == ch:
                return True
            if i >= 2 and st[i-2] == ch:
                return True

        n = len(s)

        #print(pool)
        for i in range(n-1,-1,-1):
            for ch in pool[ord(s[i]) - 97 + 1:]:
                if test(s,i,ch):
                    continue
                else:
                    s[i] = ch
                    for j in range(i+1,n):
                        for ch_new in pool:
                            if not test(s,j,ch_new):
                                s[j] = ch_new
                                break

                flag = 1
                break

            if flag:
                break

        return "".join(s) if flag == 1 else ""
