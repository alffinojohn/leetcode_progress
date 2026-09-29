class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r]:
                    return False
                rows[r].add(board[r][c])

                if board[r][c] in cols[c]:
                    return False
                cols[c].add(board[r][c])

                box = (r //3, c//3)
                if board[r][c] in boxes[box]:
                    return False
                boxes[box].add(board[r][c])

        return True
                


