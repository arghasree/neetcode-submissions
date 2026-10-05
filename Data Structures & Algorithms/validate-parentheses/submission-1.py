class Solution:
    def isValid(self, s: str) -> bool:
        res=[]
        for i in s:
            if i in ['(', '{', '[']:
                res.append(i)
            else:
                if len(res)==0:
                    return False 
                if i=='}' and not res.pop()=='{':
                    return False
                if i==']' and not res.pop()=='[':
                    return False 
                if i==')' and not res.pop()=='(':
                    return False 
        if len(res)==0:
            return True
        else:
            return False 