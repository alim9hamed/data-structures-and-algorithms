class Stack:

    def __init__(self,max_length: any= 10):

        self._max_size = max_length
        self._array = [None]* max_length
        self._top = -1

    
    def __str__(self):

        return str(self._array[:self._top+1])
    
    def __repr__(self):
        
        return f"Stack( Max_Length({self._max_size}), Top({self._top}), StackBasedFixedArray({self._array}))"
    
    def is_empty(self):
        return self._top == -1
    
    def is_full(self):
        return self._top == self._max_size -1
    
    def push(self, value):
        
        if self.is_full():
            raise OverflowError("Stack Overflow.")
        self._top +=1
        self._array[self._top] = value
    
    def pop(self):

        if self.is_empty():
            raise ValueError("Stack Underflow")
        
        value = self._array[self._top]
        self._array[self._top] = None
        self._top -=1

        return value
    def print(self):
        for i in range(self._top,0,-1):
            print( "<<|",self._array[i],"|>>","\n")
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
# ack.push(110)
print("@@@@@ Before Poping @@@@@","\n")
print(ack)
ack.pop()
ack.pop()
ack.pop()
ack.pop()
print("@@@@@ After Poping @@@@@","\n")
print(ack)

print("@@@@@ Debuging Representaion @@@@@","\n")
print(repr(ack))
ack.print()



        
