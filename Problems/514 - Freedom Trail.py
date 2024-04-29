class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        m = len(ring)
        n = len(key)

        let_to_pos = {}
        for i, x in enumerate(ring):
            if x in let_to_pos:
                let_to_pos[x].append(i)
            else:
                let_to_pos[x] = [i]

        dp = [[float('Inf')]*m for _ in range(n)]
        for j in range(m):
            if ring[j] == key[0]:
                dp[0][j] = min(j,m-j)

        for i in range(1,n):
            for cur_pos in let_to_pos[key[i]]:
                for pre_pos in let_to_pos[key[i-1]]:
                    dp[i][cur_pos] = min(dp[i][cur_pos], dp[i-1][pre_pos] + min(abs(cur_pos-pre_pos),m-abs(cur_pos-pre_pos)))
        #print(dp)
        return min([dp[n-1][x] for x in range(m)]) + n
