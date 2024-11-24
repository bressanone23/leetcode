class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        pool = [['*']*n for _ in range(m)]

        for w in walls:
            pool[w[0]][w[1]] = 'W'

        for g in guards:
            pool[g[0]][g[1]] = 'W'

        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        for gx,gy in guards:
            for dx, dy in dirs: # dx, dy - movement direction offsets
                x, y = gx, gy

                while True:
                    x += dx
                    y += dy

                    if x < 0 or x >= m or y < 0 or y >= n or pool[x][y] == 'W':
                        break

                    pool[x][y] = '#'

        return sum(x.count('*') for x in pool)
