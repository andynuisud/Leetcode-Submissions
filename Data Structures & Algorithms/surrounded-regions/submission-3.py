class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        """
            Given m x n matrix. Where we are given letters X and O. 
            We want to find out the regions that are surrounded by X's

            We want to flip every `O` that is fully surrounded by 'X'
            All of the connected `O`s near the border can never be captured  
            Have an array to check everything thats safe and just revert them back to normal 

            BFS/DFS to figure that out
        """

        if not board or not board[0]:
            return 

        rows = len(board)
        cols = len(board[0])

        def dfs(r, c): 
            stack = [(r, c)]
            
            while stack: 
                row, col = stack.pop()

                if row < 0 or col < 0 or row >= rows or col >= cols: 
                    continue

                if board[row][col] != "O":
                    continue
                
                board[row][col] = "."

                directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

                for dr, dc in directions: 
                    nr, nc = row + dr, dc + col
                    stack.append((nr, nc))

        for r in range(rows):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][cols - 1] == "O":
                dfs(r, cols - 1)

        for c in range(cols):
            if board[0][c] == "O":
                dfs(0, c)
            if board[rows - 1][c] == "O":
                dfs(rows - 1, c)

        for r in range(rows):
            for c in range(cols): 
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == ".":
                    board[r][c] = "O"