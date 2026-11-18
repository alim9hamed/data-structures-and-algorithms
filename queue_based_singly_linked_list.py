#  Neet to Edit
class Node:

    def __init__(self, data, new_next : Node = None):


        self._data = data
        self._next = new_next
    
    def data(self):
        return self._data
    
    def next(self):
        return self._next
    
    def has_next(self):
        return self._next is not None
    
    def append(self,new_node):
        self._next = new_node

    def __str__(self):
        
        return str(self.data())
    
    def __repr__(self):
        return repr(self.data())
    

class QueueSinglyLinkedList:

    def __init__(self):

        self._front = self._rear = None
        self._length = 0

    def __iter__(self):

        current = self._front

        while current is not None:
            yield current._data
            current = current.next()
        
    def __str__(self):
        return str(list(self))

    def __repr__(self):
        
        return f"QueueSinglyLinkedList({list(self)}, Length({self._length}))"


    def is_full(self):

        return self._length == self._max_size
    
    def is_empty(self):

        return self._length == 0
    
    
    def enqueue(self,value):
        new_node = Node(value)

        if self.is_empty():
            self._front = self._rear = new_node
        else:    
            self._rear._next = new_node
            self._rear = new_node
        self._length +=1

        if self._front is None:
            self._rear = None
        

    def dequeue(self):

        if self.is_empty():
            raise ValueError("Empty Queue!")
        else:
            data = self._front._data
            self._front = self._front._next
            self._length -=1
            return data


qu = QueueSinglyLinkedList()

qu.enqueue(10)
print(qu)
print(repr(qu))
print("@#"*20,"\n")
qu.enqueue(20)
qu.enqueue(30)
qu.enqueue(40)
qu.enqueue(50)
qu.enqueue(60)
print(qu)
print(repr(qu))
print("@#"*20,"\n")
qu.dequeue()
qu.dequeue()
qu.dequeue()
qu.dequeue()
qu.dequeue()
qu.dequeue()
print(qu)
print(repr(qu))
print("@#"*20,"\n")
qu.enqueue(40)
qu.enqueue(50)
qu.enqueue(60)
qu.enqueue(70)
qu.enqueue(80)
qu.enqueue(90)
qu.enqueue(100)
qu.enqueue(110)
qu.enqueue(120)
qu.enqueue(130)
# qu.enqueue(140)
print(qu)
print(repr(qu))
print("@#"*20,"\n")
qu.dequeue()
qu.dequeue()
qu.dequeue()
qu.dequeue()
qu.dequeue()
qu.dequeue()
qu.dequeue()
qu.dequeue()
qu.dequeue()
qu.dequeue()
print(qu)
print(repr(qu))
print("@#"*20,"\n")
# qu.dequeue()