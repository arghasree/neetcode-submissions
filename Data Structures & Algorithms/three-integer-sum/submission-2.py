class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=set()
        print(nums)
        
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue 

            if nums[i]>0:
                break 
            
            l=i+1
            r=len(nums)-1
            while l<r:
                if nums[l]+nums[r]+nums[i]==0:
                    re=[nums[i], nums[l], nums[r]]
                    ans.add(tuple(re))
                    l+=1
                    r-=1
                elif nums[l]+nums[r]+nums[i]>0:
                    r-=1
                    while r-1>l and nums[r-1]==nums[r]:
                        r-=1
                elif nums[l]+nums[r]+nums[i]<0:
                    l+=1
                    while l+1<r and nums[l+1]==nums[l]:
                        l+=1


            print(ans)
        return [list(i) for i in ans]
                