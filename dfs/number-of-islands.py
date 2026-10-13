class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0

        rows = len(grid)
        columns = len(grid[0])
        count = 0

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= columns or grid[r][c] != '1':
                return
            grid[r][c] = '0'

            dfs(r, c+1)
            dfs(r, c-1)
            dfs(r+1, c)
            dfs(r-1, c)

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == '1':
                    dfs(r, c)
                    count+=1
        return count
