import heapq
hq = []
N = int(input())
for _ in range(N):
    row = map(int, input().split())
    for i in row:
        if len(hq) >= N:
            heapq.heappushpop(hq,i)
        
        else:
            heapq.heappush(hq, i)

print(heapq.heappop(hq))