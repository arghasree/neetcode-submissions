class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # one hashmap for the rows like row[1]: 1->true, etc, row[2]:1->false etc
        # another hashmap for the columns col[1]: 1->true etc. 
        # another hashmap for box[1]: 1->true etc. 

        rows, cols = len(board), len(board[0])     
        
        list_rows =[]
        list_cols=[]
        list_boxes =[]

        for i in range(rows):
            d={}
            for j in range(rows):
                d[str(j+1)]=False
            list_rows.append(d)  

        for i in range(rows):
            d={}
            for j in range(rows):
                d[str(j+1)]=False
            list_cols.append(d)

        for i in range(rows):
            d={}
            for j in range(rows):
                d[str(j+1)]=False
            list_boxes.append(d)


        box_indx = {
            'UL' : 1,
            'UM' : 2,
            'UR': 3,
            'ML': 4, 
            'MM': 5,
            'MR': 6,
            'BL':7,
            'BM':8,
            'BR':9
        }

        for i in range(rows):
            for j in range(cols):
                if board[i][j]=='.':
                    continue

                if not list_rows[i][board[i][j]]:
                    list_rows[i][board[i][j]]=True
                else:
                    return False
                if not list_cols[j][board[i][j]]:
                    list_cols[j][board[i][j]]=True
                else:
                    return False
                s=''
                if i<=2 and i>=0:
                    s+='U'
                elif i<=5 and i>=3:
                    s+='M'
                else:
                    s+='B'

                if j<=2 and j>=0:
                    s+='L'
                elif j<=5 and j>=3:
                    s+='M'
                else:
                    s+='R'
                
                if not list_boxes[box_indx[s]-1][board[i][j]]:
                    list_boxes[box_indx[s]-1][board[i][j]]=True
                else:
                    return False
        return True
                    
