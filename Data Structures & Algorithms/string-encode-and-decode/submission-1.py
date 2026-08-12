class Solution:

    def encode(self, strs: List[str]) -> str:
        total_length=0
        s=""
        print(len(strs))
        for i in strs:
            total_length+=len(i)
            s=s+self.num_2_hexstr(len(i))+i
            print(f'The length is {len(i)} = {int(self.num_2_hexstr(len(i)), 16)}')
        # total_length=self.num_2_hexstr(total_length)

        return s

    def decode(self, s: str) -> List[str]:
        # total_length = int(s[0:4], 16)
        # s=s[4:]
        l=[]
        # tot_l=0

        while len(s)>0:
            length = int(s[0:4], 16)
            s=s[4:]
            l.append(s[0:length])
            s=s[length:]
            # tot_l+=length
        # assert tot_l==total_length

        return l





    def num_2_hexstr(self, num):
        print(num)
        num=hex(num)
        num=str(num)[2:]
        if len(str(num))==1:
            num='000'+num
        elif len(str(num))==2:
            num='00'+num
        elif len(str(num))==3:
            num='0'+num
        
        print(num)
        return num

