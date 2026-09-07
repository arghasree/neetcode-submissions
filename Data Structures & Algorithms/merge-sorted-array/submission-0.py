class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if len(nums1)==len(nums2):
            for i in range(len(nums2)):
                nums1[i]=nums2[i]


        else:
            # start from the back 
            l, r = len(nums1)-len(nums2)-1, len(nums2)-1
            zero_last = len(nums1)-1
            while r>=0 and l>=0:
                if nums2[r]<nums1[l]:
                    nums1[zero_last], nums1[l] = nums1[l], nums1[zero_last]
                    zero_last-=1
                    l-=1
                else:
                    nums1[zero_last]=nums2[r]
                    r-=1
                    zero_last-=1
                if l==zero_last:
                    l-=1
            while zero_last>=0 and r>=0:
                nums1[zero_last]=nums2[r]
                r-=1
                zero_last-=1




        
        # d={}
        # for i in range(len(nums1)-len(nums2)):
        #     d[nums1[i]]=i
        
        # i=j=0
        # while i<len(nums2):
        #     if nums1[i]<nums2[j]:
        #         i+=1
        #     else:
        #         d[nums1[i]]+=1
        #         nums1[i]=nums2[j]
        #         i+=1
        #         j+=1
        
        # nums_i=0
        # tot=0
        # for n in d:
        #     if n==nums[nums_i]:
        #         if d[n]=!nums_i: 


                

        