class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        for char in s:
            if char in d:
                d[char]+=1
            else:
                d[char]=1
        print(d)
        for char in t:
            if char in d:
                d[char]-=1
            else:
                return False
        print(d)
        for char in d:
            if d[char]<0 or d[char]>0:
                return False
        return True