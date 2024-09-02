class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m=len(grid1)
        n=len(grid1[0])

        def dfs(i,j):
            if i<0 or i>=m or j<0 or j>=n or grid2[i][j]==0:
                return

            grid2[i][j]=0

            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i,j-1)
            dfs(i-1,j)

        # removing all the non-common sub-islands
        for i in range(m):
            for j in range(n):
                if grid2[i][j]==1 and grid1[i][j]==0:
                    dfs(i,j)

        c=0
        # counting sub-islands
        for i in range(m):
            for j in range(n):
                if grid2[i][j]==1:
                    dfs(i,j)
                    c+=1
        return c


# firstly remove all the non-common island which means - If a cell in grid2 is a land-cell (part of an island) but the corresponding cell in grid1 is water,
# then that particular island in grid2 cannot be considered as a valid island. All islands in grid2 must be contained within (or be a subset of) the islands in grid1.
#
# After removing all the islands from grid2 that are not completely contained within the islands of grid1,
# the remaining islands in grid2 are subsets or parts of the islands in grid1.
#
# Now count the sub-islands
