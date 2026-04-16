import sys
input = sys.stdin.readline

meetings = []
N = int(input())

for _ in range(N):
    start, end = map(int, input().split())
    meetings.append((end, start))

meetings.sort()

t = 0
answer = 0

for end, start in meetings:
    if t<=start:
        answer += 1
        t = end
print(answer)