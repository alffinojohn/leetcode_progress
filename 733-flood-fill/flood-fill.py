class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # a dfs

        num = image[sr][sc]
        rows = len(image)
        col = len(image[0])

        if num == color:
            return image

        
        def dfs(r,c):
            
            if (
                r < 0 or r >= rows or c < 0 or c >= col or image[r][c] != num
            ):
                return

            image[r][c] = color

            dfs(r+1,c)
            dfs(r, c+1)
            dfs(r-1,c)
            dfs(r, c-1)

        dfs(sr, sc)
        return image

            






        