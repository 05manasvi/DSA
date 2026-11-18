class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LL:
    def __init__(self):
        self.head = None
        self.size = 0

    def create(self):
        n = int(input("Enter the size of linked list: "))

        for i in range(n):
            val = int(input(f"Enter the data for node {i + 1}: "))
            newNode = Node(val)

            if self.head is None:
                self.head = newNode
                newNode.next = self.head
            else:
                temp = self.head

                while temp.next != self.head:
                    temp = temp.next

                temp.next = newNode
                newNode.next = self.head

            self.size += 1

    def printll(self):
        if self.head is None:
            print("The Linked List is empty!")
            return

        temp = self.head

        while True:
            print(temp.data, end=" ")
            temp = temp.next

            if temp == self.head:
                break

        print()

    def insert (self,pos):
        X=int(input("Enter the value of new node: "))
        newNode=Node(X)
        if self.head is None:
            newNode.next = self.head
            self.head = newNode
        
           


ll = LL()

if ll.head is not None:

    
    print("Linked List already exists!")
else:
    ll.create()

ll.printll() 