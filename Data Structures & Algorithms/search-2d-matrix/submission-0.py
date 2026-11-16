class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix[0])
        n = len(matrix)
        row=None
        for i in range(n):
            if target<=matrix[i][m-1]:
                row=i 
                break
        if row is None:
            return False
        
        l=0
        r=m

        while l<=r:
            m = (l+r)//2
            if target < matrix[row][m]:
                r = m-1
            elif target>matrix[row][m]:
                l = m+1
            else:
                return True
        return False
        
        

        # def decode(i):
        #     m = len(matrix[0])
        #     n = len(matrix)
        #     return i[0] * m + i[1]
            
        # m = len(matrix[0])
        # n = len(matrix)
        # l=[0,0]
        # r=[n-1, m-1]
        
        # print(f'Decoded l = {decode(l)}, Decoded r = {decode(r)}')

        # while decode(l)<=decode(r):
        #     mid = (decode(r)-decode(l))//2        
        #     rows = mid//m
        #     cols= mid%m
        #     print('mid =', mid)
        #     print(f'rows = {rows}, cols = {cols}')
        #     print(l[0]+rows, l[1]+cols)
        #     mid= matrix[l[0]+rows][l[1]+cols]


        #     if mid<target:
        #         l = [l[0]+rows, l[1]+cols]
        #     elif mid>target:
        #         r = [l[0]+rows, l[1]+cols]
        #     else:
        #         return True
        #     print(f'Decoded l({l}) = {decode(l)}, Decoded r ({r}) = {decode(r)}')

        # return False