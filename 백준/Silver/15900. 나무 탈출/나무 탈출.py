# 모든 리프 노드들의 경로 합을 구해서 홀짝 판정
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
g = [[] for _ in range(N+1)]
sum_routes  = 0
depths = [-1] * (N+1)

for _ in range (N-1):
    v,i = map(int, input().split())
    g[v].append(i)
    g[i].append(v)

stack = [(1,0)]
while stack:
    v,d = stack.pop()
    if v !=1 and len(g[v]) == 1:
        sum_routes += d
        continue
    for i in g[v]:
        if depths[i] == -1:
            next_depth = d+1
            depths[i] = next_depth
            stack.append((i,next_depth))
if sum_routes % 2 == 0:
    print("No")
else:
    print("Yes")




    