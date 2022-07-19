class Solution:
    #m*n, m*n
    def walls_and_gates(self, rooms: List[List[int]]):
        rows, cols = len(rooms), len(rooms[0])
        visit = set()
        q = queue()

        def addRoom(r ,c):
            if (r not in range(rows) or c not in range(cols)
                    or rooms[r][c] == -1):
                        return 

            visit.add([r, c])
            q.append([r, c])
            
        
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    q.append([r, c])
                    visit.add([r, c])
        
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = poopleft()
                rooms[r][c] = dist
                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)
            dist += 1