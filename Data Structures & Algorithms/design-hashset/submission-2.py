class MyHashSet:

    def __init__(self):
        self.d={}
        

    def add(self, key: int) -> None:
        self.d[key]=''
        

    def remove(self, key: int) -> None:
        # print(f'Dictionary is {self.d}')
        # print(f'Removed {key}')
        if key in self.d:
            del self.d[key]

        

    def contains(self, key: int) -> bool:
        return key in self.d
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)