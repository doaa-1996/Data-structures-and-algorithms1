class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f'{self.value}'


class Stack:

    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0
    
    def isEmpty(self):
        return self.top == None

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node
        self.length += 1

    def pop(self):
        if self.length <= 0:
            print('nothing to pop')
            return
        
        temp = self.top
        self.top = self.top.next
        popped = temp.value
        self.length -= 1
        return popped

    def peek(self):
        if self.length <= 0:
            print('nothing to peek')
            return
        print(self.top.value)
        return self.top.value


class Queue:

    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    def isEmpty(self):
        return self.front == None

    def enqueue(self, value):
        self.length += 1
        new_node = Node(value)

        if self.rear == None:
            self.front = self.rear = new_node

            return

        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        self.length -= 1

        if self.isEmpty():
            self.queue = []
            print('queue is empty')
            return self.queue

        temp = self.front
        self.front = temp.next

        if self.front == None:
            self.rear = None

        return str(temp.value)

    def peek(self):
        return self.front.value

class PseudoQueue:
  def __init__(self):
    self.main_stack = Stack()
    self.helper_stack = Stack()
  
  def enqueue(self, value):

    while self.main_stack.length != 0:
      current = self.main_stack.pop()
      self.helper_stack.push(current)
    
    self.helper_stack.push(value)

    while self.helper_stack.length != 0:
      current = self.helper_stack.pop()
      self.main_stack.push(current)
    
  
  def dequeue(self): 
    if self.main_stack.top: 
      return self.main_stack.pop()
    
    return None

q = PseudoQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
