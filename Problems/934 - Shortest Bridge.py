class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def dfs(grid,i,j, points):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != 1:
                return
            grid[i][j] = 0
            points.append([i,j])
            dfs(grid, i+1, j, points)
            dfs(grid, i-1, j, points)
            dfs(grid, i, j+1, points)
            dfs(grid, i, j-1, points)

        points1 = []
        points2 = []
        temp = 1
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if temp ==1:
                    if grid[i][j] == 1:
                        dfs(grid,i,j,points1)
                        temp = 2
                else:
                    if grid[i][j] == 1:
                        dfs(grid,i,j,points2)
        #print(points1,points2)

        dis = float('inf')
        for x in points1:
            for y in points2:
                dis = min(dis,abs(x[0]-y[0])+abs(x[1]-y[1]))
        return dis - 1
