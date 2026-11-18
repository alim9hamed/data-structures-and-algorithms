class QueueArray:

    def __init__(self,max_size):

        if max_size <= 1:
            raise ValueError(f'Invalid size (a queue must have at least two elements): {max_size}')
        
        self._data = [None]* max_size
        self._max_size = max_size
        self._front = 0
        self._rear = max_size-1
        self._length = 0

    def __iter__(self):

        front = self._front
        count = 0

        while count < self._max_size:

            yield self._data[front]
            front = (front + 1) % self._max_size
            count +=1
        
    def __str__(self):
        return str([item for item in self if item != None ])

    def __repr__(self):
        
        return f"QueueArray({self._data}, Max_size({self._max_size}), Length({self._length}))"


    def is_full(self):

        return self._length == self._max_size
    
    def is_empty(self):

        return self._length == 0
    
    
    def enqueue(self,value):

        if self.is_full():
            raise ValueError("Full Queue!")
        else:

            self._rear = (self._rear + 1)% self._max_size
            self._data[self._rear] = value
            self._length +=1
        

    def dequeue(self):

        if self.is_empty():
            raise ValueError("Empty Queue!")
        else:
            self._data[self._front] = None
            self._front = (self._front + 1)% self._max_size
            data = self._data[self._front]
            self._length -=1
            return data


qu = QueueArray(10)

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