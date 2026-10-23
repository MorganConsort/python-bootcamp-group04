"""W1-4: Translate C++ to Python – In-place insertion sort.

Unlike C++'s std::vector<int>, a Python list supports dynamic resizing and
does not require explicit memory management. The sort is performed in-place
by shifting elements, identical to the C++ algorithm.
"""


def insertion_sort(a):
    """Sort a list of integers in-place using insertion sort and return it."""
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


# Keep the original graph traversal code for reference
def build_graph(edges, directed=False, nodes=None):
    """Build sorted, duplicate-free adjacency lists, including isolated nodes."""
    neighbors = {node: set() for node in nodes or []}
    for source, target in edges:
        neighbors.setdefault(source, set()).add(target)
        neighbors.setdefault(target, set())
        if not directed:
            neighbors[target].add(source)
    return {node: sorted(adjacent) for node, adjacent in neighbors.items()}


def dfs(graph, start):
    """Recursively visit reachable nodes, visiting smaller neighbors first."""
    if start not in graph:
        raise ValueError("start must be a node in the graph")

    visited = set()
    order = []

    def visit(node):
        visited.add(node)
        order.append(node)
        for neighbor in sorted(graph.get(node, [])):
            if neighbor not in visited:
                visit(neighbor)

    visit(start)
    return order


def dfs_iterative(graph, start):
    """Match recursive DFS using a stack, without Python's recursion limit."""
    if start not in graph:
        raise ValueError("start must be a node in the graph")
    visited = set()
    order = []
    stack = [start]
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        stack.extend(reversed(sorted(graph.get(node, []))))
    return order
