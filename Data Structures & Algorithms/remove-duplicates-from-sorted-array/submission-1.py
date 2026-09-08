class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=r=-1
        for i in range(1, len(nums)):
            # if i>=l and i<=r:
            #     continue
            # print(nums, l, r)
            if l==-1:
                if nums[i]==nums[i-1]:
                    l=i
                    r=i
                continue

            if nums[i]!=nums[l-1]: 
                nums[l], nums[i] = nums[i], nums[l]
                r+=1
                l+=1
            else:
                r+=1

        # print(nums)
        if l==-1:
            return len(nums)
        return l
            

        