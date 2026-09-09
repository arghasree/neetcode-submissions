class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans=set()
        print(nums)
        for i in range(len(nums)):
            f = nums[i]
            # if f>target:
            #     break
            start_of_2nd_loop = i+1
            # while (start_of_2nd_loop+1)<len(nums) and nums[start_of_2nd_loop]==nums[start_of_2nd_loop+1]:
            #     start_of_2nd_loop+=1
            # print('start of 2nd loop is', start_of_2nd_loop)
            for j in range(start_of_2nd_loop, len(nums)):
                s = nums[j]

                l, r = j+1, len(nums)-1
                while l<r:
                    # print(f,s,nums[l],nums[r], 'sum =', f+s+ nums[l] + nums[r], (l,r))
                    if f+s+ nums[l] + nums[r]==target:
                        res = [f, s, nums[l], nums[r]] 
                        ans.add(tuple(res))
                        r-=1
                        l+=1
                    elif f+s+ nums[l] + nums[r]>target:
                        r-=1
                    elif f+s+ nums[l] + nums[r]<target:
                        l+=1
                    # # look for duplicates
                    # while (l+1)<r and nums[l]==nums[l+1]:
                    #     l+=1
                    # while (r-1)>l and nums[r]==nums[r-1]:
                    #     r-=1
        
        return [list(i) for i in ans]


        