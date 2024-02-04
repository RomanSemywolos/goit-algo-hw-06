from graph import subway, show_graph
import networkx as nx


def dfs_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for neighbor in graph.neighbors(start):
        if neighbor not in path:
            new_paths = dfs_paths(graph, neighbor, end, path)
            for p in new_paths:
                paths.append(p)
    return paths


def bfs_paths(graph, start, end):
    queue = [(start, [start])]
    paths = []
    while queue:
        current, path = queue.pop(0)
        for neighbor in graph.neighbors(current):
            if neighbor not in path:
                new_path = path + [neighbor]
                queue.append((neighbor, new_path))
                if neighbor == end:
                    paths.append(new_path)
    return paths

start = "Heroiv Dnipra"
end = "Hydropark"

dfs_tree = dfs_paths(subway, start, end)
bfs_tree = bfs_paths(subway, start, end)

print(f"dfs tree: {dfs_tree}\n")
print(f"bfs tree: {bfs_tree}\n")

dfs_tree = nx.dfs_tree(subway, source="Heroiv Dnipra")
bfs_tree = nx.bfs_tree(subway, source="Heroiv Dnipra")

show_graph(dfs_tree, "DFS Tree")
show_graph(bfs_tree, "BFS Tree")