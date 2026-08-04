class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k==len(nums):
            return nums

        count=[[]]*len(nums)

        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        
        for key in d:
            count[d[key]-1]=count[d[key]-1]+[key]
        
        ans=[]
        for i in range(len(count)-1,-1,-1):
            if count[i]!=[]:
                ans+=count[i]

        return ans[:k]




        
        
