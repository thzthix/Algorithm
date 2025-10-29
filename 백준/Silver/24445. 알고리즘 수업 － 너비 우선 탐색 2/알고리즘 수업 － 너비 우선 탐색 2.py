import sys
from collections import deque
input = sys.stdin.readline
def BFS(start_node, graph, N):
    queue = deque([start_node])
    visited = set([start_node])
    count = 1
    result = [0] * (N+1)
    result[start_node] = count
    while queue:
        curr_node = queue.popleft()    
        for i in sorted(graph[curr_node], reverse=True):
            if i not in visited:
                queue.append(i)
                visited.add(i)
                count+=1
                result[i] = count
                

    return result

N,M,R = map(int, input().split())
graph = [[] for i in range(N+1)]
for i in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
result = BFS(R, graph, N)
for i in range(1, N+1):
    print(result[i])
