class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class LL:
    def __init__(self):
        self.head=None

    def append(self,newNode):
        if self.head==None:
            self.head=newNode
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=newNode


    def printLL(self):
        if self.head==None:
            print("Empty Linked List: ")
        else:
            temp=self.head
            while temp!=None:
                print(temp.data, end=" ")
                temp=temp.next
            print()

    def insert(self,pos,newNode):
        if pos==1:
            newNode.next=self.head
            self.head=newNode
        else:
            p=1
            temp=self.head
            while(p!=pos-1):
                temp=temp.next
                p+=1
            newNode.next=temp.next
            temp.next=newNode

    def delete(self,pos):
        if pos==1:
            self.head=self.head.next
        else:
            prev=None
            temp=self.head
            next=None
            p=1
            while p!=pos:
                prev=temp
                temp=temp.next
                next=temp.next
                p+=1

            prev.next=next

    def deleteValue(self,value):
        if self.head.data==value:
            self.head=self.head.next
        else:
            temp=self.head
            while(temp.data!=value):
                prev=temp
                temp=temp.next
                if temp==None:
                    print(f"value {value} is not present in the Linked List")
                    return
            prev.next=temp.next
            temp=None
        


            







list1=LL()

node1= Node(10)
node2= Node(20)
node3= Node(30)
node4= Node(40)
node5= Node(454)
list1.append(node1)
list1.append(node2)
list1.append(node3)
list1.append(node4)
list1.printLL()

# list1.insert(3,node5)
list1.deleteValue(30)
list1.printLL()