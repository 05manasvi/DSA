
# class Stack:
#     def __init__(self):
#         self.stack = []

#     # Push an element into the stack
#     def push(self, value):
#         self.stack.append(value)
#         print(value, "pushed into stack")

#     # Pop an element from the stack
#     def pop(self):
#         if len(self.stack) == 0:
#             print("Stack is empty")
#         else:
#             print("Popped:", self.stack.pop())

#     # Display the stack
#     def display(self):
#         if len(self.stack) == 0:
#             print("Stack is empty")
#         else:
#             print("Stack:", self.stack)

#     # Reverse a string using stack
#     def reverse_string(self, string):
#         s = []

#         for ch in string:
#             s.append(ch)

#         result = ""

#         while s:
#             result += s.pop()

#         print("Reversed string:", result)

#     # Reverse the stack
#     def reverse_stack(self):
#         temp = []

#         while self.stack:
#             temp.append(self.stack.pop())

#         self.stack = temp
#         print("Stack reversed")


# # Main program
# s = Stack()

# s.push(10)
# s.push(20)
# s.push(30)

# s.display()

# s.pop()

# s.display()

# s.reverse_string("PYTHON")

# s.reverse_stack()

# s.display()


class Queue:
    def __init__(self):
        self.queue = []

    # Enqueue an element into the queue
    def enqueue(self, value):
        self.queue.append(value)
        print(value, "inserted into queue")

    # Dequeue an element from the queue
    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print("Deleted:", self.queue.pop(0))

    # Display the queue
    def display(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print("Queue:", self.queue)

    # Reverse the queue using a stack
    def reverse_queue(self):
        stack = []

        while self.queue:
            stack.append(self.queue.pop(0))

        while stack:
            self.queue.append(stack.pop())

        print("Queue reversed")

    # Merge two queues
    def merge(self, q2):
        self.queue.extend(q2.queue)
        print("Queues merged")

    # Check whether two queues are identical
    def identical(self, q2):
        if self.queue == q2.queue:
            print("Queues are identical")
        else:
            print("Queues are not identical")


# Main program
q1 = Queue()
q2 = Queue()

q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)

q2.enqueue(40)
q2.enqueue(50)

q1.display()
q2.display()

q1.dequeue()

q1.display()

q1.reverse_queue()

q1.display()

q1.merge(q2)

q1.display()

q1.identical(q2)
