#stack using linked list 
#lifo

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class stack:
    def __init__(self):
        self.top=None

    def isEmpty(self):
        return self.top is None

    def push(self,data):
        newNode = Node(data)
        newNode.next=self.top
        self.top=newNode

    def pop(self):
        if self.isEmpty():
            print("Stack is empty! ")
            return
        data=self.top.data
        self.top=self.top.next
        return data

    def peek(self):
        if self.isEmpty():
            print("Stack is Empty!")
            return
        temp=self.top
        while temp is not None:
            print(temp.data, end =" ")
            temp=temp.next
        print()


s=stack()
s.push(10)
s.push(20)
s.push(30)

s.peek()
s.pop()