class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
            
        # assuming word1 is bigger:
        ans=[]
        for i in range(len(word1)):
            ans.append(word1[i])
            if len(word1)>len(word2):
                if i<len(word2):
                    ans.append(word2[i])
            else:
                ans.append(word2[i])
                if i==len(word1)-1:
                    ans.extend(word2[i+1:])


        return ''.join(ans)

        