class node:
    def __init__(self,pid,name,pr):
        self.pid=pid
        self.name=name
        self.priority=pr
        self.next=None


class PriorityQueue:
    def __init__(self):
        self.front=None

    # 1. Add Process
    def enqueue(self,new_node):
        if self.front==None:
            self.front=new_node
            return

        if self.front.priority>new_node.priority:
            new_node.next=self.front
            self.front=new_node
            return

        temp=self.front

        while temp.next and temp.next.priority<=new_node.priority:
            temp=temp.next

        new_node.next=temp.next
        temp.next=new_node

    # 2. Execute Process
    def dequeue(self):
        if self.front==None:
            print("No process available")
        else:
            temp=self.front
            print("Process executed:",temp.pid,temp.name)
            self.front=self.front.next

    # 3. View Next Process
    def display_next(self):
        if self.front==None:
            print("No process available")
        else:


            
            print("Next Process:")
            print("Process ID:",self.front.pid)
            print("Process Name:",self.front.name)
            print("Priority:",self.front.priority)

    # 4. Display All Processes
    def display(self):
        if self.front==None:
            print("No pending processes")
            return

        temp=self.front
        while temp:
            print(temp.pid,temp.name,"Priority:",temp.priority)
            temp=temp.next

    # 5. Count Processes
    def count(self):
        temp=self.front
        c=0

        while temp:
            c+=1
            temp=temp.next

        print("Total pending processes:",c)


# Main Program
pq=PriorityQueue()

while True:
    print("\n--- CPU PROCESS SCHEDULING ---")
    print("1. Add Process")
    print("2. Execute Process")
    print("3. View Next Process")
    print("4. Display All Processes")
    print("5. Count Processes")
    print("6. Exit")

    ch=int(input("Enter your choice: "))

    if ch==1:
        pid=int(input("Enter Process ID: "))
        name=input("Enter Process Name: ")
        pr=int(input("Enter Priority (1-4): "))

        if pr>=1 and pr<=4:
            pq.enqueue(node(pid,name,pr))
            print("Process added successfully")
        else:
            print("Invalid priority")

    elif ch==2:
        pq.dequeue()

    elif ch==3:
        pq.display_next()

    elif ch==4:
        pq.display()

    elif ch==5:
        pq.count()

    elif ch==6:
        print("Exiting...")
        break

    else:
        print("Invalid choice")