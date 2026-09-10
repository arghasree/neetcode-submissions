class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Rotate array with two pointers 
        k=k%len(nums)
        l=0
        r = len(nums)-1
        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            l+=1
            r-=1
        
        # whole array is not reversed 
        # we will again reverse till k-1 and then reverse the rest of nums back 
        l=0
        r=k-1
        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            l+=1
            r-=1

        l=k
        r=len(nums)-1 

        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            l+=1
            r-=1
        



        # 0 -> 0+k = 4 
        # 1-> 5 
        # 2-> 6
        # 3 -> 7
        # 4 -> 8%8=0
        # 5 -> 9%8 =1 
        # [1, 2, 3, 4] k=3
        # [2, 3, 4, 1]

        # [1,2,3,4,5,6,7,8] , k=3
        # [4,2,3,1,5,6,7,8]
        # [4,5,3,1,2,6,7,8]
        # [4,5,6,1,2,3,7,8] stop here at i = k
        # [7,5,6,1,2,3,4,8]
        # [7,8,6,1,2,3,4,5]
        # if k==0:
        #     return 
        # n = len(nums)
        # i=0
        # point=0
        # once=True
        # temp=None
        # while i<n:
        #     if n/k==2 and once:
        #         i+=k
        #         once=False
        #     print(nums, point)
        #     to_go = (point+k)%n if (point+k)>=n else point+k
            
        #     if temp is None:
        #         print(nums[point],'is going to', to_go)
        #         temp = nums[to_go]
        #         nums[to_go] = nums[point]
        #     else:
        #         print(temp,'is going to', to_go)
        #         nums[to_go]=temp
        #     print('new nums', nums)

        #     to_to_go = (to_go+k)%n if (to_go+k)>=n else to_go+k
        #     print(temp, 'is going to', to_to_go)
        #     if to_to_go==point:
        #         point+=1
        #     else:
        #         point=to_to_go
                
        #     i+=1
        #     # temp2=nums[to_to_go]
            
        #     temp, nums[to_to_go] = nums[to_to_go], temp
        #     print('end of loop nums', nums)
        #     print('holding', temp)
        #     print('point is now',point)

        

        