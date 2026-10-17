class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = {}
        rows = len(grid)
        cols = len(grid[0])
        land = 0
        
        def dfs(row,col):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return

            if grid[row][col] == "0":
                return

            if (row, col) in seen:
                return

            seen[(row, col)] = 1
            dfs(row-1,col)
            dfs(row+1,col)
            dfs(row,col+1)
            dfs(row,col-1)

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "0" or (r,c) in seen:
                    continue
                land += 1
                dfs(r,c)


        return land
                

            
            

            

