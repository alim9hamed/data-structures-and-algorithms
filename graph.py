from singly_linked_list import SinglyLinkedList


class Vertex:

    def __init__(self, key):
        self.id = key
        self.adj_list = SinglyLinkedList()

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(repr(self))

    def __str__(self):
        return f"<{str(self.id)}>"

    def __repr__(self):
        return f"Vertex({repr(self.id)})"   

    def has_edge_to(self, destination_vertex):
        return self.adj_list._search(destination_vertex) is not None

    def add_edge_to(self, destination_vertex):

        if self.has_edge_to(destination_vertex):
            raise ValueError(f"Edge already exists: {self} -> {destination_vertex}")
        self.adj_list.insert_in_back(destination_vertex)

    def delete_edge_to(self, destination_vertex):

        try:
            self.adj_list.delete(destination_vertex)

        except ValueError as e:
            raise ValueError(f"Edge does not exist: {self} -> {destination_vertex}") from e

    def outgoing_edges(self):
        return [(self.id, v.id) for v in self.adj_list]


class Graph:

    def __init__(self):
        self.adj = {}

    def __repr__(self):

        def edges_repr(edges):
            return f"[{', '.join((f'->{u}' for _, u in edges))}]"

        adj_lst_repr = (f"{repr(v)}: {edges_repr(v.outgoing_edges())}" for v in self.adj.values())

        return f"Graph({' | '.join(adj_lst_repr)})"

    def get_vertex(self, key):

        if key not in self.adj:
            raise ValueError(f"Vertex {key} not found.")
        return self.adj[key]

    def insert_vertex(self, key):

        if key in self.adj:
            raise ValueError(f"Vertex {key} already exists")
        self.adj[key] = Vertex(key)

    def has_vertex(self, key):
        return key in self.adj

    def delete_vertex(self, key):

        v = self.get_vertex(key)

        for u in self.adj.values():   # FIXED
            if u != v and u.has_edge_to(v):
                u.delete_edge_to(v)

        del self.adj[key]

    def get_vertices(self):
        return set(self.adj.keys())

    def vertex_count(self):
        return len(self.adj)

    def insert_edge(self, key1, key2):

        v1 = self.get_vertex(key1)
        v2 = self.get_vertex(key2)
        v1.add_edge_to(v2)

    def has_edge(self, key1, key2):

        v1 = self.get_vertex(key1)
        v2 = self.get_vertex(key2)
        return v1.has_edge_to(v2)

    def delete_edge(self, key1, key2):

        v1 = self.get_vertex(key1)
        v2 = self.get_vertex(key2)
        v1.delete_edge_to(v2)

    def get_edges(self):
        return set(e for v in self.adj.values() for e in v.outgoing_edges())

    def edges_count(self):
        return sum(len(v.outgoing_edges()) for v in self.adj.values())
    

    def bfs_shortest_path(self, start_vertex, target_vertex):


        if not self.has_vertex(start_vertex):
            raise ValueError(f"SrartVertex({start_vertex}) does not exist in Graph.")

        if not self.has_vertex(target_vertex):
            raise ValueError(f"TargetVertex({target_vertex}) does not exist in Graph.")
        
        def recosstruct_path(predecessor, target):

            path =[]

            while target:
                path.append(target)
                target = predecessor[target]
            return path[::-1]
        
        distance = {v:None for v in self.adj}
        predecessor = {v:None for v in self.adj}

        queue = []
        queue.append(start_vertex)
        distance[start_vertex] = 0

        while queue:

            u = queue.pop(0)

            if u == target_vertex:

                return recosstruct_path(predecessor,target_vertex)
            
            for (_,v) in self.get_vertex(u).outgoing_edges():
                
                if distance[v] == None:
                    distance[v] = distance[u] +1
                    predecessor[v] = u
                    queue.append(v)

        
        return None


    def bfs_traversal(self, start):
        visited = set()
        result = []

        def bfs_connected(src):
            queue = []

            queue.append(start)
            visited.add(start)

            while queue:
                u  = queue.pop(0)
                result.append(u)

                for _,v in self.get_vertex(u).outgoing_edges():
                    if v not in visited:
                        visited.add(v)
                        queue.append(v)
        bfs_connected(start)
        
        for vertex in self.get_vertices():
            if vertex not in visited:
                bfs_connected(vertex)


        return result
                 

    def dfs(self, start_vertex):

        if not self.has_vertex(start_vertex):
            raise ValueError(f" SrartVertex({start_vertex}) does not exist in Graph.")
        
        visited = set()
        curr_path = set()

        acyclic = True
        stack = []
        stack.append((False,start_vertex))

        while stack:

            leave, v = stack.pop()

            if leave:
                curr_path.remove(v)
            elif v in curr_path:
                acyclic = False 
            elif v not in visited:

                visited.add(v)
                curr_path.add(v)

                stack.append((True, v))

                for _,u in self.get_vertex(v).outgoing_edges():
                    stack.append((False, u))
        

        return acyclic, visited
    

    def dfs_traversal(self,start_vertex):

        if not self.has_vertex(start_vertex):
            raise ValueError(f" SrartVertex({start_vertex}) does not exist in Graph.")
        
        visited = set()
        result = []

        def dfs_rec(v_key):

            visited.add(v_key)
            result.append(v_key)

            Vertex = self.get_vertex(v_key)

            for _,w in Vertex.outgoing_edges():
                if w not in visited:
                    dfs_rec(w)

        

        for v_key in self.get_vertices():
            if v_key not in visited:
                dfs_rec(v_key)

        return result


