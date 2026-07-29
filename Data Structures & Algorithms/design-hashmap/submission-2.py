

class MyHashMap:

    def __init__(self):
        self.keys=[]
        self.values=[]
        

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.keys)):
            if self.keys[i]==key:
                self.values[i]=value
                return None
        self.keys.append(key)
        self.values.append(value)
        return None
        

    def get(self, key: int) -> int:
        for i in range(len(self.keys)):
            if self.keys[i]==key:
                return self.values[i]
        return -1
        
        

    def remove(self, key: int) -> None:
        k=False
        for i in range(len(self.keys)):
            if self.keys[i]==key:
                self.keys[-1], self.keys[i]=self.keys[i],self.keys[-1]
                self.values[-1], self.values[i]=self.values[i],self.values[-1]
                self.keys.pop()
                self.values.pop()
                return None






"""
class Node:
    def __init__(self, value):
        self.value=value
        self.next=None

class MyHashMap:

    def __init__(self):
        self.head=Node(None)

    def put(self, key: int, value: int) -> None:
        temp_head=self.head
        if key==1:
            temp_head.value=value
        else:
            i=1
            while i<key-1 and temp_head.next is not None:
                temp_head=temp_head.next
                i+=1
            if temp_head.next is not None:
                temp_head.next.value=value
            else:
                temp_head.next=Node(value)
        

    def get(self, key: int) -> int:
        i=1
        temp_head=self.head
        while i<key and temp_head.next is not None:
            temp_head=temp_head.next
            i+=1
        if i!=key:
            return -1
        return temp_head.value
        

    def remove(self, key: int) -> None:
        i=1
        temp_head=self.head
        while i<=key:
            print('i=',i)
            if i==key-1:
                print('inside')
                print(i, key, temp_head.value)
                self.pr()
                if temp_head.next.next is not None:
                    temp_head.next=temp_head.next.next
                    self.pr()
                else:
                    temp_head.next=None
            else:
                temp_head=temp_head.next
                i+=1

    def pr(self):
        t=self.head
        while t!=None:
            print(t.value, end=' ')
            t=t.next
        print()
"""
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)