class Node:

    @staticmethod
    def _node_str(node):
        return str(node) if node != None else ''

    def __init__(self,value,left: Node= None,right: Node = None):

        self._value = value
        self._left = left
        self._right = right

    def __str__(self):
        left_str = Node._node_str(self._left)
        right_str = Node._node_str(self._right)
        return f"{self._value} ({left_str})({right_str})"

    def find_min_in_subtree(self):

        parent = None
        node = self

        while node._left != None:
            parent = node
            node = node._left

        return node, parent
    

    def find_max_in_subtree(self):

        parent = None
        node = self

        while node._right != None:
            parent = node
            node = node._right

        return node, parent
    

class BinarySearchTree:

    def __init__(self):
        
        self._root = None

    
    def __repr__(self) -> str:
        return f'BinarySearchTree({str(self)})'


    def __str__(self) -> str:
        return Node._node_str(self._root)
    

    def search(self, value):

        parent = None
        node = self._root

        while node != None:
            
            if value == node._value:
                return node, parent
            elif value < node._value:
                parent = node
                node = node._left
            else:
                parent = node
                node = node._right
        return None, None


    def insert(self, value):


        node = self._root 
        if node == None:
            self._root = Node(value)
            return  
        else:

            while True:

                if value <= node._value :

                    if node._left == None:
                        node._left = Node(value)
                        break

                    else:

                        node = node._left
                else: 

                    if node._right == None:
                        node._right = Node(value)
                        break
                    else:
                        node = node._right



    def delete(self, value):

        if self._root == None:
            raise ValueError("try to delete empty tree.")
        
        node, parent = self.search(value)
        if node == None:
            raise ValueError("Node not found")
        

        if node._left == None and node._right == None:

            if parent == None:
                self._root = None
            elif parent._left == node:
                parent._left = None
            else:
                parent._right = None
        elif node._left == None or node._right == None:
            child = node._left if node._left != None else node._right

            if parent == None:
                self._root = child
            elif parent._left == node:
                parent._left = child
            else:
                parent._right = child

        else:
            max_node, max_parent = node._left.find_max_in_subtree()

            node._value = max_node._value

            if parent == None:
                node._left = max_node._left
            else:
                max_parent._right = max_node._left

    def print_tree(self):

        def _print(node, level=0):

            if node is None:
                return

            _print(node._right, level + 1)

            print("    " * level + str(node._value))

            _print(node._left, level + 1)

        _print(self._root)

## In Order traversal 
def inorder(node):
    if node is None:
        return

    inorder(node._left)
    print(node._value)
    inorder(node._right)

## Post Order Traversal
def post_order(node):

    if node == None:
        return
    post_order(node._left)
    post_order(node._right)
    print(node._value)

## Pre Order Traversal
def pre_order(node):

    if node == None:
        return
    print(node._value)
    pre_order(node._left)
    pre_order(node._right)

def count(node):
    if node is None:
        return 0

    return 1 + count(node._left) + count(node._right)

bst = BinarySearchTree()

for x in [50, 30, 70, 20, 40, 60, 80]:
    bst.insert(x)

bst.print_tree()

print("Count of Node:",count(bst._root) )
print("@@@ Inorder Traversal@@@")
inorder(bst._root)

print("@@@ Postorder Traversal@@@")
post_order(bst._root)
print("@@@ Preorder Traversal@@@")
pre_order(bst._root)

















# class BinarySearchTree:

#     def __init__(self):
#         self.root = None

#     # =========================
#     # RECURSIVE INSERT
#     # =========================
#     def insert(self, value):
#         self.root = self._insert(self.root, value)

#     def _insert(self, node, value):

#         if node is None:
#             return Node(value)

#         if value <= node.value:
#             node.left = self._insert(node.left, value)
#         else:
#             node.right = self._insert(node.right, value)

#         return node

#     # =========================
#     # SEARCH (iterative for simplicity)
#     # =========================
#     def search(self, value):
#         parent = None
#         node = self.root

#         while node:
#             if value == node.value:
#                 return node, parent
#             elif value < node.value:
#                 parent = node
#                 node = node.left
#             else:
#                 parent = node
#                 node = node.right

#         return None, None

#     # =========================
#     # RECURSIVE DELETE
#     # =========================
#     def delete(self, value):
#         self.root = self._delete(self.root, value)

#     def _delete(self, node, value):

#         if node is None:
#             return None

#         # go left
#         if value < node.value:
#             node.left = self._delete(node.left, value)

#         # go right
#         elif value > node.value:
#             node.right = self._delete(node.right, value)

#         else:
#             # =========================
#             # CASE 1: leaf
#             # =========================
#             if node.left is None and node.right is None:
#                 return None

#             # =========================
#             # CASE 2: one child
#             # =========================
#             if node.left is None:
#                 return node.right
#             if node.right is None:
#                 return node.left

#             # =========================
#             # CASE 3: two children
#             # =========================
#             max_node = self._find_max(node.left)

#             node.value = max_node.value

#             node.left = self._delete(node.left, max_node.value)

#         return node

#     # =========================
#     # FIND MAX (recursive helper)
#     # =========================
#     def _find_max(self, node):
#         if node.right is None:
#             return node
#         return self._find_max(node.right)

#     # =========================
#     # PRINT TREE
#     # =========================
#     def print_tree(self):
#         self._print(self.root)

#     def _print(self, node, level=0):
#         if node is None:
#             return

#         self._print(node.right, level + 1)
#         print("    " * level + str(node.value))
#         self._print(node.left, level + 1)




# def insert(node, value):

#     if node is None:
#         return Node(value)

#     if value < node.value:
#         node.left = insert(node.left, value)

#     else:
#         node.right = insert(node.right, value)

#     return node

# def delete(node, value):

#     if node is None:
#         return None

#     if value < node.value:
#         node.left = delete(node.left, value)

#     elif value > node.value:
#         node.right = delete(node.right, value)

#     else:

#         # Case 1 & 2

#         if node.left is None:
#             return node.right

#         if node.right is None:
#             return node.left

#         # Case 3

#         successor = min_value(node.right)

#         node.value = successor.value

#         node.right = delete(
#             node.right,
#             successor.value
#         )

#     return node