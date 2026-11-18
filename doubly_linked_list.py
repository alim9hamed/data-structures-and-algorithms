# Need to Edit !!!!!!!!
class Node:

    def __init__(self, data):


        self._data = data
        self._next = None
        self._prev = None
    
    def data(self):
        return self._data
    
    def next(self):
        return self._next
    
    def has_next(self):
        return self._next is not None
    
    def prev(self):
        return self._prev
    
    def has_prev(self):
        return self._prev != None
    
    def append(self,next_node):
        self._next = next_node
        if next_node != None:
            next_node._prev = self

    


    def prepend(self, prev_node):
        self._prev = prev_node
        if prev_node != None:
            prev_node._next= self
    

    def __str__(self):
        
        return str(self.data())
    
    def __repr__(self):
        return repr(self.data())
    
    
class DoublyLinkedList:

    def __init__(self):
        
        self._head = None
        self._tail = None
        self._length = 0
    


    def __len__(self):
        
        return len(self.traverse(lambda x: x))


    def __repr__(self):
        
        return f"SinglyLinkedList({"->".join(self.traverse(repr))})"

    def __str__(self):
        
        return '->'.join(self.traverse(str))
    
    def __iter__(self):

        current = self._head

        while current != None: # another Solution: while current:
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

        if self._head == None:
            self._tail = self._head = Node(data)
        else:
            old_node = self._head
            self._head = Node(data)
            self._head.append(old_node)
        self._length +=1


    def insert_in_back(self,data):

        if self._tail == Node:
            self._tail = self._head = Node(data)
        else:
            old_tail = self._tail
            self._tail = Node(data)
            self._tail.prepend(old_tail)
        self._length +=1

    def insert_at(self,pos, data):
        if pos < 0 or pos > self._length:
            raise IndexError("Index must be postive!")
        if pos ==0:
            self.insert_in_front(data)
        elif pos == self._length:
            self.insert_in_back(data)
        else:
            new_node = Node(data)
            curr = self._head
            for i in range(1, pos):
                curr = curr.next()
            # new_node._next = curr._next
            # new_node._perv = curr
            # curr._next = new_node
            # curr._next._prev = new_node
        
            next_node = curr._next

            new_node._next = next_node
            new_node._prev = curr

            curr._next = new_node
            next_node._prev = new_node

        self._length +=1


    
    def traverse(self,functor):

        result =[]
        current = self._head
        while current != None:
            result.append(functor(current.data()))
            current = current.next()
        return result



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
    
    def delete_from_front(self):


        if self.is_empty():
            raise ValueError("list is empty, can not delete")
        data = self._head.data()
        self._head = self._head.next()
        if self._head == None:
            self._tail = None
        else:
            self._head.prepend(None)
        self._length -=1
        return data
        
    
    def delete_from_back(self):
        
        if self.is_empty():
            raise ValueError('Delete on an empty list.')
        data = self._tail.data()
        self._tail = self._tail.prev()
        if self._tail is None:
            self._head = None
        else:
            self._tail.append(None)
        self._length -=1
        return data
    
    def delete(self,item):
        if self._length ==0:
           raise ValueError('Delete on an empty list!')
        elif self._head == item:
            # self._head = self._head._next
            self.delete_from_front()
        else:
            curr = self._head._next
            while curr != None and curr._data != item:
                curr = curr._next
            if curr == None:
                raise ValueError("Item is not there!")
            elif curr._next == None:
                self.delete_from_back()
            else:
                curr._prev._next = curr._next
                curr._next._prev = curr.prev
            self._length -=1
        
    def reverse(self):
        curr = self._tail

        while curr != None:
            print(curr._data)
            curr = curr._prev
        print("\n")





ll = DoublyLinkedList()


ll.insert_in_front(50)
# ll.insert_in_front(60)
# ll.insert_in_front(70)
# ll.insert_in_front(80)
ll.insert_in_back(0)
ll.insert_in_back(10)
ll.insert_in_back(20)
ll.insert_in_back(30)
ll.insert_in_back(40)
ll.insert_at(2,99)
print("###########Before deleting###########")
print("List:",ll) # (50->0->99->10->20->30->40)
print("size _length:", ll._length)
print("Size of list:",len(ll))
print(repr(ll))


# print("search on 50 in index: ",ll._search(50))
# # ll.delete(10)


# ll.delete_from_front()
# ll.delete_from_front()
# ll.delete_from_front()
# ll.delete_from_front()
# ll.delete_from_front()
# ll.delete_from_front()
# ll.delete_from_front()
# ll.delete_from_front()
# ll.delete_from_front()
# ll.delete_from_front()
print("###########After deleting###########")
ll.delete(30)
ll.delete(20)
ll.insert_at(3,"aha")
print("Size of list:",ll.size())
print("List:",ll)
print(repr(ll))
ll.reverse()



# linked_list = SinglyLinkedList()
# print(len(linked_list))