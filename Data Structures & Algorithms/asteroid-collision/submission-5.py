class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        def attack(res, a):
            # last is always > a
            last=res.pop()
            if abs(last) == abs(a) and (last>a or a>last):
                return 
            elif (last<0 and a<0) or (last>0 and a>0):
                res.append(last)
                res.append(a)
     
            elif abs(last) < abs(a):
                if res==[]:
                    res.append(a)
                else:
                    attack(res, a)     
            elif abs(last)>abs(a):
                res.append(last)

        res=[]

        for i in asteroids:
            # print(res, i)
            if res==[]:
                res.append(i)
            elif i>0 and res[-1]>0:
                res.append(i)
            elif i<0 and res[-1]<0:
                res.append(i)
            elif i<0 and res[-1]>0:
                attack(res, i)
                # print(res)
            elif i>0 and res[-1]<0:
                res.append(i)

        
        
        # res=[]
        # for i in asteroids:
        #     if res==[]:
        #         res.append(i)
        #     elif i>0 and res[-1]>0:
        #         res.append(i)
        #     elif i<0 and res[-1]<0:
        #         res.append(i)
        #     else:
        #         attack(res, i)

        return res



        """
        popped>0 and a>0: add to stack 
        popped>0 and a<0: 
            if a is bigger then add the bigger one back 
            
        popped<0 and a>0
        popped<0 and a<0: add to stack 
        """
        # stack=[]
        # for a in asteroids:
        #     if stack!=[]:
        #         popped=stack.pop()
        #         if popped<0 and a<0:
                    
        #         popped>abs(a):
        #             stack.append(popped)
        #         if popped<abs(a):
        #             stack.append(a)
                    
        