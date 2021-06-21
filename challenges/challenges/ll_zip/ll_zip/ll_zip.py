class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
 
  
  
def printList(msg, head):
    print(msg, end='')

    ptr = head
    while ptr:
        print(ptr.data, end=" —> ")
        ptr = ptr.next

    print("None")

        

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
    
  

 
def zipLists(a, b):
 
    dummy = Node()
    tail = dummy
 
    while True:
        if a is None:
            tail.next = b
            break
 
        elif b is None:
            tail.next = a
            break
 
        else:
            tail.next = a
            tail = a
            a = a.next
 
            tail.next = b
            tail = b
            b = b.next
 
    return dummy.next
 
 
if __name__ == '__main__':
    linklist = LinkedList()
    a = b = None
    for i in reversed(range(7, 12, 2)):
        a = Node(i, a)

    for i in reversed(range(2, 7, 2)):
        b = Node(i, b)

    printList("First List: ", a)
    printList("Second List: ", b)

    head = zipLists (a, b)
    printList("After merging: ", head)

