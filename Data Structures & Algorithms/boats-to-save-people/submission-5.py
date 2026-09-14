class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # 2 pointer approach 
        people.sort()
        # print(people)
        l=0; r=len(people)-1
        ans=0
        enter=False
        while r>=0 and people[r]==limit:
            # print('found at', r, people[r])
            r-=1
            ans+=1

        while l<r:
            if people[l]+people[r]<=limit:
                s=people[l]+people[r]
                while s<limit:
                    l+=1
                    s+=people[l]+people[r]
                    enter=True
                    # print('ans found at', people[l], people[r], 'now ans is', ans+1)
                ans+=1
                if not enter:
                    l+=1
                enter=False
                r-=1
            if people[l]+people[r]>limit:
                ans+=1
                # print('ans not found so, search reduced to', people[l:r], 'now ans is', ans)
                r-=1

        if l==r:
            ans+=1

        return ans

            