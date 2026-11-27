class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class bst:
    def __init__(self):
        self.head = None

    # INSERT NODE
    def insert(self, newNode):

        if self.head is None:
            self.head = newNode
            return

        current = self.head

        while True:

            if newNode.data < current.data:

                if current.left is None:
                    current.left = newNode
                    break
                else:
                    current = current.left

            elif newNode.data > current.data:

                if current.right is None:
                    current.right = newNode
                    break
                else:
                    current = current.right

            else:
                print("Duplicate values are not allowed")
                break

    # INORDER TRAVERSAL
    def inorder(self, root):

        if root is None:
            return

        self.inorder(root.left)
        print(root.data, end=" ")
        self.inorder(root.right)

    # POSTORDER TRAVERSAL
    def postorder(self, root):

        if root is None:
            return

        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data, end=" ")

    # PREORDER TRAVERSAL
    def preorder(self, root):

        if root is None:
            return

        print(root.data, end=" ")
        self.preorder(root.left)
        self.preorder(root.right)


    # FIND MINIMUM AND MAXIMUM
    def find_min_max(self):

        if self.head is None:
            return None, None

        minimum = self.head
        maximum = self.head

        while minimum.left is not None:
            minimum = minimum.left

        while maximum.right is not None:
            maximum = maximum.right

        return minimum.data, maximum.data

    # FIND MINIMUM NODE IN A SUBTREE
    def find_min(self, root):

        while root.left is not None:
            root = root.left

        return root

    # DELETE NODE
    def delete(self, root, value):

        if root is None:
            return None

        if value < root.data:
            root.left = self.delete(root.left, value)

        elif value > root.data:
            root.right = self.delete(root.right, value)

        else:

            # CASE 1: NO CHILD
            if root.left is None and root.right is None:
                return None

            # CASE 2: ONLY RIGHT CHILD
            elif root.left is None:
                return root.right

            # CASE 2: ONLY LEFT CHILD
            elif root.right is None:
                return root.left

            # CASE 3: TWO CHILDREN
            else:
                successor = self.find_min(root.right)

                root.data = successor.data

                root.right = self.delete(root.right, successor.data)

        return root


# MAIN PROGRAM

tree = bst()

while True:

    print("\n\n========== BST MENU ==========")
    print("1. Insert Node")
    print("2. Delete Node")
    print("3. Inorder Traversal")
    
    print("4. Preorder Traversal")
    print("5. Postorder Traversal")
    print("6. Find Minimum and Maximum")
    print("7. Exit")

    choice = int(input("Enter your choice: "))  

    if choice == 1:

        value = int(input("Enter node value: "))
        newNode = Node(value)

        tree.insert(newNode)

    elif choice == 2:

        if tree.head is None:
            print("Tree is empty")

        else:
            value = int(input("Enter value to delete: "))
            tree.head = tree.delete(tree.head, value)

            print("Node deleted (if it existed)")

    elif choice == 3:

        print("Inorder Traversal:")
        tree.inorder(tree.head)

    elif choice == 4:

        print("Preorder Traversal:")
        tree.preorder(tree.head)

    elif choice == 5:

        print("Postorder Traversal:")
        tree.postorder(tree.head)

    elif choice == 6:

        minimum, maximum = tree.find_min_max()

        if minimum is None:
            print("Tree is empty")

        else:
            print("Minimum value:", minimum)
            print("Maximum value:", maximum)

    elif choice == 7:



        print("Exiting program...")
        break




    else:
        print("Invalid choice! Please try again.")