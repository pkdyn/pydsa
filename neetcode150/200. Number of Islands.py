class Solution:
    #m*n, m*n
    def numIslands(self, grid: List[List[str]]) -> int:
        
        islnd = 0
        visit = set()
        rows, cols = len(grid), len(grid[0])
        
        def bfs(r, c): #bfs is iterative, gotta use a data structure
            q = collections.deque()
            q.append((r,c))
            visit.add((r,c))
            while q: #dont forget q loop
                dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                r, c = q.popleft() # do pop() for iterativ dfs
                for dr, dc in dir:
                    if (r + dr in range(rows) and c + dc in range(cols) and grid[r + dr][c +                     dc] == "1" and (r + dr, c + dc) not in visit):
                        visit.add((r + dr, c + dc))
                        q.append((r + dr, c + dc))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islnd += 1
        
        return islnd