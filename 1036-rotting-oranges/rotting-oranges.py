from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        rotten = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    rotten.append((r,c))

        mins = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        while rotten and fresh > 0:
            size = len(rotten)
            for i in range(size):
                row,col = rotten.popleft()
                for r,c in directions:
                    nr = row + r
                    nc = col + c

                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        continue

                    if grid[nr][nc] == 1:
                        rotten.append((nr,nc))
                        grid[nr][nc] = 2
                        fresh -= 1

            mins += 1

        if fresh:
            return -1
        
        return mins







        