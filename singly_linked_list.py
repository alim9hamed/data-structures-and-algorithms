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
    
    
class SinglyLinkedList:

    def __init__(self):
        
        self._head = None
    
    def __len__(self):
        
        return len(self.traverse(lambda x: x))

    def traverse(self,functor):

        result =[]
        current = self._head
        while current is not None:
            result.append(functor(current.data()))
            current = current.next()
        return result
    def __repr__(self):
        
        return f"SinglyLinkedList({"->".join(self.traverse(repr))})"

    def __str__(self):
        
        return '->'.join(self.traverse(str))
    
    def __iter__(self):

        current = self._head

        while current is not None: # another Solution: while current:
            data = current.data()
            current = current.next()
            yield data

    def size(self):

        size = 0
        current = self._head
        while current is not None:
            size += 1
            current = current.next()
        return size
    

    def is_empty(self) -> bool:

        return self._head is None

    
    def insert_in_front(self,data):

        old_node = self._head
        self._head =Node(data, old_node)


    def insert_in_back(self,data):

        current = self._head
        if current is None:
            self._head = Node(data)
        else:
            while current.next() is not None:
                current = current.next()
            current.append(Node(data))
    
    def get(self, index):

        if index < 0:
            raise IndexError("Index must be postive!")

        current = self._head
        current_index = 0
        while current_index < index and current is not None:
            current = current.next()
            current_index += 1
        if current == None :
            raise IndexError("Index out of bounds")
        return current.data()
    
    def _search(self,target):

        current = self._head
        current_index = -1
        while current is not None:
            if current.data() == target:
                return current_index
            current = current.next()
            current_index +=1

        return None
    
    def delete(self,target):


        current = self._head
        previous = None

        while current is not None:

            if current.data() == target:
                if previous == None:
                    self._head = current.next()
                else:
                    previous.append(current.next())
                return
            previous = current
            current = current.next()

        raise ValueError(f"{target} not found in list")
    
    def delete_from_front(self):


        if self.is_empty():
            raise ValueError("list is empty, can not delete")
        data = self._head.data()
        self._head = self._head.next()
        return data






# ll = SinglyLinkedList()

# ll.insert_in_back(0)
# # # ll.delete(10)
# ll.insert_in_back(10)
# ll.insert_in_back(20)
# ll.insert_in_back(30)
# ll.insert_in_back(40)
# # ll.insert_in_back(50)
# # ll.insert_in_back(60)
# # ll.insert_in_back(70)
# # ll.insert_in_back(80)
# print("###########Before deleting###########")
# print("List:",ll)

# print("Size of list:",len(ll))
# print(repr(ll))


# # print("search on 50 in index: ",ll._search(50))



# ll.delete_from_front()
# ll.delete_from_front()
# ll.delete_from_front()
# ll.delete_from_front()
# ll.delete_from_front()
# # ll.delete_from_front()
# # ll.delete_from_front()
# # ll.delete_from_front()
# # ll.delete_from_front()
# # ll.delete_from_front()
# print("###########After deleting###########")
# print("Size of list:",ll.size())
# print("List:",ll)
# print(repr(ll))



# # linked_list = SinglyLinkedList()
# # print(len(linked_list))