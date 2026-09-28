class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        r=0
        s=0
        res=9999999
        while r<len(nums):
            if nums[r]>=target:
                return 1
            
            s+=nums[r]

            if s<target:
                r+=1
                continue
            
            while l<r and s>=target:
                # print('sum=',s)
                res=min(res, r-l+1)
                print(s, '-', nums[l])
                s-=nums[l]
                
                l+=1
                    
                # print(s, res, nums[l:r+1])
            r+=1
            # print("here", nums[l:r+1])

        if res==9999999:
            return 0
        else:
            return res
            
            
                

                         