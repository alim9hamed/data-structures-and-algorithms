from typing import Any


class Heap:

    def __init__(self, elements: list[Any] = None, elements_priority=lambda x: x):

        self._priority = elements_priority

        if elements is not None and len(elements) > 0:
            self.heapify(elements)
        else:
            self._elements = []

    def __len__(self):
        return len(self._elements)

    def __str__(self):
        return str(self._elements)

    def is_empty(self):
        return len(self) == 0

    def has_lower_priority(self, element_1, element_2):
        return self._priority(element_1) < self._priority(element_2)

    def has_higher_priority(self, element_1, element_2):
        return self._priority(element_1) > self._priority(element_2)

    def left_child_index(self, index):
        return index * 2 + 1

    def parent_index(self, index):
        return (index - 1) // 2

    def first_leaf_index(self):
        return len(self) // 2

    def highest_priority_child_index(self, index):

        first_index = self.left_child_index(index)

        if first_index >= len(self):
            return None

        if first_index + 1 >= len(self):
            return first_index

        left = self._elements[first_index]
        right = self._elements[first_index + 1]

        if self.has_higher_priority(left, right):
            return first_index
        else:
            return first_index + 1

    def push_down(self, index):

        element = self._elements[index]
        current_index = index

        while True:

            child_index = self.highest_priority_child_index(current_index)

            if child_index is None:
                break

            child = self._elements[child_index]

            if self.has_lower_priority(element, child):

                self._elements[current_index] = child
                current_index = child_index

            else:
                break

        self._elements[current_index] = element

    def bubble_up(self, index):

        element = self._elements[index]

        while index > 0:

            parent_index = self.parent_index(index)
            parent = self._elements[parent_index]

            if self.has_higher_priority(element, parent):

                self._elements[index] = parent
                index = parent_index

            else:
                break

        self._elements[index] = element

    def heapify(self, elements):

        self._elements = elements[:]

        last_inner_node_index = self.first_leaf_index() - 1

        for index in range(last_inner_node_index, -1, -1):
            self.push_down(index)

    def insert(self, element):

        self._elements.append(element)
        self.bubble_up(len(self._elements) - 1)

    def top(self):

        if self.is_empty():
            raise ValueError("Empty Heap Can't pop heap.")

        if len(self) == 1:
            return self._elements.pop()

        element = self._elements[0]

        self._elements[0] = self._elements.pop()

        self.push_down(0)

        return element

    def peek(self):

        if self.is_empty():
            raise ValueError("Empty Heap.")

        return self._elements[0]



    def print_tree(self, index=0, prefix="", is_left=True):

        if index >= len(self):
            return

        right_child = 2 * index + 2
        left_child = 2 * index + 1

        if right_child < len(self):
            self.print_tree(
                right_child,
                prefix + ("│   " if is_left else "    "),
                False
            )

        print(prefix + ("└── " if is_left else "┌── ") + str(self._elements[index]))

        if left_child < len(self):
            self.print_tree(
                left_child,
                prefix + ("    " if is_left else "│   "),
                True
            )
# =========================
# TEST CODE
# =========================

print("====== CREATE HEAP ======")

heap = Heap([3, 9, 5, 1, 4, 8])

print("Heap:")
print(heap)


print("\n====== INSERT ======")

heap.insert(20)

print("After insert 20:")
print(heap)
heap.print_tree()

heap.insert(15)

print("After insert 15:")
print(heap)
heap.print_tree()

print("\n====== PEEK ======")

print("Top element:")
print(heap.peek())
heap.print_tree()

print("\n====== REMOVE TOP ======")

removed = heap.top()

print("Removed:")
print(removed)

print("Heap after removal:")
print(heap)

heap.print_tree()
print("\n====== REMOVE ALL ======")

while not heap.is_empty():
    print("Removed:", heap.top())
    # print("Heap:", heap)
    heap.print_tree()


