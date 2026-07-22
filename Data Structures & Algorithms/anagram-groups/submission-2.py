class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # check both the length and sum of ascii
        # word_sum={}
        # for word in strs:
        #     s=0
        #     for i in range(len(word)):
        #         s += ord(word[i])
        #     if s in word_sum and len(word)==len(word_sum[s][-1]):
        #         word_sum[s].append(word)
        #     else:
        #         word_sum[s]=[word]
            
        # l=[]
        # print(word_sum)
        # for s in word_sum:
        #     l.append(word_sum[s])
        d={}
        for word in strs:
            c=[0]*26
            for char in word:
                index=ord(char)-ord('a')
                c[index]+=1
            if str(c) in d:
                d[str(c)].append(word)
            else:
                d[str(c)]=[word]

        return list(d.values())
