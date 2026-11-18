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

class Stack:

    def __init__(self):

        
        self._top = None

    
    def is_empty(self):
        return self._top == None
    
    
    
    def push(self, value):
        
        new_node = Node(value)
        new_node._next = self._top
        self._top = new_node

    
    def pop(self):

        if self.is_empty():
            raise ValueError("Stack Underflow")
        
        data = self._top.data
        self._top = self._top._next

        return data
    
    def print(self):
        current = self._top
        while current != None:
            print( "<<|",current._data,"|>>","\n")
            current = current._next
        print("<<|----|>>")
    
    


ack = Stack()

ack.push(10)
ack.push(20)
ack.push(30)
ack.push(40)
ack.push(50)
ack.push(60)
ack.push(70)
ack.push(80)
ack.push(90)
ack.push(100)
ack.push(110)
print("@@@@@ Before Poping @@@@@","\n")
ack.print()
ack.pop()
ack.pop()
ack.pop()
ack.pop()
print("@@@@@ After Poping @@@@@","\n")
ack.print()





        
