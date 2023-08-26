class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        import math
        m=len(matrix)
        n=len(matrix[0])
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    for row in range(len(matrix)):
                        for column in range(len(matrix[0])):
                            if matrix[row][column]==0:
                                continue
                            elif row==i or column==j:
                                matrix[row][column]=float('-inf')
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == float('-inf'):
                    matrix[row][col] = 0
        

    
                    

        