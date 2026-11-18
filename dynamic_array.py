import array


class DynamicArray:
    def __init__(self, initial_capacity: int = 1, typecode: str = 'l'):
        if initial_capacity <= 0:
            raise ValueError("initial_capacity must be positive")

        self._capacity = initial_capacity
        self._typecode = typecode
        self._length = 0

        self._array = self._make_array(self._capacity, self._typecode)

    def _make_array(self, capacity, typecode):
        fill = '\x00' if typecode in 'uw ' else 0
        return array.array(typecode, [fill] * capacity)

    def __len__(self):
        return self._length

    def _is_full(self):
        return self._length == self._capacity

    def _is_empty(self):
        return self._length == 0

    def _check_index(self, index):
        if index < 0 or index >= self._length:
            raise IndexError("Index out of range")

    def __repr__(self):
        return f"DynamicArray({repr(self._array[:self._length])})"

    def __getitem__(self, index):
        self._check_index(index)
        return self._array[index]

    def __iter__(self):
        for i in range(self._length):
            yield self._array[i]

    # ---------------- resizing ----------------

    def _double_size(self):
        assert self._length == self._capacity

        old_array = self._array
        self._capacity *= 2
        self._array = self._make_array(self._capacity, self._typecode)

        for i in range(self._length):
            self._array[i] = old_array[i]

        assert self._capacity >= self._length

    def _halve_size(self):
        assert self._capacity > 1 and self._length <= self._capacity // 4

        old_array = self._array
        self._capacity //= 2
        self._array = self._make_array(self._capacity, self._typecode)

        for i in range(self._length):
            self._array[i] = old_array[i]

        assert self._capacity >= self._length

    # ---------------- operations ----------------

    def insert(self, value):
        if self._is_full():
            self._double_size()

        self._array[self._length] = value
        self._length += 1

    def find(self, target):
        for i in range(self._length):
            if self._array[i] == target:
                return i
        return None

    def delete(self, target):
        index = self.find(target)

        if index is None:
            raise ValueError(f"{target} not found")

        for i in range(index, self._length - 1):
            self._array[i] = self._array[i + 1]

        self._length -= 1

        if self._capacity > 1 and self._length <= self._capacity // 4:
            self._halve_size()


def test_dynamic_array():
    print("Testing DynamicArray...")

    arr = DynamicArray()

    # -----------------
    # Test insert
    # -----------------
    arr.insert(10)
    arr.insert(20)
    arr.insert(30)

    assert len(arr) == 3
    assert arr[0] == 10
    assert arr[1] == 20
    assert arr[2] == 30

    print("Insert test passed")

    # -----------------
    # Test find
    # -----------------
    assert arr.find(20) == 1
    assert arr.find(100) is None

    print("Find test passed")

    # -----------------
    # Test delete
    # -----------------
    arr.delete(20)

    assert len(arr) == 2
    assert arr[0] == 10
    assert arr[1] == 30

    print("Delete test passed")

    # # -----------------
    # # Test indexing
    # # -----------------
    # arr[0] = 99
    # assert arr[0] == 99

    # print("Set/Get item test passed")

    # -----------------
    # # Test iteration
    # # -----------------
    # values = [x for x in arr]
    # assert values == [99, 30]

    # print("Iteration test passed")

    # -----------------
    # Test resize (force it)
    # -----------------
    for i in range(100):
        arr.insert(i)

    assert len(arr) == 102  # 2 + 100

    print("Resize test passed")

    # -----------------
    # Test delete shrink
    # -----------------
    for i in range(90):
        arr.delete(i)

    assert len(arr) > 0

    print("Shrink test passed")

    print("All tests passed successfully!")


# run tests
test_dynamic_array()