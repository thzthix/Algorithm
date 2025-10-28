from collections import deque


def DFS(g,v,visited, result):
    visited[v] = True
    result.append(v)
    for i in g[v]:
        if not visited[i]:
            DFS(g,i,visited, result)
    return result

def BFS(start_node, g, result):
    queue = deque([start_node])
    visited = [False] * (N+1)
    visited[start_node] = True
    result.append(start_node)
    while queue:
        curr_node = queue.popleft()
        for i in g[curr_node]:
            if not visited[i]:           
                visited[i] = True
                result.append(i)
                queue.append(i)
    return result

N,M,V = map(int,input().split())

graph = [[] for i in range(N+1)]
visited_DFS = [False] * (N+1)
result_DFS = []
result_BFS = []
for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for adj_list in graph:
    adj_list.sort()
print(" ".join(map(str,DFS(graph,V, visited_DFS , result_DFS ))))
print(" ".join(map(str, BFS(V,graph, result_BFS))))
