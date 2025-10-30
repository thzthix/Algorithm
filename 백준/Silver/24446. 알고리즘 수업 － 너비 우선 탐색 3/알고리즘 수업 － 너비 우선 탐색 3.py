import queue
import sys
from collections import deque
input = sys.stdin.readline
def BFS(start_node, graph, N):
    queue = deque([start_node])
    visited = set([start_node])
    depths = [-1] * (N+1)
    depths[start_node] = 0
    while queue:
        curr_node = queue.popleft()
        curr_depth = depths[curr_node]
        for i in graph[curr_node]:
            if i not in visited:
                queue.append(i)
                visited.add(i)
                depths[i] = (curr_depth +1)
    return depths

N,M,R = map(int, input().split())
graph = [[] for i in range(N+1)]
for i in range(1, M+1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
depths = BFS(R,graph,N)
for i in range(1, N+1):
    print(depths[i])