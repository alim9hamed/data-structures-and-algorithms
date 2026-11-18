import array 


class SortedArray:

    def __init__(self,max_size: int, typecode: str ='l'):
        self._max_size = max_size
        self._length = 0
        if self._max_size <= 0:
            raise ValueError(f"MaxSize {self._max_size} must be postive, ")
        
        fill = '\x00' if typecode in 'uw' else 0
        
        self._array = array.array(typecode, [fill] * self._max_size)


    def is_full(self):

        if self._length >= self._max_size:
            raise OverflowError("SortedArray is full")
        


    def is_empty(self):
        if self._length <= 0:
            raise ValueError("SortedArray is already empty!")
    


    def __len__(self):
        return self._length
    


    def _check_index(self,value):
        if value < 0 or value >= self._max_size:
            raise IndexError(f" Value {value} out of range!")
    


    def __getitem__(self, index):
        
        self._check_index(index)
        return self._array[index]
    

    def __setitem__(self, index, value):

        self._check_index(index)
        self._array[index] = value

    def __repr__(self):
        
        return f"SortedArray({list(self._array[:self._length])})"


    def insert(self, value):

        self.is_full()

        i = self._length -1

        while i >= 0 and self._array[i]> value:
            self._array[i+1] = self._array[i]
            i -=1
        self._array[i+1] = value
        self._length +=1

        # for i in range(self._length,0, -1):
        #     if self._array[i-1] <= value:
        #         self._array[i] = value
        #         self._length +=1
        #         return
        #     else:
        #         self._array[i] = self._array[i-1]
        
        # self._array[0] = value
        # self._length += 1
    

    def binary_search(self, value):
        left = 0
        right = self._length -1

        while left <= right:
            mid_index =  (left + right) // 2

            if self._array[mid_index] == value:
                return mid_index
            elif value < self._array[mid_index]:
                right = mid_index - 1
            else:
                left = mid_index + 1

        return None
    
    def delete(self, value):

        index = self.binary_search(value)
        if index is None:
            raise ValueError(f" Unable to delete {value}, the entry is not in the array.")
        
        for i in range(index,self._length-1):
            self._array[i] = self._array[i+1]
        
        self._length -= 1
        self._array[self._length] = 0


    # def __iter__(self):
        

    #     for i in range(self._size):
    #         yield self._array[i]


arr = SortedArray(10,"i")

arr[8] = 5
arr.insert(3)
arr.insert(10)
arr.insert(0)
arr.insert(5)
arr.insert(88)
arr.insert(99)
arr.insert(544)




print(arr)

# arr.delete(55)
arr.delete(88)
print(arr)

print(arr.binary_search(544))
# print(arr._array[:arr._max_size])


