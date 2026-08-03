class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        
        k=0
        for i in [0,1,2]:
            if i in d:
                while d[i]>0:
                    nums[k]=i
                    d[i]-=1
                    k+=1
                
                    

        