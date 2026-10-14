class StockSpanner:

    def __init__(self):
        self.stack=[]
    

    def next(self, price: int) -> int:
        k=1
        while self.stack:
            print(self.stack)
            last = self.stack.pop()
            if last[0]<=price:
                k+=last[1]
            else:
                self.stack.append(last)
                break
        self.stack.append((price, k))
        return k
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)