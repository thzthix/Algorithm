import sys
input = sys.stdin.readline

meetings = []
N = int(input())

for _ in range(N):
    meetings.append( tuple(map(int, input().split())))

meetings.sort(key = lambda x: (x[1], x[0]))

t = 0
answer = 0

for start, end in meetings:
    if t<= start:
        answer += 1
        t = end
print(answer)