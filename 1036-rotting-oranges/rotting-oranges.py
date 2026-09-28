from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        q = deque()
        row = len(grid)
        col = len(grid[0])
        mins = -1

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        fresh = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1

        if fresh == 0:
            return 0


        while q:
            size = len(q)
            for i in range(size):
                r,c = q.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if nr >= row or nr < 0 or nc >= col or nc < 0:
                        continue
                    if grid[nr][nc] == 1:
                        q.append((nr,nc))
                        grid[nr][nc] = 2
                        fresh -= 1

            mins += 1

        if fresh > 0:
            return -1
        else:
            return mins
                
                

        