class Solution:
    # n!, n*n
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        col = set()
        pdig = set() # r+c konstant
        ndig = set() # r-c konstant
        board = [["."] * n for i in range(n)]
        
        def bcktrck(r):
            if r == n:
                copy = ["".join(ro) for ro in board]
                res.append(copy)
            for c in range(n):
                if c in col or r + c in pdig or r-c in ndig:
                    continue
                
                col.add(c)
                pdig.add(r + c)
                ndig.add(r - c)
                
                board[r][c]= "Q"
                bcktrck(r + 1)
                
                #revert for other possible solutions
                #clean up after backtracking
                col.remove(c)
                pdig.remove(r + c)
                ndig.remove(r - c)
                board[r][c] = "."
        
        bcktrck(0)
        return res
        