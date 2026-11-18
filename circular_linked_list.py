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

class CircularLinkedList:

    def __init__(self):

        self._head = None

    
    def insert(self,value):

        new_node = Node(value)

        if self._head == None:
            self._head = new_node
            new_node._next = self._head
            return

        current = self._head
        while current._next != self._head:
            current = current._next

        current._next = new_node
        new_node._next = self._head

    def delete(self,Value):

        pass

    def print(self):

        if self._head == None:
            raise ValueError("@@@ Empty List @@@")
        
        current = self._head

        while current._next != self._head:
            print(current._data,"->", end=" ")
            current = current._next
        print(current)


ll = CircularLinkedList()

ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)
ll.print()