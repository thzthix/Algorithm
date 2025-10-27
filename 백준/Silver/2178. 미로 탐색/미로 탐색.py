from collections import deque
def BFS(end_x, end_y, graph):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
   
    queue = deque([(1,1,1)])
    visited = set([(1, 1)])
    while queue:
        x,y, path = queue.popleft()
        if x == end_x and y == end_y:
            return path
        for i in range (4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 1<= nx <=end_x  and 1<= ny<=end_y  and graph[nx][ny] == 1:
                if (nx, ny) not in visited:
                    visited.add((nx,ny))
                    queue.append((nx, ny, path + 1))
            
            
    return -1
N,M = map(int, input().split())
graph = [ [0] * (M+1) for i in range(N+1)]
for i in range(1,N+1):
    row =  input().strip()
    for j in range(1, M+1):
        graph[i][j] = int(row[j-1])
print(BFS(N,M,graph))


