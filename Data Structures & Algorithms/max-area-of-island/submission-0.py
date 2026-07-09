class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visit = set()
        island = 0
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return 0
            grid[r][c] = 0  # mark visited
            area = 1
            for dr, dc in directions:
                area += dfs(r + dr, c + dc)
            return area

        island = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    island = max(island, dfs(r, c))
        return island