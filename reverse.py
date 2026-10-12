"""Singly Linked List
Linear Linked List

Medium

MODULE: ASSIGNMENT

Assl: Create a Singly Linear Linked List with following operations

Create Linked List
Traverse and print the node values
Insert node at a specific position
Find Middle node and print its value
Delete node

Reverse list
Calculate the sum of every two consecutive node values.

Constraints:

Time limit: 2000 ms

Memory limit: 256 MB
"""

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
            else:
                temp = self.head
                while temp.next is not None:
                    temp = temp.next
                temp.next = newNode

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
        value = int(input("Enter the value of new Node: "))
        pos = int(input("Enter the position of new Node (starting from 1): "))

        if pos < 1 or pos > self.size + 1:
            print("Invalid position!")
            return

        newNode = Node(value)

        if pos == 1:
            newNode.next = self.head
            self.head = newNode
        else:
            temp = self.head
            for _ in range(pos - 2):
                temp = temp.next

            newNode.next = temp.next
            temp.next = newNode

        self.size += 1

    def printMiddle(self):
        if self.head is None:
            print("Linked List is empty!")
            return

        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        print(f"The middle Node is {slow.data}!")

    def delete(self):
        if self.head is None:
            print("Linked List is empty!")
            return

        pos = int(input("Enter the position of Node to be deleted: "))

        if pos < 1 or pos > self.size:
            print("Invalid position!")
            return

        if pos == 1:
            self.head = self.head.next
        else:
            temp = self.head

            for _ in range(pos - 2):
                temp = temp.next

            temp.next = temp.next.next

        self.size -= 1

    def deleteMiddle(self):
        if self.head is None:
            print("Linked List is empty!")
            return

        if self.head.next is None:
            self.head = None
            return

        slow = self.head
        fast = self.head
        prev = None

        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next
        
    
def deleteFandL(self):
    if self.head is None:
        print("Linked List is empty!")
        return

    if self.head.next is None:
        self.head = None
        return
    
    self.head = self.head.next
    temp = self.head
    prev = None

    while temp.next is not None:
        prev = temp
        temp = temp.next

    prev.next = None



    def reverse(self):
        prev = None
        current = self.head

        while current is not None:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
    
        self.head = prev
        print("Linked List reversed!")

    def consecutiveS(self):
        if self.head is None or self.head.next is None:
            print("At least two nodes are required!")
            return

        temp = self.head
        ans = []

        while temp.next is not None:
            ans.append(temp.data + temp.next.data)
            temp = temp.next

        print("Consecutive sums are:", ans)



    
ll = LL()

while True:
    print("\n--- Linked List Menu ---")
    print("1. Create Linked List")
    print("2. Print Linked List")
    print("3. Insert Node")
    print("4. Print Middle Node")
    print("5. Delete Node")
    print("6. Reverse Linked List")
    print("7. Delete Middle Node")
    print("8. Delete first and Last Node")
    print("9. Calculate Consecutive Sums")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        if ll.head is not None:
            print("Linked List already exists!")
        else:
            ll.create()
    elif choice == 2:
        ll.printll()
    elif choice == 3:
        ll.insert()
    elif choice == 4:
        ll.printMiddle()
    elif choice == 5:
        ll.delete()
    elif choice == 6:
        ll.reverse()
    elif choice==7:
        ll.deleteMiddle()
    elif choice==8:
        ll.deleteFandL()
    elif choice == 9:
        ll.consecutiveS()
    elif choice == 10:
        print("Program terminated.")
        break
    else:
        print("Invalid choice! Try again.")
        