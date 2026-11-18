from math import floor, sqrt
from decimal import Decimal


class Node:
    def __init__(self, key, value):
        self._key = key
        self._value = value
        self._next = None


class HashTable:

    __A__ = Decimal((sqrt(5) - 1) / 2)

    def __init__(self, Buckets):
        if Buckets <= 0:
            raise ValueError("Buckets must be positive")

        self._m = Buckets
        self._size = 0
        self._data = [None] * Buckets

    def __str__(self):
        elements = []

        for bucket in self._data:
            current = bucket

            while current:
                elements.append((current._key, current._value))
                current = current._next

        return str(elements)

    def _hash(self, key):
        key_hash = hash(key)

        return floor(
            abs(
                self._m
                * ((Decimal(key_hash) * self.__A__) % 1)
            )
        )

    def insert(self, key, value):
        index = self._hash(key)

        if self._data[index] is None:
            self._data[index] = Node(key, value)
            self._size += 1
            return

        current = self._data[index]

        while current:
            if current._key == key:
                current._value = value
                return

            current = current._next

        new_node = Node(key, value)
        new_node._next = self._data[index]
        self._data[index] = new_node
        self._size += 1

    def search(self, key):
        index = self._hash(key)

        current = self._data[index]

        while current:
            if current._key == key:
                return current._value

            current = current._next

        raise KeyError(f"Key '{key}' not found")

    def delete(self, key):
        index = self._hash(key)

        current = self._data[index]
        previous = None

        while current:

            if current._key == key:

                if previous is None:
                    self._data[index] = current._next
                else:
                    previous._next = current._next

                self._size -= 1
                return

            previous = current
            current = current._next

        raise KeyError(f"Key '{key}' not found")

    def __contains__(self, key):
        try:
            self.search(key)
            return True
        except KeyError:
            return False

    def __len__(self):
        return self._size


if __name__ == "__main__":

    ht = HashTable(5)

    ht.insert("apple", 3)
    ht.insert("banana", 2)
    ht.insert("cherry", 5)

    print("apple" in ht)
    print("durian" in ht)

    print(ht.search("banana"))

    ht.insert("banana", 4)
    print(ht.search("banana"))

    print(ht)

    ht.delete("apple")

    print(ht)
    print(len(ht))