class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_mat=[0]*len(matrix)
        col_mat=[0]*len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    row_mat[i]=1
                    col_mat[j]=1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if row_mat[i]==1 or col_mat[j]==1:
                    matrix[i][j]=0
            
