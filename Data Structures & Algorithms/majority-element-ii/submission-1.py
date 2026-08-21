class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d={}
        count_neg=0
        for i in nums:
            if i not in d:
                d[i]=0
            d[i]+=1

            if count_neg<=2:
                print(d)
                continue
            
            count_neg=0
            for key in d:
                d[key]-=1
                if d[key]<=0:
                    count_neg+=1

            print(d)
        # print(d)
        res=[]
        for key in d:
            if d[key]>0:
                count=0
                for i in nums:
                    if i==key:
                        count+=1
                if count>len(nums)//3:
                    res.append(key)
                    
        return res






        # d={}
        # for i in nums:
        #     if i not in d:
        #         d[i]=0
        #     d[i]+=1
        
        # ans=[]
        # for i in d:
        #     if d[i]>len(nums)//3:
        #         ans.append(i)
        
        # return ans

        

        