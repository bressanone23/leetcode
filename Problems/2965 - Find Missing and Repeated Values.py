class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        pool = set()
        n = len(grid)
        res = int((n**2+1)*n**2/2)
        tar = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] in pool:
                    tar.append(grid[i][j])
                else:
                    pool.add(grid[i][j])
                    res -= grid[i][j]
        return tar + [res]
