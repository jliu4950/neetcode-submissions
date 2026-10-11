from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dq = deque()
        cnt_fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    dq.append((r,c))
                if grid[r][c] == 1:
                    cnt_fresh += 1
        
        def to_rotten(r,c):
            nonlocal cnt_fresh
            if r not in range(rows) or c not in range(cols) or grid[r][c] != 1:
                return
            
            grid[r][c] = 2
            cnt_fresh -= 1
            dq.append((r,c))

        minitues = 0
        while dq and cnt_fresh >0:
            minitues += 1
            for _ in range(len(dq)):
                r,c = dq.popleft()
                to_rotten(r + 1,c)
                to_rotten(r - 1,c)
                to_rotten(r,c + 1)
                to_rotten(r,c - 1)
        
        return minitues if cnt_fresh == 0 else -1