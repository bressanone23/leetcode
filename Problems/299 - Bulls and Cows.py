class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull, cow = 0,0
        dic = defaultdict(list)
        for i,x in enumerate(secret):
            if x == guess[i]:
                bull += 1

            dic[x].append(i)

        for i,x in enumerate(guess):
            if dic[x] != []:
                cow += 1
                dic[x].pop()

        return str(bull) + 'A' + str(cow-bull) +'B'
