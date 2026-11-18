class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LL:
    def __init__(self):
        self.head = None
        self.size = 0

    def create(self):
        n = int(input("Enter the size of linked list: "))

        for i in range(1, n + 1):
            val = int(input(f"Enter the value of Node {i}: "))
            newNode = Node(val)

            if self.head is None:
                self.head = newNode
            else:
                temp = self.head

                while temp.next is not None:
                    temp = temp.next

                temp.next = newNode
                newNode.prev = temp

            self.size += 1

    def printll(self):
        if self.head is None:
            print("The Linked List is empty!")
            return

        temp = self.head

        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next

        print()

    def insert(self):
        pos = int(input("Enter the position to insert: "))
        val = int(input("Enter the value of new Node: "))

        if pos < 1 or pos > self.size + 1:
            print("Invalid position!")
            return

        newNode = Node(val)

        if pos == 1:
            newNode.next = self.head

            if self.head is not None:
                self.head.prev = newNode

            self.head = newNode

        else:
            temp = self.head
            p = 1

            while p < pos - 1:
                temp = temp.next
                p += 1

            newNode.next = temp.next
            newNode.prev = temp

            if temp.next is not None:
                temp.next.prev = newNode

            temp.next = newNode

        self.size += 1
        print("Node inserted successfully!")


    def del_node(self):
        val = int(input("Enter the value to be deleted: "))
        if self.head is None:
            print("Linked List Is Empty!")
            return

        temp = self.head
        while temp is not None and temp.data != val:
            temp = temp.next

        if temp is None:
            print("Value not found!")
            return
        if temp == self.head:
            self.head = temp.next
            if self.head is not None:
                self.head.prev = None
        else:
            temp.prev.next = temp.next
            if temp.next is not None:
                temp.next.prev = temp.prev

        print("Node deleted successfully!")


            
    def reverse(self):
        temp=self.head
        while temp.next:
            temp=temp.next
        while temp:
            print(temp.data, end=" ")
            temp=temp.prev

    def countOccur(self):
        val=int(input("Enter the number to count: "))
        if self.head is None:
            print("The Linked List is empty!")
            return

        temp = self.head
        count=0
        while temp is not None:
            if temp.data==val:
                count+=1
            temp = temp.next
        print(f"{val} occured {count} times!")


ll = LL()

ll.create()
# ll.insert()
ll.printll()
ll.countOccur()
# ll.reverse()
# ll.del_node()
# ll.printll()

