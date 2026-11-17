class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def decode(m):
            c=0
            for i in piles:
                c+=math.ceil(i/m)
            return c

        # finding out the maximum 
        max_ = max(piles)

        l=1
        r=max_
        k=0
        found=False

        while l<=r:
            m = (l+r)//2
            h_hat = decode(m)
            print(m, h_hat, h)
            if h_hat>h:
                # if found:
                #     break 
                l=m+1
            elif h_hat<=h:
                k=m
                r=m-1
            print(l, r, '\n')
        
        return k



        