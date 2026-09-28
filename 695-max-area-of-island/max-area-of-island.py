class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        seen = set()
        area = 0

        def dfs(r,c):
            if r >= row or r < 0 or c >= col or c < 0:
                return 0

            if grid[r][c] == 0:
                return 0

            if (r,c) in seen:
                return 0

            seen.add((r,c))

            return(1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1))

        for i in range(row):
            for j in range(col):
                if (i,j) not in seen and grid[i][j] == 1:
                    count = dfs(i,j)
                    area = max(area, count)


        return area

grid = [
    [0, 0 , 0 ,0],
    [0, 1 , 0 ,0],
    [0, 1 , 0 ,0],
    [0, 0 , 0 ,0]
]