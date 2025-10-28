
from collections import deque


def DFS(g,v,visited):
    visited[v] = True
    visited_nodes_DFS.append(v)
    for i in g[v]:
        if not visited[i]:
            DFS(g,i,visited)
def BFS(start_node, g):
    queue = deque([start_node])
    visited = [False] * (N+1)
    visited[start_node] = True
    visited_nodes = [start_node]
    while queue:
        curr_node = queue.popleft()
        for i in g[curr_node]:
            if not visited[i]:           
                visited[i] = True
                visited_nodes.append(i)
                queue.append(i)
    return " ".join(map(str, visited_nodes))
N,M,V = map(int,input().split())

graph = {i: [] for i in range(1, N+1)}
visited_DFS = [False] * (N+1)
visited_nodes_DFS = [] 
for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1,N+1):
    graph[i].sort()
DFS(graph,V, visited_DFS)
print(" ".join(map(str, visited_nodes_DFS)))
print(BFS(V, graph))
