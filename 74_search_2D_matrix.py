class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m=len(matrix)
        n=len(matrix[0])
        l=0
        h=m*n-1 #len of the 1D matrix

        while l<=h:
            mid=(l+h)//2
            row=mid//n
            col=mid%n
            mid_value=matrix[row][col]

            if matrix[row][col]==target:
                return True
            elif matrix[row][col]<target:
                l=mid+1
            else:
                h=mid-1
        return False