class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        6 - [2,4,5,8] = abs -> [4,2,1,2]
        prefer the left most if two are the same 
        """
        res=[]
        point=len(arr)-1
        for i in range(len(arr)-1):
            if arr[i]>x and i==0:
                point=-1
                break
            if arr[i]<=x and arr[i+1]>x:
                point = i
        # print('point is', point)
        l=point
        r=point+1
        # l will go to the left 
        # r will go to the right 
        while k>0:
            # print(l, r)
            if l<0:
                res=res+[arr[r]]
                r+=1
            elif r>=len(arr):
                res=[arr[l]]+res
                l-=1
            elif abs(arr[l]-x)<=abs(arr[r]-x):
                res=[arr[l]]+res
                l-=1
            elif abs(arr[l]-x)>abs(arr[r]-x):
                res=res+[arr[r]]
                r+=1
            k-=1

        """
        for [2,3,4]
        point=-1
        l=-1 and r=0 
        k=3, and res=[2], r=1 and k=2 and so on 

        for [2,4,5,6], k=1 and x=7
        point=3 
        l=3 and r=4
        so res=[6] and l=2 and so on 
        """

        return res

        