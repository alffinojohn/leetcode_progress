from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        q = deque()
        mins = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))

        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        while q and fresh > 0:
            length = len(q)
            for i in range(length):
                row,col = q.popleft()
                for r, c in directions:
                    nr = row + r
                    nc = col + c

                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                        continue

                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr,nc))

            mins += 1

                
        if fresh > 0:
            return -1

        else:
            return mins




                





            

            


        