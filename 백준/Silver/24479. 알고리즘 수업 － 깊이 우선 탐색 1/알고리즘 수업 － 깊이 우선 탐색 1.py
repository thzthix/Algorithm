import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def DFS(g,v,visited):
    global count
    count+=1
    visited[v] = count
    for i in g[v]:
        if visited[i] == 0:
            DFS(g,i,visited)
    

N,M,R = map(int,input().split())
visited = [0] * (N+1)
nodes = [[] for _ in range(N+1)]
for i in range(M):
    a,b = map(int,input().split())
    nodes[a].append(b)
    nodes[b].append(a)
for i in range(1, N+1):
    nodes[i].sort()
count = 0
DFS(nodes, R, visited)
for i in range(1,N+1):
    print(visited[i])