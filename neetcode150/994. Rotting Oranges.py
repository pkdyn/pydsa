class Solution:
    #n*m, n*m
    def orangesRotting(self, grid: List[List[int]]) -> int:
        frsh = 0
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    frsh += 1
                elif grid[r][c] == 2:
                    q.append([r, c])
        
        time = 0
        dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q and frsh:
            for i in range(len(q)): #to traverse the original length of q
                #as we'll be appending it with them fresh ones
                r, c = q.popleft()
                for dr, dc in dir:
                    if (r + dr not in range(rows) or c + dc not in range(cols)
                        or grid[r + dr][c + dc] != 1):
                        continue
                    grid[r + dr][c + dc] = 2
                    q.append([r + dr, c + dc])
                    frsh -= 1
            time += 1
        
        return -1 if frsh else time
                