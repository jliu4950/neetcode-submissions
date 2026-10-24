from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        dq = deque()
        
        rows = len(grid)
        cols = len(grid[0])

        visited = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    dq.append((r,c))
                    visited.add((r,c))
        dirc = [[-1,0],[1,0],[0,-1],[0,1]]
        distance = 0
        while dq:

            for _ in range(len(dq)):
                r,c = dq.popleft()
                grid[r][c] = distance
                for i,j in dirc:
                    nr = r + i
                    nc = c + j

                    if 0<= nr < rows and 0 <= nc < cols and grid[nr][nc] != -1 and (nr,nc) not in visited:
                        dq.append((nr,nc))
                        visited.add((nr,nc))
            distance += 1

