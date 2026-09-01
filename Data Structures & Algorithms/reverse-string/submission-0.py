class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        for i in range(len(s)//2):
            """
            if len is even say 4, it will go till 0,1,
            if len is odd say 5, it will go till 0,1, which is fine since index 3 character will not move
            """
            # what will be the swapping index:
            #  0 will be swapped with len(s)-1
            # 1 with len(s)-2
            s[i], s[len(s)-1-i] = s[len(s)-1-i], s[i]
            
        