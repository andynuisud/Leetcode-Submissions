class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        maxArea = 0

        def dfs(r, c):
            nonlocal maxArea
            if r < 0 or r >= rows or c < 0 or c >= cols: 
                return 
            if grid[r][c] == 0:
                return 
            if (r, c) in visited:
                return
            
            visited.add((r, c))
            
            directions = [[1, 0], [0, 1], [0, -1], [-1, 0]]

            area = 1

            for dr, dc in directions: 
                nr, nc = dr + r, dc + c
                area += dfs(nr, nc) or 0

            maxArea = max(maxArea, area)
            return area
                

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    dfs(r, c)


        return maxArea