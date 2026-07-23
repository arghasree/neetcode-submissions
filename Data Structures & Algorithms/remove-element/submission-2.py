class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # count=0
        n=len(nums)
        # i=0
        # while True:
        #     if i==n-count:
        #         break
        #     if nums[i] == val:
        #         for j in range(i,n-1):
        #             nums[j]=nums[j+1]
        #         nums[-1]=val
        #         count+=1
        #     else:
        #         i+=1
            
        # return n-count

        k=0
        for i in range(n):
            if nums[i]!=val:
                nums[k]=nums[i]
                k+=1

        return k