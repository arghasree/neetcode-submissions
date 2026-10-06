class MinStack:

    def __init__(self):
        self.l=[]
        self.min_= [2**31]

    def push(self, val: int) -> None:
        if val<=self.min_[-1]:
            self.min_.append(val)
        self.l.append(val)
        

    def pop(self) -> None:
        dele = self.l.pop()
        if dele==self.min_[-1]:
            self.min_.pop()
        

    def top(self) -> int:
        return self.l[-1]
        

    def getMin(self) -> int:
        return self.min_[-1]
        
