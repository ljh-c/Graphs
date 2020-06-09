"""
Use unidirectional edges to represent parent-child relationship

ancestors is a list of edges (parent, child)

For our problem, it may be useful to designate an edge as (parent <-- child)

Earlier ancestors have more edges from start node

Return the earliest ancestor

- Breadth-first traversal of ancestors to get earliest ancestors
- Use queue to evaluate generation by generation
- If generation has no parents, return ancestor with lowest id
- If no parents, return -1
"""
from collections import deque

# def get_ancestors(ancestors, starting_node):
#     node_parents = {p for p, child in ancestors if child == starting_node}

#     return node_parents

def earliest_ancestor(ancestors, starting_node):
    q = deque([[starting_node]])

    while len(q) > 0:
        gen = q.popleft()
        # print(gen)

        new_gen = []

        for node in gen:
            new_gen.extend([p for p, child in ancestors if child == node])

        if new_gen:
            q.extend([new_gen])
        else:
            return min(gen) if min(gen) != starting_node else -1

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(test_ancestors, 2))