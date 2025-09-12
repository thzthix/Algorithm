import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

count = 0
def DFS(g,v,visited):
    global count
    count += 1
    visited[v] = count
    for i in g[v]:
        if visited[i] == 0:
            DFS(g, i, visited)

n, m, r = map(int, input().split())
graph = [[] for i in range(n+1)]
visited = [0] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort(reverse=True)

DFS(graph, r, visited)

for i in range(1, n+1):
    print(visited[i])