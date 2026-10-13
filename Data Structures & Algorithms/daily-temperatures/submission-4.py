class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # I thought I cannot save the index too but since i can. 

        stack=[]
        res=[]
        ans=0
        for i in range(len(temperatures)-1, -1, -1):
            t=temperatures[i]
            ans=0
            while stack:
                te = stack.pop()
                ele, ele_indx = te[0], te[1]
                if ele>t:
                    stack.append([ele, ele_indx])
                    ans=ele_indx - i
                    break
            stack.append([t, i])
            res.append(ans)

        return res[::-1]







        # s1=[]
        # s2=[]
        # res=[]
        # ans=temperatures[-1]
        # for i in range(len(temperatures)-1, -1, -1):
        #     t=temperatures[i]
        #     # print(s1, s2, t, res)
        #     if s1==[]:
        #         s1.append(t)
        #         res.append(0)
        #     else:
        #         # find out the next big ele in the stack 
        #         k=0
        #         while s1!=[]:
        #             # print('inside', s1, s2, t)
        #             ele = s1.pop()
        #             s2.append(ele)
        #             k+=1
        #             if ele>t:
        #                 break
                
        #         # if s1 is empty that means that t is the highest ele as of yet. 
        #         if not s1 and ele<t:
        #             k=0 
                    
        #         while s2!=[]:
        #             s1.append(s2.pop())
                
        #         res.append(k)
        #         s1.append(t)
        # return res[::-1]
            