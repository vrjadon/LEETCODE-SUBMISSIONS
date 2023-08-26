class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascaltriangle=[[0]*(i+1) for i in range(numRows)]
        for row in range(numRows):
            for column in range(row+1):
                if column==0 or column==row:
                    pascaltriangle[row][column]=1
                else:
                    pascaltriangle[row][column]=pascaltriangle[row-1][column-1]+pascaltriangle[row-1][column]
        return pascaltriangle