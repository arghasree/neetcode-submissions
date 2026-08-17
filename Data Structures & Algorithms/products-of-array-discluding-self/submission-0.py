class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=[]
        pre=1
        for n in nums:
            l.append(pre)
            pre*=n

        post=1
        for i in range(len(nums)-1, -1, -1):
            l[i]*=post
            post*=nums[i]

        return l
