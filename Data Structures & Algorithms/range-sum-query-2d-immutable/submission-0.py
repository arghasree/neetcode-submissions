class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        presum = [[0]* (len(matrix[0])+1) for i in range(len(matrix)+1)]
        for i in range(len(matrix)):
            for j in range( len(matrix[0])):
                presum[i+1][j+1]=matrix[i][j]

        for i in range(1, len(matrix)+1):
            for j in range(1, len(matrix[0])+1):
                presum[i][j]+=presum[i][j-1]+presum[i-1][j]- presum[i-1][j-1]

        self.presum=presum    
        
        # for i in range(len(matrix)+1):
        #     for j in range(len(matrix[0])+1):
        #         print(presum[i][j], end='  ')
        #     print()
        
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         print(matrix[i][j], end='  ')
        #     print()
        
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1+1, col1+1, row2+1, col2+1
        left = self.presum[row2][col1-1] # -1 for the before and +1 because there are extra rows and columns
        up=self.presum[row1-1][col2]
        to_add = self.presum[row1-1][col1-1]

        # print(self.presum[row2][col2], left , up , to_add)

        return self.presum[row2][col2] - left - up + to_add

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)