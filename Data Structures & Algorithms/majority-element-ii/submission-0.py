class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d={}
        for i in nums:
            if i not in d:
                d[i]=0
            d[i]+=1
        
        ans=[]
        for i in d:
            if d[i]>len(nums)//3:
                ans.append(i)
        
        return ans

        