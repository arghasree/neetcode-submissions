class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        # Bubble sort:
        # for i in range(len(nums)):
        #     for j in range(1,len(nums)-i):
        #         # print(i,j,nums)
        #         if nums[j-1]>nums[j]:
        #             nums[j-1], nums[j]=nums[j], nums[j-1]

        # return nums

        # Merge sort:
        return self.mergesort(nums,0,len(nums))
            




    def merge(self, arr, l, m, r):
        left=arr[l:m+1]
        right=arr[m+1:r+1]

        i=l # NOTE THIS
        i_left=0
        i_right=0

        while i_left<len(left) and i_right<len(right):
            if left[i_left]<=right[i_right]:
                arr[i]=left[i_left]
                i_left+=1
            else:
                arr[i]=right[i_right]
                i_right+=1
            i+=1

        while i_left<len(left):
            arr[i]=left[i_left]
            i_left+=1
            i+=1

        while i_right<len(right):
            arr[i]=right[i_right]
            i_right+=1
            i+=1



    def mergesort(self, arr,l,r):
        if l==r:
            return arr
        
        m = (l+r)//2
        self.mergesort(arr, l, m)
        self.mergesort(arr, m+1, r)
        self.merge(arr, l, m, r)

        return arr


        