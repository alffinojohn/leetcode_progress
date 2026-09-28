class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        seen = set()
        island = 0

        def dfs(r,c):
            if r >= row or r < 0 or c >= col or c < 0:
                return 

            if (r,c) in seen:
                return 

            if grid[r][c] == "0":
                return 

            seen.add((r,c))

            dfs(r+1,c) 
            dfs(r-1,c) 
            dfs(r,c+1)
            dfs(r,c-1)


        for i in range(row):
            for j in range(col):
                if (i,j) not in seen and grid[i][j] == "1":
                    island += 1
                    dfs(i,j)

        return island


            


        