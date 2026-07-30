class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        if not board: 
            return board

        arr = []

        """
            Find all the coordinates that are surrounded. Add it to the arr and then just swap them
        """

        rows = len(board)
        cols = len(board[0])
        visited = set()

        def dfs(r, c, component):
            if r < 0 or r >= rows or c < 0 or c >= cols: 
                return True

            if (r, c) in visited or board[r][c] == "X": 
                return False

            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

            visited.add((r, c))
            component.append((r, c))

            escaped = False

            for dr, dc in directions: 
                nr, nc = dr + r, dc + c
                if dfs(nr, nc, component):
                    escaped = True

            return escaped

        
        for r in range(rows):
            for c in range(cols):
                component = []
                if board[r][c] == "O" and (r, c) not in visited: 
                    if not dfs(r, c, component):
                        arr.extend(component)

        for r, c in arr: 
            board[r][c] = "X"