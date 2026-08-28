class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        for the presum: [2, 1, 2, 4]
        then when you substract the elements to get the subarrays:
        w/o the first index: presum - presum[0] = [-1, 0, 2] & [2]
        w/o the second index: presum - presum[2] = [1, 3] & [2, 1]
        w/o the third index: presum - presum[3] = [2] & [2, 1, 2]

        So it goes till n-1 times
        Each iteration it is: presum[i+1:] - presum[i]

        To make it together I have to do:
        first iteration: 
        2
        second iteration:
        2 1 -> for the presum
        -1 (nums[i]) for the sub array 
        """
        # calculate presum:
        d={}
        presum=[]
        j=0
        for i, n in enumerate(nums):
            if i ==0:
                presum.append(n)
                d[n]=[j]
                j+=1
            else:
                presum.append(presum[-1]+n)
                if presum[-1] in d:
                    d[presum[-1]].append(j)
                    j+=1
                else:
                    d[presum[-1]]=[j]
                    j+=1
        
        ans=0
        # print(d)

        for i, n in enumerate(presum):
            to_look = n-k if n>k else k-n
            # print(n, ', n-k =', to_look, d )
            if n==k:
                # do something
                # print('A', nums[:i+1])
                ans+=1
            # if to_look in d:
            if n-k in d:
                # do something else
                for indices in d[n-k]:
                    # print(indices, i)
                    if indices!=i:
                        # print('B', nums[indices+1:i+1])
                        if nums[indices+1:i+1]:
                            ans+=1

        return ans



        