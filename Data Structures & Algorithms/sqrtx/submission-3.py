class Solution:
    def mySqrt(self, x: int) -> int:
        l,r =1, x//2

        if x==1:
            return 1
        
        if x==0:
            return 0

        while(l<=r):
            m = (l+r)//2
            # print(f'{m}*{m} = {x}')
            next_ = m+1 if m+1<=x else None

            if m*m==x:
                return m 
            elif m*m<x:
                if next_ is not None and (next_*next_)>x:
                    return m 
                l=m+1
            elif m*m>x:
                r=m-1
        


        