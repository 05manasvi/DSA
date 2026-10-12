class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # 1. Create a linked list
    def create_list(self):
        count = int(input("How many nodes do you want? "))

        for i in range(count):
            value = int(input(f"Enter value for node {i + 1}: "))
            self.add_end(value)

    # Helper method to append a node
    def add_end(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    # 2. Display all node values
    def display(self):
        current = self.head

        if current is None:
            print("The list is empty.")
            return

        while current:
            print(current.value, end=" -> ")
            current = current.next

        print("None")

    # 3. Insert a node at a given position
    def insert_at(self):
        value = int(input("Enter the value: "))
        position = int(input("Enter position (starting from 1): "))

        if position < 1:
            print("Invalid position.")
            return

        new_node = Node(value)

        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head

        for _ in range(position - 2):
            if current is None:
                print("Invalid position.")
                return
            current = current.next

        if current is None:
            print("Invalid position.")
            return

        new_node.next = current.next
        current.next = new_node

    # 4. Find the middle node
    def find_middle(self):
        slow = self.head
        fast = self.head

        if self.head is None:
            print("The list is empty.")
            return

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        print("Middle node value:", slow.value)

    # 5. Delete a node at a given position
    def delete_at(self):
        position = int(input("Enter position to delete: "))

        if position < 1 or self.head is None:
            print("Invalid position or empty list.")
            return

        if position == 1:
            self.head = self.head.next
            print("Node deleted.")
            return

        current = self.head

        for _ in range(position - 2):
            if current.next is None:
                print("Invalid position.")
                return
            current = current.next

        if current.next is None:
            print("Invalid position.")
            return

        current.next = current.next.next
        print("Node deleted.")

    # 6. Reverse the linked list
    def reverse_list(self):
        previous = None
        current = self.head

        while current is not None:
            following = current.next
            current.next = previous
            previous = current
            current = following

        self.head = previous
        print("List reversed.")

    # 7. Sum every two consecutive node values
    def pair_sums(self):
        current = self.head

        if current is None or current.next is None:
            print("At least two nodes are required.")
            return

        print("Sums of consecutive pairs:")

        while current.next is not None:
            total = current.value + current.next.value
            print(f"{current.value} + {current.next.value} = {total}")
            current = current.next


# Main menu
linked_list = LinkedList()

while True:
    print("\n===== SINGLY LINKED LIST =====")
    print("1. Create Linked List")
    print("2. Display Linked List")
    print("3. Insert Node")
    print("4. Find Middle Node")
    print("5. Delete Node")
    print("6. Reverse Linked List")
    print("7. Sum Consecutive Nodes")
    print("8. Exit")

    try:
        option = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if option == 1:
        if linked_list.head is None:
            linked_list.create_list()
        else:
            print("The list already contains nodes.")

    elif option == 2:
        linked_list.display()

    elif option == 3:
        linked_list.insert_at()

    elif option == 4:
        linked_list.find_middle()

    elif option == 5:
        linked_list.delete_at()

    elif option == 6:
        linked_list.reverse_list()

    elif option == 7:
        linked_list.pair_sums()

    elif option == 8:
        print("Program ended.")
        break

    else:
        print("Invalid choice. Try again.")