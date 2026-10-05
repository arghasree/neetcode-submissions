class MyStack:

    def __init__(self):
        self.res=deque()

    def push(self, x: int) -> None:
        self.res.append(x)
        

    def pop(self) -> int:
        # return self.res.pop() cannot do this 
        l=len(self.res)
        for i in range(l):
            deleted=self.res.popleft()
            if i!=l-1:
                self.res.append(deleted)
        return deleted
        

    def top(self) -> int:
        return self.res[-1]
        

    def empty(self) -> bool:
        if self.res==deque():
            return True
        return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()