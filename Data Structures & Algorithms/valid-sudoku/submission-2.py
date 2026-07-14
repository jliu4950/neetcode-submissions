from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #优化
        row=defaultdict(set)
        col=defaultdict(set)
        sqr=defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c]==".":
                    continue
                cur =board[r][c]
                if cur in row[r] or cur in col[c] or cur in sqr[(r//3,c//3)]:
                    return False
                
                row[r].add(cur)
                col[c].add(cur)
                sqr[(r//3,c//3)].add(cur)
        
        return True
                
        