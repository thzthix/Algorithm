import sys
input = sys.stdin.readline
output = sys.stdout.write

N = int(input())
info = []
for _ in range(N):
    age, name = input().rstrip().split()
    info.append((name,int(age)))
info.sort(key = lambda x: (x[1]))
for name, age in info:
    output(f"{age} {name}\n")