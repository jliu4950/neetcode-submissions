from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        dq = deque()
        visited = set()
        # markdistance
        def addDistance(r,c):
            if r not in range(rows) or c not in range(cols) or (r,c) in visited or grid[r][c] == -1:
                return
            grid[r][c] = dis
            dq.append((r,c))
            visited.add((r,c))

        # find treasure chest and mark it
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    dq.append((r,c))
                    visited.add((r,c))
        
        # count distance
        dis = 0
        while dq:
            level = len(dq)
            dis += 1
            for _ in range(level):
                r,c = dq.popleft()
                addDistance(r + 1,c)
                addDistance(r - 1,c)
                addDistance(r,c + 1)
                addDistance(r,c - 1)

        