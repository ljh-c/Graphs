"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id in self.vertices:
            raise KeyError(f'vertex {vertex_id} has already been added')
        else:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 not in self.vertices or v2 not in self.vertices:
            raise IndexError(f'vertex {v1} and/or {v2} not in vertices')
        else:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id not in self.vertices:
            raise IndexError(f'vertex {vertex_id} does not exist')
        else:
            return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        q.enqueue(starting_vertex)
        visited = set()

        while q.size() > 0:
            curr = q.dequeue()

            if curr not in visited:
                print(curr)
                visited.add(curr)

                for neighbor in self.get_neighbors(curr):
                    q.enqueue(neighbor)
            else:
                continue
        
        # print(visited)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        s.push(starting_vertex)
        visited = set()

        while s.size() > 0:
            curr = s.pop()

            if curr not in visited:
                print(curr)
                visited.add(curr)

                for neighbor in self.get_neighbors(curr):
                    s.push(neighbor)
            else: 
                continue
        
        # print(visited)

    def dft_recursive(self, starting_vertex, visit_set=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        visited = set() if not visit_set else visit_set

        if starting_vertex not in visited:
            visited.add(starting_vertex)
            print(starting_vertex)

            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create a queue and enqueue a PATH to the starting vertex
        q = Queue()
        q.enqueue([starting_vertex])
        # Create a set to store visited vertices
        visited = set()
        # While the queue is not empty:
        while q.size() > 0:
            # Dequeue the first PATH
            curr = q.dequeue()
            # Grab the last vertex from the PATH
            vertex = curr[-1]
            # If that vertex has not been visited:
            if vertex not in visited:
                # Check if it's the target
                if vertex == destination_vertex:
                    # Return PATH
                    return curr
                # Mark as visited
                visited.add(vertex)
                # Add a PATH to its neighbors to the back of the queue
                for neighbor in self.get_neighbors(vertex):
                    # Copy path because different paths are added
                    path = curr.copy()
                    # Append neighbor - append returns None
                    path.append(neighbor)
                    q.enqueue(path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create a stack for paths and a set for visited vertices
        s = Stack()
        s.push([starting_vertex])
        visited = set()
        # While the stack is not empty, evaluate the next path
        while s.size() > 0:
            curr = s.pop()
            # If the last vertex has not been visited:
            vertex = curr[-1]
            if vertex not in visited:
                # Check if target
                if vertex == destination_vertex:
                    return curr
                # Mark as visited and add extended path to stack
                visited.add(vertex)
                for neighbor in self.get_neighbors(vertex):
                    # Copy path and append neighbor
                    path = curr.copy()
                    path.append(neighbor)
                    s.push(path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visit_set=None, prev_path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # Establish visited vertices and current path
        visited = set() if not visit_set else visit_set
        path = [] if not prev_path else prev_path
        curr_path = path + [starting_vertex]
        # path += [starting_vertex] doesn't work because it is using same path
        
        if starting_vertex == destination_vertex:
            return curr_path
        
        # Mark as visited and recursively search rest of graph
        visited.add(starting_vertex)

        for neighbor in self.get_neighbors(starting_vertex):
            # If neighbor has not been visited
            if neighbor not in visited:
                new_path = self.dfs_recursive(neighbor, destination_vertex, visited, curr_path)
            
                if new_path:
                    return new_path
            
        return None

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    # '''
    # Valid DFT paths:
    #     1, 2, 3, 5, 4, 6, 7
    #     1, 2, 3, 5, 4, 7, 6
    #     1, 2, 4, 7, 6, 3, 5
    #     1, 2, 4, 6, 3, 5, 7
    # '''
    graph.dft(1)
    graph.dft_recursive(1)

    # '''
    # Valid BFS path:
    #     [1, 2, 4, 6]
    # '''
    print(graph.bfs(1, 6))

    # '''
    # Valid DFS paths:
    #     [1, 2, 4, 6]
    #     [1, 2, 4, 7, 6]
    # '''
    print(graph.dfs(1, 6))
    print('hello', graph.dfs_recursive(1, 6))

