class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # sort the array 
        # and then take the last element if for 0 to n/2 there are more than one elements 

        nums.sort()

        if len(nums)%2==0:
            n=int(len(nums)/2) # 2 for len=4
        else:
            n=int(len(nums)//2+1) # 3 for len=5
        a=nums[0]
        # print(nums)
        # print(f'n is {n}')
        count=0
        for i in range(len(nums)):
            if nums[i]!=a:
                if count>=n:
                    return a
                a=nums[i]
                count=1
            else:
                count+=1
            # print(a, count, i)
        return a

