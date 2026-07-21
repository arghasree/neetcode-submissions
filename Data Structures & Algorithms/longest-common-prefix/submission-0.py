class Solution:
    def find_inter(self, word, next_word):
        if len(next_word)>len(word):
            A=next_word
            B=word
        else:
            A=word
            B=next_word
        
        i=0
        while True:
            if i==len(B):
                break
            if B[i]==A[i]:
                i+=1
            else:
                return i

        return i

            



    def longestCommonPrefix(self, strs: List[str]) -> str:
        # brute force:
        # maximum length word and then I can go through each of the characters, 
        # go to the same index of the other elements 
        # for i in range(max len):
        # for j in range len(strs):
        # if strs[j][i] is not same as max_word[i]:
        # return i 

        # take a word 
        # go to the next word
        # see what is common between them 
        # take the intersection and go to the next word. 

        prev_word=""
        for i, word in enumerate(strs):
            # print(i)
            # if i==len(strs):
            #     break
            if i==0:
                prev_word=word
                continue
            else:
                len_of_inter = self.find_inter(prev_word, word)
                # print(prev_word, word, len_of_inter)
                if len_of_inter>0:
                    prev_word=word[:len_of_inter]
                else:
                    return ""
        return prev_word

            

