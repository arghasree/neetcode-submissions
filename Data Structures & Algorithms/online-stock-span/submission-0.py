class StockSpanner:

    def __init__(self):
        self.stack=[]
        

    def next(self, price: int) -> int:
        s1=[]
        k=1
        while self.stack:
            last = self.stack.pop()
            s1.append(last)
            if last<=price:
                k+=1
            else:
                break
        
        while s1:
            self.stack.append(s1.pop())
        self.stack.append(price)
        return k
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)