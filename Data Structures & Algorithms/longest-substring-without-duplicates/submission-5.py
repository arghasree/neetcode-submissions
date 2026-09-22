class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l =0 
        r=0
        max_len=0
        d={}

        while r<len(s):
            # print(s, l, r, s[r],d)
            letter = s[r]
            if letter not in d:
                d[letter]=r
            else:
                last_index=d[letter]
                while l<=last_index:
                    del d[s[l]]
                    l+=1
                    # print(d, l)
                # l=d[letter]+1
                # d[letter]=r
                d[letter]=r
            # print(l, r, r-l+1, max_len)
            max_len = max(max_len, r-l+1)

            r+=1
            # print(s, l, r)
            
        return max_len
        
