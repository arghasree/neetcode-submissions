class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        max_len=0
        d={}

        for r in range(len(s)):
            # print(s[l:r+1])
            if s[r] not in d:
                d[s[r]]=1
            else:
                d[s[r]]+=1
            while ((r-l+1) - max(d.values()) )> k:
                d[s[l]]-=1
                l+=1

            
            max_len = max(max_len, r-l+1)

        return max_len

















        # l=0
        # r=0
        # d={}
        # max_len = 0
        # max_char = s[0]
        # while r<len(s):
        #     if s[r] not in d:
        #         d[s[r]] =1
        #     else:
        #         d[s[r]]+=1
            
        #     # check for the no of characters to replace
        #     if d[s[r]]>d[max_char]:
        #         max_char = s[r]
        #     max_=d[max_char]
        #     diff_chars = (r-l+1) - max_ 

        #     while diff_chars>k:
        #         l+=1
        #         d[s[l]]-=1
        #         if d[max_char]<(r+l-1 - max_char)

        #     print( r-l+1, s[l:r+1])

        #     if diff_chars>k:
        #         # print(d, s[l:r+1])
        #         if s[l]==max_char:
        #             while d[max_char]>0:
        #                 print(d)
        #                 d[s[l]]-=1
        #                 l+=1
        #                 if l>r:
        #                     l-=1
        #                     break
        #             max_char = s[l]
                    
        #         else:
        #             d[s[l]]-=1
        #             l+=1 
        #         # max_len = max(max_len, r-l+1)
        #     # after this one has been removed
        #     max_len = max(max_len, r-l+1)
        #     r+=1
        #     print('max_len is', max_len)
            

        return max_len
        
        