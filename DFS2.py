def dfs(graph, start, goal):
    visited = [start]
    stack = [start]
    parent = {start: None}

    while stack:
        node = stack[-1]

        if goal == node:
            break

        found = False

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                stack.append(neighbour)
                parent[neighbour] = node
                print("Visited", neighbour)
                found = True
                break

        if not found:
            stack.pop()

    if goal not in visited:
        return None

    path = []
    node = goal

    while node is not None:
        path.append(node)
        node = parent[node]

    path.reverse()
    return path

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

path = dfs(graph, 'A', 'F')

if path:
    print("Path is", path)
else:
    print("Path doesn't exist")
    
