import sys
input= sys.stdin.readline

N = int(input())
counts = [0] * 10001
for i in range(N):
    counts[int(input())] +=1
for i in range(len(counts)):
    number = counts[i]
    for _ in range(number):
        print(i)