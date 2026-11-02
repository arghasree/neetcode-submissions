class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r=0, len(nums)-1

        while l<=r:
            m = (l+r)//2
            print(nums[l:m+1], nums[m+1:r+1])
            if nums[m]>target:
                r=m-1
            elif nums[m]<target:
                l=m+1
            else:
                return m 
        if target<=nums[m]:
            return m
        else:
            return m+1
        