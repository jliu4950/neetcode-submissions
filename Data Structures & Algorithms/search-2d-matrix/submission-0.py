class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])

        l=0
        r=m*n
        
        while l<r:
            mid=l+(r-l)//2
            cur=matrix[mid//n][mid%n]
            if cur==target:
                return True
            elif cur>target:
                r=mid
            elif cur<target:
                l=mid+1
        
        return False