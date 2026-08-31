class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # SOLN 1
        # print(nums)
        for i in range(len(nums)):
            if nums[i]>len(nums) or nums[i]<1:
                nums[i]=0
        i=0
        j=0
        while i<len(nums):
            # print(nums, i)
            temp = nums[i]
            if temp==nums[temp-1] and temp-1!=i:
                # nums[i] should be same as i 
                # if it is not that means nums[i] should be 0
                nums[i]=0
                i+=1
         
            elif temp!=0 and temp!=i+1:
                # print(f'replacing {nums[temp-1]} with {temp}' )
                a = nums[temp-1]
                nums[temp-1]=temp
                if a!=0:
                    nums[i]=a
                    # print(nums, a, i, 'here')
                else:
                    nums[i]=a
                    i+=1
            else:
                i+=1
            # j+=1
        # print(nums, i)

        for i, n in enumerate(nums):
            # print(n)
            if n==0:
               return i+1

        return n+1 

            


        
        # SOLN 2: WORKED BUT O(N) SPACE
        # d={}
        # for i in range(1, len(nums)+1):
        #     d[i]=0
        # for i in nums:
        #     if i in d:
        #         d[i]=1
        # for i in d:
        #     if d[i]==0:
        #         return i

        # return i+1



        # SOLN 1 : DID NOT WORK
        # d={}
        # min_=2**31
        # max_=-2**31
        # last=None
        # found_1=False
        # for i, n in enumerate(nums):
            
        #     if n==1:
        #         found_1=True
        #     if n<1:
        #         if max_==-2**31 or max_<1:
        #             max_=n
        #         if min_==2**31 or min_<1:
        #             min_=n
        #         print('n<1 and max_, min_ = ', max_, min_)
        #         if last is None:
        #             last=None
        #         continue
        #     if i==0:
        #         last=n 
        #         if n<min_:
        #             min_=n
        #         if n>max_:
        #             max_=n
        #         d[n]=1
        #         continue

        #     if last is not None and last+1==n:
        #         d[last]=1
        #         d[n]=1
        
        #     elif n in d:
        #         d[n]=1

        #     else:
        #         d[n]=1
        #         if last is not None and last<n:
        #             for j in range(last+1,n):
        #                 if j not in d:
        #                     d[j]=0
        #         if last is not None and last>n:
        #             for j in range(n+1,last):
        #                 if j not in d:
        #                     d[j]=0
        #     last=n
        #     if n<min_:
        #         min_=n

        #     if n>max_:
        #         max_=n
        # #     print(n, d)

        # # print(d)
        # ans=None
        # for i in d:
        #     if d[i]==1:
        #         continue
        #     else:
        #         ans=i

        # # print(max_, min_)
        # if min_!=1 and not found_1:
        #     return 1
        # else:
        #     if ans is None:
        #         if min_-1>0:
        #             return min_-1
        #         else:
        #             return max_+1
        #     else:
        #         return ans

        

            

        