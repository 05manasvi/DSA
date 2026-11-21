class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class bst:
    def __init__(self):
        self.head = None

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

    def inorder(self, root):

        if root is None:
            return

        self.inorder(root.left)
        print(root.data, end=" ")
        self.inorder(root.right)

    def postorder(self, root):

        if root is None:
            return

        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data, end=" ")

    def preorder(self, root):

        if root is None:
            return
        print(root.data, end=" ")
        self.inorder(root.left)
        self.inorder(root.right)



tree = bst()

while True:
    value = int(input("Enter node value (-1 to stop): "))

    if value == -1:
        break 





    newNode  = Node(value)
    tree.insert(newNode)

print("\nInorder Traversal:")
tree.inorder(tree.head)

print("\n Postorder Traversal:")
tree.postorder(tree.head)

print("\n Preorder Traversal:")
tree.preorder(tree.head)