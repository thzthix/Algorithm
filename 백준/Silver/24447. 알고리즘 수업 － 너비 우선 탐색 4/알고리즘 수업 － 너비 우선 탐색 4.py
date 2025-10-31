import sys
from collections import deque
input = sys.stdin.readline

def BFS(start_node, graph):
    queue = deque([(start_node,0)])
    visited = set([start_node])
    curr_order = 1
    result = 0
    while queue:
        curr_node, depth = queue.popleft()
        for i in sorted(graph[curr_node]):
            if i not in visited:
                child_depth = depth+1
                curr_order +=1
                queue.append((i,child_depth))
                visited.add(i)
                result += child_depth * curr_order
                
    return result

N,M,R = map(int, input().split())
graph = [[] for i in range(N+1) ]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
print(BFS(R,graph))