import sys
input = sys.stdin.readline
output = sys.stdout.write
N = int(input())
numbers = [list(map(int, input().split())) for _ in range(N)]
numbers.sort(key=lambda x:(x[0], x[1]))
for i in range(N):
    output(f"{numbers[i][0]} {numbers[i][1]}\n")