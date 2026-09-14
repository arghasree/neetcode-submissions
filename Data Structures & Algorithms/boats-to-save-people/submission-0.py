class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # 2 pointer approach 
        people.sort()
        print(people)
        l=0; r=len(people)-1
        ans=0
        while people[r]==limit:
            # print('found at', r, people[r])
            r-=1
            ans+=1

        while l<r:
            if people[l]+people[r]<=limit:
                while people[l]+people[r]<limit:
                    l+=1
                # res = people[:l] + [people[r]] 
                # print('ans found at', people[l], people[r])
                ans+=1
                l+=1
                r-=1
            if people[l]+people[r]>limit:
                # print('ans not found so, search reduced to', people[l:r])
                ans+=1
                r-=1

        return ans

            