class MyQueue:

    def __init__(self):
        self.q1=[]
        self.q2=[]        

    def push(self, x: int) -> None:
        self.q1.append(x)
        

    def pop(self) -> int:
        # q1 has the pushed elements 
        for i in range(len(self.q1)-1):
            delete = self.q1.pop()
            self.q2.append(delete)
        
        to_return = self.q1.pop()
        for i in range(len(self.q2)):
            self.q1.append(self.q2.pop())

        return to_return 
    

    def peek(self) -> int:
        print(self.q1, self.q2)
        for i in range(len(self.q1)):
            to_add = self.q1.pop()
            self.q2.append(to_add)
            
        res=to_add

        for i in range(len(self.q2)):
            self.q1.append(self.q2.pop())

        return res

    def empty(self) -> bool:
        if len(self.q1)==0:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()