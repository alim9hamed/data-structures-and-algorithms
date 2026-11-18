class PriorityQueue:

    def __init__(self, max_size):
        if max_size <= 0:
            raise ValueError("Max Size must be positive")

        self._max_size = max_size
        self._data = [None] * max_size
        self._length = 0


    def __str__(self):
        if self._length == 0:
            return "PriorityQueue is empty"

        result = []

        for i in range(self._length - 1, -1, -1):
            priority, value = self._data[i]
            result.append(f"(priority={priority}, value={value})")

        return " \n".join(result)
    
    def __repr__(self):
        items = []

        for i in range(self._length - 1, -1, -1):
            priority, value = self._data[i]
            items.append(f"({priority}, {value})")

        return f"PriorityQueue(max_size={self._max_size}, size={self._length}, data={items})"

    def insert(self, priority, value):

        if self._length == self._max_size:
            raise Exception("Queue is full")

        new_item = (priority, value)

        i = self._length - 1

        # shift right
        while i >= 0 and self._data[i][0] > priority:
            self._data[i + 1] = self._data[i]
            i -= 1

        self._data[i + 1] = new_item
        self._length += 1

    def top(self):
        if self._length == 0:
            raise Exception("Queue is empty")
        item = self._data[self._length - 1]
        self._data[self._length - 1] = None
        self._length -=1
        return item
    
    def peek(self):
        if self._length == 0:
            raise Exception("Queue is empty")
        return self._data[self._length - 1][1]


q = PriorityQueue(10)

q.insert(10,"Bug1")
q.insert(542,"Bug2")
q.insert(0,"Bug75")
q.insert(4158,"Bug41")
q.insert(11,"Bug12")
q.insert(10,"Bug4")
q.insert(3,"Bug6")
print(q)
print("@#"* 20,"\n")
q.top()
q.top()
q.top()
print(q)
print("@#"* 20,"\n")
print(q.peek())