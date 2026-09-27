class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        visited = set()
        
        def dfs(r,c, i):
            if r >= row or r < 0 or c >= col or c < 0:
                return False

            if (r,c) in visited:
                return False

            if board[r][c] != word[i]:
                return False

            if i+1 == len(word):
                return True

            visited.add((r,c))

            res =  (
                dfs(r+1, c, i+1) or
                dfs(r-1, c, i+1) or
                dfs(r, c+1, i+1) or
                dfs(r, c-1, i+1)
            )

            visited.remove((r,c))

            return res

        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    if dfs(i,j,0):
                        return True

        return False


        

            
