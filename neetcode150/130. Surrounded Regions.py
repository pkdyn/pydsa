class Solution:
    #m*n, m*n
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        def dfs(r, c):
            if (r not in range(rows) or c not in range(cols)
               or board[r][c] != "O"): #rather than == X, cauze we got Z too
                return 
            board[r][c] = "Z"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
            
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and r in [0, rows - 1] or c in [0, cols - 1]:
                    dfs(r, c)
                    
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                    
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "Z":
                    board[r][c] = "O"
                    
        
        