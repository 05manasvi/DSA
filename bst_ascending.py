# BST using Linked List

class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # Insert a new node into the BST
    def insert(self, new_node):
        if self.root is None:
            self.root = new_node
        else:
            temp = self.root

            while True:
                if new_node.data < temp.data:
                    # Insert into the left subtree
                    if temp.left is None:
                        temp.left = new_node
                        return
                    else:
                        temp = temp.left
                else:
                    # Insert into the right subtree
                    if temp.right is None:
                        temp.right = new_node
                        return
                    else:
                        temp = temp.right

    # Inorder traversal: Ascending order
    def inorder(self, rt):
        if rt is None:
            return

        self.inorder(rt.left)
        print(rt.data, end=" ")
        self.inorder(rt.right)

    # Preorder traversal
    def preorder(self, rt):
        if rt is None:
            return

        print(rt.data, end=" ")
        self.preorder(rt.left)
        self.preorder(rt.right)

    # Postorder traversal
    def postorder(self, rt):
        if rt is None:
            return

        self.postorder(rt.left)
        self.postorder(rt.right)
        print(rt.data, end=" ")

    # Find minimum and maximum values
    def findminmax(self):
        if self.root is None:
            print("BST is empty")
            return

        # Find minimum
        temp = self.root
        while temp.left:
            temp = temp.left

        print("Min:", temp.data)

        # Find maximum
        temp = self.root
        while temp.right:
            temp = temp.right

        print("Max:", temp.data)

    # Count total number of nodes
    def count_nodes(self, rt):
        if rt is None:
            return 0

        return (
            1
            + self.count_nodes(rt.left)
            + self.count_nodes(rt.right)
        )


# Create BST
b1 = BST()

# Insert nodes
b1.insert(Node(100))
b1.insert(Node(10))
b1.insert(Node(450))
b1.insert(Node(0))
b1.insert(Node(65))
b1.insert(Node(300))

# Inorder traversal: Ascending order
print("\nInorder (Ascending Order):")
b1.inorder(b1.root)

# Count total nodes
print("\n\nNo of nodes:", b1.count_nodes(b1.root))

# Preorder traversal
print("\n\nPreorder:")
b1.preorder(b1.root)

# Postorder traversal
print("\n\nPostorder:")
b1.postorder(b1.root)

# Find minimum and maximum
print("\n")
b1.findminmax()