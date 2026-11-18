# Data Structures and Algorithms: Study Portfolio

This repository contains Python learning implementations created while studying
data structures and algorithms. The notes below explain the concepts represented
in the code and connect them to related topics in the two Grokking books. This is
an original study guide, not a reproduction of either book.

## What this repository covers

### Data structures

| Topic | What it means | Implementations |
|---|---|---|
| Arrays | Store values in indexed, contiguous storage. Indexing is fast, while inserting or deleting in the middle may require shifting values. | `dynamic_array.py`, `sorted_array.py` |
| Linked lists | Connect nodes with references rather than requiring adjacent storage. A singly linked list moves forward; a doubly linked list also links backward; a circular list links its tail back into the list. | `singly_linked_list.py`, `doubly_linked_list.py`, `circular_linked_list.py` |
| Stacks | Follow last-in, first-out (LIFO): the latest pushed value is the first popped. | `stack_based_linked_list.py`, `stack_based_fixed_array.py`, `stack_based_dynamic_array.py` |
| Queues | Follow first-in, first-out (FIFO): the earliest enqueued value is the first dequeued. The code explores array-backed and linked-list-backed designs. | `queue_based_fixed_array.py`, `queue_based_singly_linked_list.py` |
| Hash tables | Map keys to values using a hash function. Separate chaining stores multiple colliding keys in a bucket. | `hash_table.py` |
| Binary search trees | Organize values so that smaller values are in the left subtree and larger values are in the right subtree, enabling ordered search and traversal. | `bst.py`, `bst_recursivepy` |
| Heaps and priority queues | A heap keeps the highest-priority element accessible at the root. A sorted-array priority queue demonstrates a different implementation trade-off. | `heap.py`, `priority_queue_based_sorted_array.py` |
| Graphs | Represent vertices and directed edges with adjacency lists; graph operations and traversals build on that representation. | `graph.py`, `test_graph.py` |

### Algorithms

| Topic | Explanation | Implementations |
|---|---|---|
| Binary search | Repeatedly halves the remaining search interval. It requires sorted input and takes `O(log n)` time. | `SortedArray.binary_search` in `sorted_array.py` |
| Elementary sorting | Selection sort repeatedly selects the next minimum; insertion sort places each value into its sorted prefix; bubble sort swaps out-of-order neighbors. These are typically `O(n^2)` in the average and worst cases. | `sorting_algorithms/selection_sort.py`, `sorting_algorithms/insertion_sort.py`, `sorting_algorithms/bubble_sort.py` |
| Merge sort | Recursively divides an input, sorts each half, and merges the sorted halves. It takes `O(n log n)` time and uses additional space for the merge. | `sorting_algorithms/merge_sort.py` |
| Recursion and tree traversal | A recursive function solves a smaller subproblem or visits child nodes, then combines or reports results. The repository uses this in merge sort and the BST traversal/count helpers. | `sorting_algorithms/merge_sort.py`, `bst.py` |
| Breadth-first search (BFS) | Visits a graph level by level. On an unweighted graph, BFS can find a path with the fewest edges. | `Graph.bfs_shortest_path` and `Graph.bfs_traversal` in `graph.py` |
| Depth-first search (DFS) | Explores a branch before backtracking, using a stack or recursion. | `Graph.dfs` and `Graph.dfs_traversal` in `graph.py` |

## Complexity at a glance

These are the standard costs for the underlying data-structure operations; actual
costs depend on the specific implementation and input.

| Structure or operation | Typical time |
|---|---|
| Array index access | `O(1)` |
| Dynamic-array append | Amortized `O(1)`; `O(n)` when resizing |
| Linked-list search or indexed access | `O(n)` |
| Stack push/pop | `O(1)` |
| Linked queue enqueue/dequeue | `O(1)` when front and rear references are maintained |
| Hash-table lookup/insert/delete | Average `O(1)`, worst-case `O(n)` |
| Binary-search-tree search/insert/delete | Average `O(log n)`, worst-case `O(n)` if the tree is unbalanced |
| Heap insert/remove highest-priority item | `O(log n)` |
| Heap peek | `O(1)` |
| Binary search | `O(log n)` |
| Selection, insertion, and bubble sort | Typically `O(n^2)` |
| Merge sort | `O(n log n)` |
| BFS/DFS with adjacency lists | `O(V + E)` with an efficient queue/stack, where `V` is vertices and `E` is edges |

The graph BFS methods currently use a Python list as a queue. Removing from the
front of a list shifts its remaining elements, so the implementation can be
slower than the standard `O(V + E)` BFS bound. A `collections.deque` is the usual
choice for an efficient FIFO queue.

## Mapping to the books

The mapping below connects topics visible in this repository to related parts
of the books. It does not claim that every chapter was completed, and chapter
numbering or headings may differ by edition.

### *Grokking Data Structures*

The code gives hands-on examples of the book's core data-structure themes:

- **Arrays and dynamic storage:** fixed-capacity sorted arrays and a resizable
  dynamic array.
- **Linked lists:** singly, doubly, and circular linked-list variants.
- **Stacks and queues:** LIFO and FIFO behavior implemented with arrays and
  linked nodes.
- **Hash tables:** hashing, bucket collisions, and separate chaining.
- **Trees:** binary search, insertion, deletion, and traversals in a binary
  search tree.
- **Heaps and priority queues:** heap ordering and operations, alongside a
  sorted-array priority-queue design.
- **Graphs:** vertices, edges, adjacency lists, and graph traversal.

### *Grokking Algorithms*

The repository connects most directly to these algorithm topics:

- **Binary search:** `sorted_array.py`.
- **Sorting and recursion:** elementary sorts and merge sort.
- **Hash tables:** `hash_table.py`.
- **Graph search:** BFS and DFS in `graph.py`; BFS also illustrates shortest
  paths in an unweighted graph.
- **Algorithm analysis:** the contrasting operation costs in arrays, lists,
  trees, heaps, sorting, and graph traversal provide examples for reasoning
  about time and space complexity.

There are no dedicated implementations in the current repository for topics
such as Dijkstra's algorithm, greedy algorithms, dynamic programming, or
k-nearest neighbors. They should only be described as completed study topics if
they were studied separately.

## Notes about the code

These are independent learning exercises rather than a packaged production
library. Some scripts include demonstration code that runs when the file is
executed. The graph implementation has a focused unit-test file,
`test_graph.py`.

## References

- *Grokking Data Structures* — [user-provided reference](https://studylib.net/doc/28053531/grokking-data-structures)
- *Grokking Algorithms* — [user-provided reference](https://github.com/yokharian/MyBooks/blob/master/Grokking%20Algorithms.pdf)

## LinkedIn post draft

I have been studying data structures and algorithms and building small Python
implementations to make the concepts concrete.

This repository includes arrays, linked lists, stacks, queues, hash tables,
binary search trees, heaps, priority queues, sorting algorithms, and graph
traversals such as BFS and DFS. Working through these examples helped me compare
the trade-offs between data structures and reason about algorithm complexity.

This is an ongoing learning project, and I plan to continue adding and testing
more algorithms.

`[Add your repository link here]`

#DataStructures #Algorithms #Python #ComputerScience #ContinuousLearning

## Run the graph tests

```bash
python -m unittest test_graph.py
```

These are learning exercises and are not intended as a production-ready library.
