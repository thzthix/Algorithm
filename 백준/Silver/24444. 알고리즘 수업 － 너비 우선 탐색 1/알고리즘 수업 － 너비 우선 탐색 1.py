from collections import deque
import sys
input = sys.stdin.readline
def BFS(start_node, graph):
    visit_order = [0] * (N+1)
    visit_count = 1
    queue = deque([start_node])
    visited = set([start_node])
    visit_order[start_node] = visit_count
    while queue:
        curr_node = queue.popleft()
        for i in sorted(graph[curr_node]):
            if i not in visited:
                queue.append(i)
                visited.add(i)
                visit_count+=1
                visit_order[i] = visit_count
    return visit_order



    
N,M,R = map(int, input().split())

graph = [[] for i in range(N+1)]
for i in range(M):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
visited_order = BFS(R, graph)
for i in range(1,N+1):
    print(visited_order[i])

