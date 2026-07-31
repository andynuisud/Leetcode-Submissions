class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        
        #Unique paths uses backtracking

        """
            Unique paths -> backtracking

            Visited = set() -> Add to the set -> Run DFS -> Remove from the set -> Recursively call to get a count
        """

        def dfs(grid, r, c, visited):
            rows = len(grid)
            cols = len(grid[0])

            if r < 0 or c < 0 or r >= rows or c >= cols: 
                return 0 

            if grid[r][c] == 1 or (r, c) in visited : 
                return 0 

            if r == rows - 1 and c == cols - 1: 
                return 1 
            
            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

            count = 0
            visited.add((r, c))

            for dr, dc in directions: 
                nr, nc = dr + r, dc + c
                count += dfs(grid, nr, nc, visited)
            
            visited.remove((r, c))
            return count

        return dfs(grid, 0, 0, set())