class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        """
        brute force: sort -> go one by one and if nums[i]+1!=nums[i+1], then reset the counter. else, counter+=1
        """
        if nums==[]:
            return 0

        numsSet = set(nums)

        longest = 0 
        for i in numsSet:
            if i-1 in numsSet:
                continue
            else:
                length=1
                while i+length in numsSet:
                    length+=1
                longest = max(longest, length)
        return longest

        
        
        # d={}
        # for i in nums:
        #     if i not in d:
        #         d[i]=-1

        # k=-1
        # found=False
        # print(d)
        # for i in nums:
        #     print(i)
        #     if d[i]!=-1:
        #         continue
        #     k+=1
        #     d[i]=k

        #     if i-1 in d and d[i-1]==-1: # i-1 was not traversed
        #         print(f'{i-1} found and it was not traversed')
        #         # k+=1
        #         found=True
        #         d[i-1]=k # k=new subarray
        #         d[i]=k
        #     elif i-1 in d and d[i-1]!=-1: #i-1 was traversed
        #         print(f'{i-1} found and it was traversed')
        #         d[i]=d[i-1]
                

        #     if i+1 in d and d[i+1]==-1: # i+1 was not traversed
        #         print(f'{i+1} found and it was not traversed')
        #         if not found:
        #             k+=1
        #         found=False
        #         d[i+1]=k # k=new subarray
        #         d[i]=k
        #     elif i+1 in d and d[i+1]!=0: #i+1 was traversed
        #         print(f'{i+1} found and it was traversed')
        #         d[i]=d[i+1]

        #     if i-1 in d and i+1 in d:
        #         k-=1
        #     #     k+=1
        #     #     d[i]=k
            
        #     print(d)
        
        # max=-11
        # for i in d.values():
        #     if i>max:
        #         max=i
        
        # print(d, max)
        # return max
            

                


        

        # # store everything in a hashmap
        # d={}
        # for i in nums:
        #     if i not in d:
        #         d[i]=False
        
        # first_key=nums[0]
        # k=0
        # keys_not_visited=d.copy()
        # while keys_not_visited is not {}:
        #     print(d, keys_not_visited)
        #     if first_key in d:
        #         if first_key in keys_not_visited:
        #             del keys_not_visited[first_key]
        #         else:
        #             k+=1
        #         print(f'{first_key} has been found, k={k+1}')
        #         d[first_key]=True    
        #         first_key+=1
        #         k+=1


        #     elif first_key not in d:
        #         print(f'{first_key} has not been found')
        #         if keys_not_visited:
        #             first_key=list(keys_not_visited.keys())[0]
        #             d[first_key]=True
        #             print('chosen key is', first_key, 'now looking for', first_key+1)
        #             del keys_not_visited[first_key]
        #             first_key+=1
        #         else:
        #             break
        # return k
            
        

        
        

        