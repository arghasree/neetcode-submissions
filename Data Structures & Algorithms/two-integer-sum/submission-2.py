class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        l=[]
        for i, n in enumerate(nums):
            l.append([n,i])

        l.sort(key=lambda x:x[0])

        i,j=0,len(nums)-1
        while i<j:
            print(l[i], l[j])
            if l[i][0]+l[j][0]>target:
                j-=1
            elif l[i][0]+l[j][0]==target:
                return [min([l[i][1], l[j][1]]), max([l[i][1], l[j][1]])]
            else:
                i+=1

        
     
        