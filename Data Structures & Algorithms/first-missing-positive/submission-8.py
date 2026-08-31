class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        d={}
        for i in range(1, len(nums)+1):
            d[i]=0
        for i in nums:
            if i in d:
                d[i]=1
        for i in d:
            if d[i]==0:
                return i

        return i+1




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

        

            

        