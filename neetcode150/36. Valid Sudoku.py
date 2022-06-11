class Solution:
    #n**2, n**2
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rSet = defaultdict(set) #default dict of sets (for invalid keys)
        cSet = defaultdict(set)
        boxSet = defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rSet[r] 
                or board[r][c] in cSet[c] 
                #truncate division for creating key via box no.
                or board[r][c] in boxSet[(r//3, c//3)]): 
                        return False
                
                rSet[r].add(board[r][c])
                cSet[c].add(board[r][c])
                boxSet[(r//3, c//3)].add(board[r][c])        
        
        return True
        