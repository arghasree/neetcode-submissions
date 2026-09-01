class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0; r= len(s)-1
        s=s.lower()

        while l<r:
            # print(l, s[l], self.check_ascii(s[l]), self.check_ascii(s[r]), r, s[r])
            while l<len(s) and not self.check_ascii(s[l]):
                l+=1
            while r>0 and not self.check_ascii(s[r]):
                r-=1
            # print(s[l], s[r])
            if l<r and s[l]!=s[r]:
                return False
            l+=1
            r-=1
        
        return True

            
    

    def check_ascii(self, a):
        # 97-122 
        # 65-90
        # 48-57
        a=ord(a)
        if a<=122 and a>=97: 
            return True
        # elif a<=90 and a>=65:
        #     return True
        elif a<=57 and a>=48:
            return True
        return False

     
        