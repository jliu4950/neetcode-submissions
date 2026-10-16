from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        '''
        1. find every treasure chest
        2. use bfs from treasure chest
        3. bfs:
            * detect four derection ,
                if not visited before and not water cell: mark distance and mark visited and add it to deque
                else: continue
        4.done
        '''
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        dq = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    dq.append((r,c))
                    visited.add((r,c))
        
        # bfs
        dis = 0
        while dq:
            for _ in range(len(dq)):
                r,c = dq.popleft()
                grid[r][c] = dis
                #visited.add((r,c))

                direction = [[-1,0],[1,0],[0,-1],[0,1]]
                for x,y in direction:
                    nr = r + x
                    nc = c + y
                    if nr in range(ROWS) and nc in range(COLS) and (nr,nc) not in visited and grid[nr][nc] != -1:
                        dq.append((nr,nc))
                        visited.add((nr,nc))
            dis += 1
                        



