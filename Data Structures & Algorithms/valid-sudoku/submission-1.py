class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        digit=["0","1","2","3","4","5","6","7","8","9"]

        row={0:set(),1:set(),2:set(),3:set(),4:set(),5:set(),6:set(),7:set(),8:set(),9:set()}
        col={0:set(),1:set(),2:set(),3:set(),4:set(),5:set(),6:set(),7:set(),8:set(),9:set()}
        sqr={(0,0):set(),(0,1):set(),(0,2):set(),(1,0):set(),(1,1):set(),(1,2):set(),(2,0):set(),(2,1):set(),(2,2):set()}

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
                
        