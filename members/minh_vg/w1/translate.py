"""Represent graphs with adjacency lists and traverse them depth first.

Unlike C++'s vector<vector<int>>, a Python dict supports node labels that
need not be consecutive. A set replaces vector<bool> for visited nodes, and
the traversal functions return their order instead of filling an output
parameter. The iterative version avoids Python's recursion depth limit.
"""


def build_graph(
    edges: list[tuple[int, int]],
    directed: bool = False,
    nodes: list[int] | None = None,
) -> dict[int, list[int]]:
    """Build sorted, duplicate-free adjacency lists, including isolated nodes."""
    neighbors = {node: set() for node in nodes or []}
    for source, target in edges:
        neighbors.setdefault(source, set()).add(target)
        neighbors.setdefault(target, set())
        if not directed:
            neighbors[target].add(source)
    return {node: sorted(adjacent) for node, adjacent in neighbors.items()}


def dfs(graph: dict[int, list[int]], start: int) -> list[int]:
    """Recursively visit reachable nodes, visiting smaller neighbors first."""
    if start not in graph:
        raise ValueError("start must be a node in the graph")

    visited = set()
    order = []

    def visit(node: int) -> None:
        visited.add(node)
        order.append(node)
        for neighbor in sorted(graph.get(node, [])):
            if neighbor not in visited:
                visit(neighbor)

    visit(start)
    return order


def dfs_iterative(graph: dict[int, list[int]], start: int) -> list[int]:
    """Use an explicit stack to produce the same first-visit order as dfs."""
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
        # Mark nodes on pop so a cross edge can still reach a pending node first.
        stack.extend(
            neighbor
            for neighbor in sorted(graph.get(node, []), reverse=True)
            if neighbor not in visited
        )
    return order
