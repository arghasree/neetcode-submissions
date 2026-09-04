class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        abbadc 
        a c -> delete a -> bbadc 
        |----> delete c -> abbad
        Then check for pallindrom normally 
        """
        # l =0
        # r= len(s)-1
        # s.lower()
        # found=False
        # left=False
        # check=False
        # while l<r:
        #     # print(s, s[l], s[r])
        #     while l<r and not s[l].isalnum():
        #         l+=1
        #     while r>l and not s[l].isalnum():
        #         r-=1
        #     # print('removing non alpha', s, s[l], s[r])
        #     if s[l]!=s[r]:
        #         # print('Not same')
        #         if check: # last iteration left was checked 
        #             # time to check for the right 
        #             r-=1
        #             l-=1 # reseting the left counter
        #             found=True
        #             check=False # so that it does not come here again
        #             # print('2nd branch, new r', r, s[r])
        #             continue
        #         if not found:
        #             # left has not been explored 
        #             l+=1
        #             check=True 
        #             # print('1st branch, new l', l, s[l])
        #             continue
        #         else:
        #             return False
        #     else:
        #         if check:
        #             found=True
        #         l+=1
        #         r-=1
            


        # return True



        l =0
        r= len(s)-1
        s.lower()
        found=False
        left=False
        right=False
        while l<r:
            print(s, s[l], s[r])
            while l<r and not s[l].isalnum():
                l+=1
            while r>l and not s[l].isalnum():
                r-=1
            # print('removing non alpha', s, s[l], s[r])
            if s[l]!=s[r]:
                print(found)
                if not found:
                    if s[l+1]==s[r]:
                        print('left increased', s[l+1], s[r])
                        l+=1
                        found=True
                        left=True
                        continue
                    elif s[r-1]==s[l]:
                        print('right decreased', s[l], s[r-1])
                        r-=1
                        found=True
                        right=True
                        continue
                    print('not equal and therefore returning false')
                    return False
                else:
                    if left and not right:
                        l-=1
                        r-=1
                        right=True
                        continue
                    elif right and not left:
                        r+=1
                        l-=1
                        left=True
                        continue
                    elif left and right:
                        return False
            
            l+=1
            r-=1
            


        return True
                

                
        