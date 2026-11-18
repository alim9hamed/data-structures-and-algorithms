class Stack:

    def __init__(self,initail_capacity: int= 1):

        self._capacity = initail_capacity
        self._array = [None]* initail_capacity
        self._length = 0
        self._top = -1

    def double_size(self):

        assert self._length == self._capacity

        old_array = self._array
        self._capacity *= 2
        self._array = [None]* self._capacity

        for i in range(self._length):
            self._array[i] = old_array[i]

        assert self._capacity >= self._length

    
    def halve_size(self):
        
        assert self._capacity > 1 and self._length <= self._capacity //4

        old_array = self._array
        self._capacity //= 2
        self._array = [None]* self._capacity

        for i in range(self._length):
            self._array[i] = old_array[i]

        assert self._capacity >= self._length

    def __str__(self):

        return str(self._array[:self._top+1])
    
    def __repr__(self):
        
        return f"Stack( Max_Length({self._capacity}), Top({self._top}), StackBasedFixedArray({self._array}))"
    
    def is_empty(self):
        return self._top == -1
    
    def is_full(self):
        return self._top == self._capacity -1
    
    def push(self, value):

        
        if self.is_full():
            self.double_size()
        self._top +=1
        self._length +=1
        self._array[self._top] = value
    
    def pop(self):

        if self.is_empty():
            raise ValueError("Stack Underflow")
        
        value = self._array[self._top]
        self._array[self._top] = None
        self._length -=1
        self._top -=1

        if self._capacity > 1 and self._length <= self._capacity // 4:
            self.halve_size()

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
print(repr(ack))
print(ack)
ack.pop()
ack.pop()
ack.pop()
ack.pop()
ack.pop()
ack.pop()
print("@@@@@ After Poping @@@@@","\n")
print(ack)

print("@@@@@ Debuging Representaion @@@@@","\n")
print(repr(ack))
ack.print()

print(repr(ack))

        
