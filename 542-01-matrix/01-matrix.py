from collections import deque
class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        rows = len(mat)
        cols = len(mat[0])
        dist = [ [-1]*cols for _ in range(rows)]

        zeros = deque()

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    dist[r][c] = 0
                    zeros.append((r,c))

        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        while zeros:
            length = len(zeros)
            for _ in range(length):
                row,col = zeros.popleft()
                for r,c in directions:
                    nr = row+r
                    nc = col+c

                    if nr >= rows or nr < 0 or nc >= cols or nc < 0 :
                        continue

                    if dist[nr][nc] == -1:
                        dist[nr][nc] = dist[row][col] + 1
                        zeros.append((nr,nc))


        return dist

                


        


        