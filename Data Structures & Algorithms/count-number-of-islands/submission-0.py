class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid: 
            return 0
        
        islands = 0 
        visited = set()

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited.add((r, c))

            while q: 
                val = q.popleft()
                r, c = val[0], val[1]

                directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
                for rd, cd in directions: 
                    rc, cr = r + rd, c + cd
                    if (rc in range(len(grid)) and cr in range(len(grid[0])) and (rc, cr) not in visited and grid[rc][cr] == "1"):
                        visited.add((rc, cr))
                        q.append((rc, cr))

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r, c) not in visited: 
                    bfs(r, c)
                    islands += 1

        return islands 